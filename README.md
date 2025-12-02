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
(Insert tree here)

## Features
- Face upload
- Face embedding extraction
- Vector search via FAISS
- User management
- Admin face ingestion
