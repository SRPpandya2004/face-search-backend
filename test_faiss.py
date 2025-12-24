# test_faiss.py

import numpy as np
from app.core.faiss_index import FaissIndex

faiss_index = FaissIndex()

# Fake embeddings (simulate InsightFace output)
embeddings = np.random.rand(3, 512).astype("float32")

metadata = [
    {"photo_id": "img1.jpg", "face_id": 0},
    {"photo_id": "img2.jpg", "face_id": 0},
    {"photo_id": "img3.jpg", "face_id": 1},
]

# Add vectors
start_id = faiss_index.index.ntotal
faiss_index.index.add(embeddings)

for i, meta in enumerate(metadata):
    faiss_index.metadata[str(start_id + i)] = meta

faiss_index.save()

print("✅ FAISS index saved")
print("Total vectors:", faiss_index.index.ntotal)


#__________________________NEw Testiong__________________________#

# --- Search test ---
query = embeddings[0]  # use one embedding already added
D, I = faiss_index.search(query, top_k=3)

print("\nSearch results:")
for rank, (d, idx) in enumerate(zip(D, I), start=1):
    print(f"Rank {rank}: index={idx}, distance={d:.6f}")
