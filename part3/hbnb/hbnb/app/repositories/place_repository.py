from app.extensions import db
from app.models.place import Place
from app.repositories.sqlalchemy_repository import SQLAlchemyRepository


class PlaceRepository(SQLAlchemyRepository):
    def __init__(self, session=None) -> None:
        super().__init__(Place, session=session or db.session)
