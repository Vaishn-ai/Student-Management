from src.configs.model import Base

from datetime import datetime
from sqlalchemy import String, Integer, Boolean, func, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Batch(Base):
    __tablename__ = "batches"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String)
    starting_date : Mapped[str] = mapped_column(String)
    ending_date : Mapped[str] = mapped_column(String)
    start_time : Mapped[str] = mapped_column(String)
    end_time : Mapped[str] = mapped_column(String)

    course_name : Mapped[str] = mapped_column(ForeignKey("courses.name"))

    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    active_at : Mapped[bool] = mapped_column(Boolean, default=True)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

