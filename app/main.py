from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
import uuid
import logging

from app.core.model import InsightFaceModel
from app.core.faiss_index import FaissIndex
from app.core.firebase_storage import FirebaseStorageClient

from app.db.database import SessionLocal, engine
from app.db.models import Base, Face, Photo

from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_BUCKET = os.getenv("FIREBASE_BUCKET_NAME")
FIREBASE_KEY_PATH = os.getenv("FIREBASE_CREDENTIALS")

# -------------------------------------------------
# App setup
# -------------------------------------------------
app = FastAPI(title="Face Search API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

# -------------------------------------------------
# Initialize DB (ONCE)
# -------------------------------------------------
Base.metadata.create_all(bind=engine)

# -------------------------------------------------
# Core services
# -------------------------------------------------
model = InsightFaceModel()
faiss_index = FaissIndex()

firebase = FirebaseStorageClient(
    bucket_name=FIREBASE_BUCKET,  # 🔴 CHANGE THIS
    service_account_path=FIREBASE_KEY_PATH,  # 🔴 CHANGE THIS
)

# -------------------------------------------------
# Health
# -------------------------------------------------
@app.get("/")
def root():
    return {"status": "Face search backend running"}

# -------------------------------------------------
# Upload photo
# -------------------------------------------------
@app.post("/upload-photo")
async def upload_photo(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(400, "Invalid image")

    faces = model.extract_faces(img)
    if not faces:
        raise HTTPException(400, "No face detected")

    db = SessionLocal()

    try:
        photo_id = str(uuid.uuid4())
        photo_url = firebase.upload_bytes(
            image_bytes,
            f"photos/{photo_id}.jpg"
        )

        photo = Photo(id=photo_id, url=photo_url)
        db.add(photo)
        db.commit()

        for face in faces:
            emb = face["embedding"]

            # FAISS
            faiss_id = faiss_index.add(emb, {"photo_id": photo_id})

            face_row = Face(
                photo_id=photo_id,
                faiss_id=faiss_id,
                confidence=face.get("confidence"),
                bbox=face.get("bbox"),
            )
            db.add(face_row)

        db.commit()

    finally:
        db.close()

    return {
        "photo_id": photo_id,
        "faces_detected": len(faces),
        "photo_url": photo_url,
    }

# -------------------------------------------------
# Search
# -------------------------------------------------
@app.post("/search")
async def search(file: UploadFile = File(...), top_k: int = 5):
    image_bytes = await file.read()
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(400, "Invalid image")

    faces = model.extract_faces(img)
    if not faces:
        raise HTTPException(400, "No face detected")

    # Use first detected face as query
    query_emb = faces[0]["embedding"]

    distances, indices = faiss_index.search(query_emb, top_k)

    THRESHOLD = 1.2  # 🔑 InsightFace recommended

    db = SessionLocal()
    results = []

    for d, idx in zip(distances, indices):

        # 🚫 Distance filter (MOST IMPORTANT)
        if d > THRESHOLD:
            continue

        meta = faiss_index.get_metadata(idx)
        if not meta:
            continue

        photo = db.query(Photo).filter(Photo.id == meta["photo_id"]).first()
        if photo:
            results.append({
                "photo_id": photo.id,
                "photo_url": photo.url,
                "distance": float(d),
            })

    db.close()

    return {
        "matches": results,
        "query_faces": len(faces),
        "threshold": THRESHOLD,
    }
