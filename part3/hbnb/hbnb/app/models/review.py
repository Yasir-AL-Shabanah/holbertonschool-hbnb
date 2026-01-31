from part3 import db
from sqlalchemy import Column, String, Integer
from part3.models.base_model import BaseModel


class Review(BaseModel):
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)
