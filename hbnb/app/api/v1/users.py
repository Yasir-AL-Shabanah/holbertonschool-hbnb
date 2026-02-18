from flask_restx import Namespace, Resource

api = Namespace('users', description='User operations')

@api.route('/')
class UserList(Resource):
    def get(self):
        return []
