from src.configs.model import Base

from datetime import datetime
from sqlalchemy import String, Integer, Boolean, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Enrollment(Base):

    __tablename__ = "enrollments"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id : Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable = False)
    batch_id : Mapped[int] = mapped_column(ForeignKey("batches.id"), nullable=False)
    student_id : Mapped[int] = mapped_column(ForeignKey("students.id"), nullable = False)

    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    active_at : Mapped[bool] = mapped_column(Boolean, default=True)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


