from src.configs.model import Base

from datetime import datetime
from sqlalchemy import String, Boolean, Integer, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column



class Student(Base):
    __tablename__ = "students"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name : Mapped[str] = mapped_column(String)
    last_name : Mapped[str] = mapped_column(String)
    age : Mapped[int] = mapped_column(Integer)
    ph_no : Mapped[str] = mapped_column(String)
    profile_image : Mapped[str] = mapped_column(String)

    email : Mapped[str] = mapped_column(String)
    password : Mapped[str] = mapped_column(String)

    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    active_at : Mapped[bool] = mapped_column(Boolean, default=True)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())