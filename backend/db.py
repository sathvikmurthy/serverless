from pymongo import MongoClient
from bson.json_util import dumps, loads
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
client = MongoClient(MONGO_URI)
db = client["serverless"]
collection = db["functions"]

def init_db():
    collection.create_index("name", unique=True)

def save_function(fun):
    collection.replace_one(
        {"name": fun.name},
        {"name": fun.name, "code": fun.code, "language": fun.language, "timeout": fun.timeout},
        upsert=True
    )

def get_function(name):
    doc = collection.find_one({"name": name})
    if doc:
        return {"name": doc['name'], "code": doc['code'], "language": doc['language'], "timeout": doc['timeout']}
    return None