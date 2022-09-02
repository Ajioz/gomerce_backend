""" Defines the Product repository """

from models import Product

class ProductRepository:
    """ The repository for the product model """

    @staticmethod
    def get(product_name):
        """ Query a product by product_name """
        return Product.query.filter_by(product_name=product_name).one()
    
    @staticmethod
    def getAll():
        """ Query all products"""
        products = Product.query.all()
        all_products = [product.json for product in products]
        return all_products

    def update(self, product_name, description, price):
        """ Update a product's price """
        product = self.get(product_name)
        product.price = price

        return product.save()

    @staticmethod
    def create(product_name, description, price):
        """ Create a new product """
        product = Product(product_name=product_name, description=description, price=price)
        return product.save()