from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace("user", path='/users', description="Get user info")
    user = api.model(
        "user",
        {
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
        },
    )
