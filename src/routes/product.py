"""
Defines the blueprint for the product
"""
from flask import Blueprint
from flask_restful import Api

from resources import ProductResource

PRODUCT_BLUEPRINT = Blueprint("product", __name__)

PRODUCT_BLUEPRINT.route("/product", methods=['GET'])(ProductResource.get_all)
PRODUCT_BLUEPRINT.route("/product", methods=['POST'])(ProductResource.post)
PRODUCT_BLUEPRINT.route("/product/<string:name>", methods=['GET'])(ProductResource.get)