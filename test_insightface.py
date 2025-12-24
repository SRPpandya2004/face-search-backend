#_____________________________________For Step 4_________________________Download Buffalo Model___________#
# import insightface
# from insightface.app import FaceAnalysis

# print("InsightFace version:", insightface.__version__)

# app = FaceAnalysis(
#     name="buffalo_l",
#     providers=["CPUExecutionProvider"]
# )

# app.prepare(ctx_id=0, det_size=(640, 640))

# print("Model downloaded and ready!")




#_____________________________________For Step 5__________________Test image detection__________________#
import cv2
from app.core.model import InsightFaceModel

# Load model
model = InsightFaceModel()

# Load test image (put a face image path here)
img = cv2.imread("test.jpg")  # <-- add a real image

faces = model.extract_faces(img)

print(f"Faces detected: {len(faces)}")

for i, f in enumerate(faces):
    print(f"\nFace {i+1}")
    print("BBox:", f["bbox"])
    print("Confidence:", f["confidence"])
    print("Embedding shape:", f["embedding"].shape)



#____________________________Verify Database Models__________________________#

# import sqlite3
# conn = sqlite3.connect("data/app.db")
# cur = conn.cursor()
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cur.fetchall())