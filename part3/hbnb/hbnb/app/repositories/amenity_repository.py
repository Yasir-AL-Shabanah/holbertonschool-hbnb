from app.extensions import db
from app.models.amenity import Amenity
from app.repositories.sqlalchemy_repository import SQLAlchemyRepository


class AmenityRepository(SQLAlchemyRepository):
    def __init__(self, session=None) -> None:
        super().__init__(Amenity, session=session or db.session)
