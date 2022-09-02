"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource

USER_BLUEPRINT = Blueprint("user", __name__)
# api = Api(USER_BLUEPRINT)
USER_BLUEPRINT.route("/user", methods=['GET'])(UserResource.get_all)
USER_BLUEPRINT.route("/user", methods=['POST'])(UserResource.post)
USER_BLUEPRINT.route("/user/<string:first_name>", methods=['GET'])(UserResource.get)