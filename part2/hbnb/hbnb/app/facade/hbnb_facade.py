from app.persistence.repository import InMemoryRepository
from app.models.review import Review
from app.models.place import Place
from app.models.user import User


class HBnBFacade:
    def __init__(self) -> None:
        
        self.repo = InMemoryRepository()

    # ---------- Users ----------
    def get_user(self, user_id: str):
        return self.repo.get(User, user_id)

    # ---------- Places ----------
    def get_place(self, place_id: str):
        return self.repo.get(Place, place_id)

    # ---------- Reviews (Task 5) ----------
    def create_review(self, data: dict):
      
        review = Review(**data)
        self.repo.add(review)
        return review

    def get_review(self, review_id: str):
        return self.repo.get(Review, review_id)

    def update_review(self, review_id: str, data: dict):
        review = self.get_review(review_id)
        if not review:
            return None

        
        for k, v in data.items():
            setattr(review, k, v)

        
        if hasattr(review, "save"):
            review.save()

        
        if hasattr(self.repo, "update"):
            self.repo.update(review)

        return review

    def delete_review(self, review_id: str) -> bool:
        review = self.get_review(review_id)
        if not review:
            return False

       
        self.repo.delete(Review, review_id)
        return True

    def get_reviews_by_place(self, place_id: str):
       
        reviews = self.repo.get_all(Review)
        return [r for r in reviews if getattr(r, "place_id", None) == place_id]
