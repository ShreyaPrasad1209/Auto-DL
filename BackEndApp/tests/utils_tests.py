# User class objects for unit testing of User class

from authv1.models import User
import mongomock


class TestUser:
    def user_test(self):
        collection = mongomock.MongoClient().db.collection
        user = User(username="test_user", password="test_pw")
        user.attributes = {
            "first_name": "test",
            "last_name": "user",
            "email": "test_user@gmail.com",
        }
        user.collection = collection
        return user

    def user_noEmail(self):
        collection = mongomock.MongoClient().db.collection
        user = User(username="test_user", password="test_pw")
        user.attributes = {
            "first_name": "test",
            "last_name": "user",
        }
        user.collection = collection
        return user

    def user_invalidEmail(self):
        collection = mongomock.MongoClient().db.collection
        user = User(username="test_user", password="test_pw")
        user.attributes = {
            "first_name": "test",
            "last_name": "user",
            "email": "test_user@.com",
        }
        user.collection = collection
        return user
