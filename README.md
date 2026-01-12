# Face Search Backend 🔍  
**AI-Based Face Search and Photo Retrieval System**

This repository contains the **backend API** for a Face Search application.  
The system allows uploading photos, extracting face embeddings using deep learning, and searching for matching faces using vector similarity.

---

## 🧠 Technologies Used

- **Backend Framework:** FastAPI (Python)
- **Face Detection & Recognition:** InsightFace (buffalo_l model, CPU)
- **Face Embeddings:** ArcFace (512-D vectors)
- **Vector Search:** FAISS (HNSW Index)
- **Database:** SQLite (SQLAlchemy ORM)
- **Image Storage:** Firebase Cloud Storage
- **Server:** Uvicorn

---

## 📂 Folder Structure

# Face Search Backend 🔍  
**AI-Based Face Search and Photo Retrieval System**

This repository contains the **backend API** for a Face Search application.  
The system allows uploading photos, extracting face embeddings using deep learning, and searching for matching faces using vector similarity.

---

## 🧠 Technologies Used

- **Backend Framework:** FastAPI (Python)
- **Face Detection & Recognition:** InsightFace (buffalo_l model, CPU)
- **Face Embeddings:** ArcFace (512-D vectors)
- **Vector Search:** FAISS (HNSW Index)
- **Database:** SQLite (SQLAlchemy ORM)
- **Image Storage:** Firebase Cloud Storage
- **Server:** Uvicorn

---

## 📂 Folder Structure

face-search-backend/
│
├── app/
│ ├── core/
│ │ ├── model.py # InsightFace model wrapper
│ │ ├── faiss_index.py # FAISS index logic
│ │ ├── firebase_storage.py # Firebase upload helper
│ │
│ ├── db/
│ │ ├── database.py # DB engine & session
│ │ ├── models.py # SQLAlchemy models
│ │
│ ├── main.py # FastAPI entry point
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 🚀 Features

- Upload photos (Admin)
- Automatic face detection
- Face embedding extraction (Deep Learning)
- Face similarity search using FAISS
- Threshold-based accurate matching
- REST API with Swagger UI

---

_________________________________________________________________________________________

##
# face-search-backend
It is face classification Project Start on 02-12-2025

# Face Search Backend (FastAPI)

This is the backend API for a Face Search application using:
- FastAPI
- InsightFace (CPU)
- FAISS (CPU)
- SQLite
- Firebase Storage (optional)

## Run locally

1. Create virtual env
   python -m venv env
   env\Scripts\activate

2. Install packages
   pip install -r requirements.txt

3. Run server
   uvicorn app.main:app --reload

## Folder Structure
   As above given

## Features
- Face upload
- Face embedding extraction
- Vector search via FAISS
- User management
- Admin face ingestion


_____________
# Face Search Backend
Python + FastAPI + FAISS + InsightFace (Free Plan)


Technology Stack
Backend

Python 3.10 / 3.11 (Recommended)

FastAPI – REST API framework

InsightFace (buffalo_l) – Face detection & embeddings

ArcFace – Deep learning face recognition model

FAISS (CPU) – Vector similarity search

SQLite – Metadata storage (via SQLAlchemy)

Firebase Cloud Storage – Image storage

Uvicorn – ASGI server

⚠️ GPU is not required. CPU-only setup is used. 


## ⚙️ How to Run Locally (Windows)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SRPpandya2004/face-search-backend.git
cd face-search-backend

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt (First Remove the numy from the requirement and after insataling pip uninstall numpy -y
pip install "numpy<2" this command download requirements.txt)

Important: NumPy Compatibility Fix

InsightFace and ONNX Runtime do NOT yet fully support NumPy 2.x.

👉 You MUST downgrade NumPy:

pip uninstall numpy -y
pip install "numpy<2"


Verify:

python -c "import numpy; print(numpy.__version__)"


Expected output:

1.26.x

4️⃣ Run the Server
uvicorn app.main:app --reload


If successful, you will see:

Uvicorn running on http://127.0.0.1:8000
InsightFace model loaded successfully
FAISS index initialized

📘 API Documentation (Swagger)

Open in browser:

http://127.0.0.1:8000/docs


Available APIs:

/upload-photo → Upload and index faces (Admin)

/search → Search photos by face

/health → Health check


🧪 Example Workflow

Upload multiple photos using /upload-photo

Faces are detected and stored as embeddings

Upload a query image using /search

System returns all matching photos where the person appears


🔐 Security Note

Sensitive data such as:

Firebase credentials

Bucket names

Environment variables


❌ are NOT included in this repository

Use:

.env files

GitHub Secrets

Environment variables

'''

🎓 Academic Use

This project is suitable for:

B.E / B.Tech Final Year Project

AI / ML / Computer Vision demonstrations

Face Recognition research prototypes

🏁 Status

✅ Backend fully functional
✅ Tested with real images
✅ Ready for frontend integration

📌 License

For academic and educational use only.


_______________________________________________________________________________
