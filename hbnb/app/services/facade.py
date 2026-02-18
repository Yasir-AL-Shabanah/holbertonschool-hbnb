class HBnBFacade:
    def __init__(self):
        self.users = []
        self.places = []

    def get_user_by_email(self, email):
        # Mock user for testing login
        if email == "test@test.com":
            from hbnb.app.models.user import User
            return User(id="123", email=email, password="123")
        return None
