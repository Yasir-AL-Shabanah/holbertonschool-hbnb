from app.extensions import db
from app.models.review import Review
from app.repositories.sqlalchemy_repository import SQLAlchemyRepository


class ReviewRepository(SQLAlchemyRepository):
    def __init__(self, session=None) -> None:
        super().__init__(Review, session=session or db.session)
