from app.extensions import db, bcrypt
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(128), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def set_password(self, raw_password: str) -> None:
        self.password_hash = bcrypt.generate_password_hash(raw_password).decode("utf-8")

    def check_password(self, raw_password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, raw_password)
