from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.auth.decorators import admin_required
from app.extensions import db
from app.models.amenity import Amenity
from app.models.user import User
from app.repositories.amenity_repository import AmenityRepository
from app.repositories.user_repository import UserRepository


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

user_repo = UserRepository()
amenity_repo = AmenityRepository()


@admin_bp.route("/users", methods=["POST"])
@jwt_required()
@admin_required
def create_user_admin():
    payload = request.get_json() or {}

    email = payload.get("email")
    password = payload.get("password")
    first_name = payload.get("first_name")
    last_name = payload.get("last_name")
    is_admin = bool(payload.get("is_admin", False))

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    if user_repo.get_by_email(email):
        return jsonify({"message": "email already in use"}), 400

    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        is_admin=is_admin,
    )
    user.set_password(password)
    user_repo.add(user)

    return jsonify(user.to_dict()), 201


@admin_bp.route("/users/<user_id>", methods=["PUT", "PATCH"])
@jwt_required()
@admin_required
def update_user_admin(user_id: str):
    user = user_repo.get(user_id)
    if user is None:
        return jsonify({"message": "user not found"}), 404

    payload = request.get_json() or {}

    email = payload.get("email")
    password = payload.get("password")

    if email:
        existing = user_repo.get_by_email(email)
        if existing and existing.id != user.id:
            return jsonify({"message": "email already in use"}), 400
        user.email = email

    if "first_name" in payload:
        user.first_name = payload.get("first_name")
    if "last_name" in payload:
        user.last_name = payload.get("last_name")
    if "is_admin" in payload:
        user.is_admin = bool(payload.get("is_admin"))

    if password:
        user.set_password(password)

    db.session.commit()
    return jsonify(user.to_dict()), 200


@admin_bp.route("/amenities", methods=["POST"])
@jwt_required()
@admin_required
def create_amenity_admin():
    payload = request.get_json() or {}
    name = payload.get("name")
    description = payload.get("description")

    if not name:
        return jsonify({"message": "name is required"}), 400

    amenity = Amenity(name=name, description=description)
    amenity_repo.add(amenity)

    return jsonify(amenity.to_dict()), 201


@admin_bp.route("/amenities/<amenity_id>", methods=["PUT", "PATCH"])
@jwt_required()
@admin_required
def update_amenity_admin(amenity_id: str):
    amenity = amenity_repo.get(amenity_id)
    if amenity is None:
        return jsonify({"message": \"amenity not found\"}), 404

    payload = request.get_json() or {}

    if "name" in payload:
        amenity.name = payload.get("name")
    if "description" in payload:
        amenity.description = payload.get("description")

    db.session.commit()
    return jsonify(amenity.to_dict()), 200
