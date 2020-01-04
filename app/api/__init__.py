from flask import jsonify
from flask_restplus import Resource, Api

from app.api.models.user import UserDto


user_api = UserDto.api


@user_api.route("/")
class User(Resource):
    @user_api.doc("Get user")
    def get(self):
        return jsonify({"username": "admin", "email": "test@example.com"})


api_final = Api(title="Test api")
api_final.add_namespace(user_api)
