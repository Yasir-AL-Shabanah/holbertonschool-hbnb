from flask_restx import Namespace, Resource

api = Namespace('amenities', description='Amenity operations')

@api.route('/')
class AmenityList(Resource):
    def get(self):
        return []
