from part3 import db
from sqlalchemy import Column, String, Integer, Float
from part3.models.base_model import BaseModel


class Place(BaseModel):
    __tablename__ = "places"

    title = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    price = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
