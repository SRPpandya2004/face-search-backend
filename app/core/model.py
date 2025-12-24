# app/core/model.py

import logging
import numpy as np
import cv2
from typing import List, Dict

from insightface.app import FaceAnalysis

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class InsightFaceModel:
    """
    CPU-only InsightFace model loader and embedding extractor
    """

    def __init__(
        self,
        model_name: str = "buffalo_l",
        det_size: tuple = (640, 640)
    ):
        logger.info("Initializing InsightFace model (CPU only)...")

        self.app = FaceAnalysis(
            name=model_name,
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=0,              # MUST be 0 for CPU
            det_size=det_size
        )

        logger.info("InsightFace model loaded successfully")

    @staticmethod
    def l2_normalize(vec: np.ndarray) -> np.ndarray:
        """
        L2 normalize embedding vector
        """
        norm = np.linalg.norm(vec)
        if norm == 0:
            return vec
        return vec / norm

    def extract_faces(self, image_bgr: np.ndarray) -> List[Dict]:
        """
        Detect faces and extract embeddings

        Args:
            image_bgr (np.ndarray): OpenCV BGR image

        Returns:
            List of dicts:
            [
                {
                    "bbox": [x1, y1, x2, y2],
                    "embedding": np.ndarray (512,),
                    "confidence": float
                }
            ]
        """

        if image_bgr is None:
            raise ValueError("Input image is None")

        if len(image_bgr.shape) != 3:
            raise ValueError("Invalid image shape")

        faces = self.app.get(image_bgr)

        if not faces:
            logger.warning("No face detected")
            return []

        results = []

        for face in faces:
            emb = face.embedding
            emb = self.l2_normalize(emb)

            bbox = face.bbox.astype(int).tolist()

            results.append({
                "bbox": bbox,
                "embedding": emb,
                "confidence": float(face.det_score)
            })

        logger.info(f"Detected {len(results)} face(s)")
        return results
