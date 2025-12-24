# app/core/faiss_index.py

import faiss
import os
import json
import numpy as np
import logging

logger = logging.getLogger(__name__)

class FaissIndex:
    def __init__(
        self,
        dim=512,
        index_path="data/faiss/index.faiss",
        meta_path="data/faiss/metadata.json",
        ef_search=64
    ):
        self.dim = dim
        self.index_path = index_path
        self.meta_path = meta_path

        os.makedirs(os.path.dirname(index_path), exist_ok=True)

        # ---------- Load or create index ----------
        if os.path.exists(index_path) and os.path.getsize(index_path) > 0:
            logger.info("🔁 Loading existing FAISS index...")
            self.index = faiss.read_index(index_path)
        else:
            logger.info("🆕 Creating new FAISS HNSW index...")
            self.index = faiss.IndexHNSWFlat(dim, 32)
            self.index.hnsw.efConstruction = 200
            self.index.hnsw.efSearch = ef_search

        # ---------- Load or create metadata ----------
        if os.path.exists(meta_path) and os.path.getsize(meta_path) > 0:
            with open(meta_path, "r") as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {}

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "w") as f:
            json.dump(self.metadata, f)

#___Added For testing___#

    def search(self, query_embedding, top_k=5):
        """
        Search nearest neighbors for a single embedding.
        query_embedding: np.ndarray of shape (512,)
        Returns: distances, indices
        """
        if self.index.ntotal == 0:
            raise ValueError("FAISS index is empty")

        # Ensure correct shape
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)

        distances, indices = self.index.search(query_embedding, top_k)
        return distances[0], indices[0]


    def add(self, embedding: np.ndarray, meta: dict):
        if embedding.ndim == 1:
            embedding = embedding.reshape(1, -1)

        idx = self.index.ntotal
        self.index.add(embedding.astype(np.float32))
        self.metadata[str(idx)] = meta
        self.save()
        return idx

    def get_metadata(self, idx: int):
        return self.metadata.get(str(idx))

