from app.models.base import BaseModel
from app import db
from sqlalchemy.orm import relationship

class Place(BaseModel, db.Model):
    __tablename__ = 'places'
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    price = db.Column(db.Integer, nullable=False, default=0)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    owner_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)

    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
