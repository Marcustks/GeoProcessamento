import pymongo
from pprint import pprint


client = pymongo.MongoClient(
    "mongodb+srv://sys:marcossales21@cluster-tcc-z3g4b.mongodb.net/test?retryWrites=true&w=majority")
db = client.tcc
collection = db.txt


cursor = collection.find({})
for document in cursor:
    pprint(document)
