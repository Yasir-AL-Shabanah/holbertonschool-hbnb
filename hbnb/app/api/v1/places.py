from flask_restx import Namespace, Resource

api = Namespace('places', description='Place operations')

@api.route('/')
class PlaceList(Resource):
    def get(self):
        # Return mock data to show in Frontend
        return [
            {
                "id": "1",
                "title": "Cozy Cottage",
                "price": 120,
                "description": "A beautiful cottage in the woods.",
                "city_id": "Paris",
                "owner_id": "User1"
            },
            {
                "id": "2",
                "title": "Modern Apartment",
                "price": 250,
                "description": "Luxury apartment in the city center.",
                "city_id": "New York",
                "owner_id": "User2"
            }
        ]

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        return {
            "id": place_id,
            "title": "Cozy Cottage",
            "price": 120,
            "description": "A beautiful cottage in the woods.",
            "city_id": "Paris",
            "owner_id": "User1"
        }
