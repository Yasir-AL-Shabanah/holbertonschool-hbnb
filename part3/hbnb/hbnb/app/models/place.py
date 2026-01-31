from app.extensions import db
from app.models.base_model import BaseModel


class Place(BaseModel):
    __tablename__ = "places"

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    city = db.Column(db.String(128), nullable=True)
    price_per_night = db.Column(db.Float, nullable=True)
    host_id = db.Column(db.String(36), nullable=True)
