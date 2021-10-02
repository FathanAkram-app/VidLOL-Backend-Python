
import pymongo
from pprint import pprint


class Database:
    
    def __init__(self):
        pass
    def connectDB():
        client = pymongo.MongoClient("mongodb://%s:%s"%("localhost","27017"))
        db = client.vidlol
        print("connected to %s database"%db.name)
        return db


    