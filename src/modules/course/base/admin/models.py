from src.configs.model import Base

from datetime import datetime
from sqlalchemy import String, Boolean, Integer, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Course(Base):
    __tablename__ = "courses"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String)
    description : Mapped[str] = mapped_column(String)
    overview : Mapped[str] = mapped_column(String)
    document : Mapped[str] = mapped_column(String)

    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    active_at : Mapped[bool] = mapped_column(Boolean, default = True)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())