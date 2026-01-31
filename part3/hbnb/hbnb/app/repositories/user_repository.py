from typing import Optional

from app.extensions import db
from app.models.user import User
from app.repositories.sqlalchemy_repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    def __init__(self, session=None) -> None:
        super().__init__(User, session=session or db.session)

    def get_by_email(self, email: str) -> Optional[User]:
        return User.query.filter_by(email=email).one_or_none()
