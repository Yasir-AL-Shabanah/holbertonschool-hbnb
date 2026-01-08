from app.persistence.repository import InMemoryRepository
from app.models.review import Review
from app.models.place import Place
from app.models.user import User


class HBnBFacade:
    def __init__(self) -> None:
        # ✅ Repository منفصل لكل كيان
        self.users_repo = InMemoryRepository()
        self.places_repo = InMemoryRepository()
        self.reviews_repo = InMemoryRepository()

    # ---------- Users ----------
    def create_user(self, data: dict) -> User:
        user = User(**data)
        self.users_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User | None:
        return self.users_repo.get(user_id)

    def get_all_users(self):
        return self.users_repo.get_all()

    # ---------- Places ----------
    def create_place(self, data: dict) -> Place:
        place = Place(**data)
        self.places_repo.add(place)
        return place

    def get_place(self, place_id: str) -> Place | None:
        return self.places_repo.get(place_id)

    def get_all_places(self):
        return self.places_repo.get_all()

    # ---------- Reviews (Task 5) ----------
    def create_review(self, data: dict) -> Review:
        review = Review(**data)
        self.reviews_repo.add(review)
        return review

    def get_review(self, review_id: str) -> Review | None:
        return self.reviews_repo.get(review_id)

    def get_all_reviews(self):
        return self.reviews_repo.get_all()

    def update_review(self, review_id: str, data: dict) -> Review | None:
        # يعتمد على وجود update() داخل الموديل
        return self.reviews_repo.update(review_id, data)

    def delete_review(self, review_id: str) -> bool:
        return self.reviews_repo.delete(review_id)

    def get_reviews_by_place(self, place_id: str):
        return [r for r in self.get_all_reviews() if getattr(r, "place_id", None) == place_id]
# Backward-compatible alias (some modules import HbnbFacade)
HbnbFacade = HBnBFacade
