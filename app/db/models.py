from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.db.database import Base


# ----------------------------
# Photo table
# ----------------------------
class Photo(Base):
    __tablename__ = "photos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    url = Column(String, nullable=False)
    file_path = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    faces = relationship(
        "Face",
        back_populates="photo",
        cascade="all, delete-orphan"
    )


# ----------------------------
# Face table
# ----------------------------
class Face(Base):
    __tablename__ = "faces"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    photo_id = Column(String, ForeignKey("photos.id"), nullable=False)

    # 🔑 FAISS mapping (THIS FIXES YOUR ORIGINAL ERROR)
    faiss_id = Column(Integer, nullable=False)

    confidence = Column(Float, nullable=True)
    bbox = Column(JSON, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    photo = relationship("Photo", back_populates="faces")
