from flask_restx import Namespace, Resource, fields
from app.facade.hbnb_facade import HbnbFacade

api = Namespace('places', description='Place management endpoints')
facade = HbnbFacade()

owner_model = api.model('Owner', {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String
})

amenity_brief = api.model('AmenityBrief', {
    'id': fields.String,
    'name': fields.String
})

place_model = api.model('Place', {
    'id': fields.String(readonly=True),
    'title': fields.String(required=True),
    'description': fields.String,
    'price': fields.Float(required=True),
    'latitude': fields.Float,
    'longitude': fields.Float,
    'owner': fields.Nested(owner_model),
    'amenities': fields.List(fields.Nested(amenity_brief))
})


@api.route('/')
class PlaceList(Resource):

    @api.marshal_list_with(place_model)
    def get(self):
        return facade.get_all_places()

    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    def post(self):
        data = api.payload

        price = data.get("price")
        if price is not None and price < 0:
            api.abort(400, "Invalid price value")

        return facade.create_place(data), 201


@api.route('/<string:place_id>')
@api.response(404, "Place not found")
class PlaceResource(Resource):

    @api.marshal_with(place_model)
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        return place

    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, place_id):
        return facade.update_place(place_id, api.payload)
