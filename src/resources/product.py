"""
Define the REST verbs relative to the products
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import ProductRepository
from utils import parse_params


class ProductResource(Resource):
    """ Verbs relative to the products """

    @staticmethod
    @swag_from("../swagger/product/GET.yml")
    def get(product_name):
        """ Return an product key information based on it product_name """
        product = ProductRepository.get(product_name=product_name)
        return jsonify({"data": product.json})
    
    @staticmethod
    @swag_from("../swagger/product/GET_ALL.yml")
    def get_all():
        """ Return all product paginated and searched"""
        products = ProductRepository.getAll()
        return jsonify({"data": products})

    @staticmethod
    @parse_params(
        Argument("product_name", location="json", required=True, help="The product_name of the product."),
        Argument("description", location="json", required=True, help="The description of the product."),
        Argument("price", location="json", required=True, help="The price of the product.")
    )
    @swag_from("../swagger/product/POST.yml")
    def post(product_name, description, price):
        """ Create an product based on the sent information """
        product = ProductRepository.create(
            product_name=product_name, description=description, price=price
        )
        return jsonify({"data": product.json})

    @staticmethod
    @parse_params(
        Argument("price", location="json", required=True, help="The price of the product.")
    )
    @swag_from("../swagger/product/PUT.yml")
    def put(product_name, description, price):
        """ Update an product based on the sent information """
        repository = ProductRepository()
        product = repository.update(product_name=product_name, description=description, price=price)
        return jsonify({"data": product.json})