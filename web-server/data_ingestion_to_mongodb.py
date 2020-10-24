import datetime
import os
from pymongo import MongoClient


class MongoIngestion:
    def __init__(self, connection_str, database_name):
        self.client = MongoClient(connection_str)
        self.database_name = database_name

    def ingest(self, data):
        db = self.client[self.database_name]
        collection = db['visited']
        insert_result = collection.insert_one(data)
        print(self.client)
        print(collection)
        print(insert_result.acknowledged)
        print(insert_result.inserted_id)

