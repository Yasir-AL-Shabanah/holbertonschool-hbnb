from flask_restx import Namespace, Resource, fields
from app.facade.hbnb_facade import HbnbFacade

api = Namespace('amenities', description='Amenity management endpoints')
facade = HbnbFacade()

amenity_model = api.model('Amenity', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
    'description': fields.String(required=False)
})


@api.route('/')
class AmenityList(Resource):

    @api.marshal_list_with(amenity_model)
    def get(self):
        return facade.get_all_amenities()

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        return facade.create_amenity(api.payload), 201


@api.route('/<string:amenity_id>')
@api.response(404, "Amenity not found")
class AmenityResource(Resource):

    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    def put(self, amenity_id):
        return facade.update_amenity(amenity_id, api.payload)
