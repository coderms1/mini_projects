#03_mongosh.py

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["test_db"]
collection = db["messages"]

collection.insert_one({"from": "Sim", "message": "Collection connected using python on vs code"})

for doc in collection.find():
  print(doc)
