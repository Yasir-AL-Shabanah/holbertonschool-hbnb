from app.extensions import db
from app.models.base_model import BaseModel


class Review(BaseModel):
    __tablename__ = "reviews"

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.String(36), nullable=False)
    place_id = db.Column(db.String(36), nullable=False)
