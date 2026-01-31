from part3 import db
from sqlalchemy import Column, String
from part3.models.base_model import BaseModel


class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False, unique=True)
