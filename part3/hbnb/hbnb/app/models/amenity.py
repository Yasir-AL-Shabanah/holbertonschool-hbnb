from app.extensions import db
from app.models.base_model import BaseModel


class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
