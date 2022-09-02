"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from utils import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(first_name):
        """ Return an user key information based on his name """
        user = UserRepository.get(first_name=first_name)
        return jsonify({"data": user.json})
    
    @staticmethod
    @swag_from("../swagger/user/GET_ALL.yml")
    def get_all():
        """ Return an user key information based on his name """
        users = UserRepository.getAll()
        return jsonify({"data": users})

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True, help="The first_name of the user."),
        Argument("last_name", location="json", required=True, help="The last_name of the user."),
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/POST.yml")
    def post(last_name, first_name, age):
        """ Create an user based on the sent information """
        user = UserRepository.create(
            last_name=last_name, first_name=first_name, age=age
        )
        return jsonify({"data": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(last_name, first_name, age):
        """ Update an user based on the sent information """
        repository = UserRepository()
        user = repository.update(last_name=last_name, first_name=first_name, age=age)
        return jsonify({"data": user.json})