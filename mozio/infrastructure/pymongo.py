from django.conf import settings

from pymongo import MongoClient


def get_db():
    mongo = settings.DATABASES['default']['CLIENT']

    client = MongoClient(
        mongo['host'],
        port=mongo['port'],
        username=mongo['username'],
        password=mongo['password'],
        authSource=mongo['authSource'],
        authMechanism=mongo['authMechanism'],
    )

    return client[mongo['authSource']]


def get_collection(collection_name):
    return get_db()[collection_name]
