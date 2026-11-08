import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class OCRRequest(Base):
    __tablename__ = "ocr_requests"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    image_hash: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    recognized_text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
