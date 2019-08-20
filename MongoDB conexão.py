import pymongo
from pymongo import MongoClient


client: MongoClient = pymongo.MongoClient("mongodb+srv://sys:<marcossales21>@cluster-tcc-z3g4b.mongodb.net/test?retryWrites=true&w=majority")
db = client['tcc']
album = db['txt']

album.find_one()
