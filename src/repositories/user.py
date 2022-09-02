""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(first_name):
        """ Query a user by first name """
        return User.query.filter_by(first_name=first_name).one()
    
    @staticmethod
    def getAll():
        """ Query all users"""
        users = User.query.all()
        all_users = [user.json for user in users]
        return all_users

    def update(self, last_name, first_name, age):
        """ Update a user's age """
        user = self.get(last_name, first_name)
        user.age = age

        return user.save()

    @staticmethod
    def create(last_name, first_name, age):
        """ Create a new user """
        user = User(last_name=last_name, first_name=first_name, age=age)
        print("Heteuweeiuuwe")
        return user.save()