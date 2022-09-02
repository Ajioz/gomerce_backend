"""
Define the Product model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Product(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Product model """

    __tablename__ = "products"

    product_name = db.Column(db.String(300), primary_key=True)
    description = db.Column(db.Text(), primary_key=True)
    price = db.Column(db.Numeric, nullable=True)

    def __init__(self, product_name, description, price):
        """ Create a new Product """
        self.product_name = product_name
        self.description = description
        self.price = price