from typing import Collection
from pymongo import MongoClient

client = MongoClient()

db = client.my_database
recognized_text_db = db.recognized_text_db


def add_to_db(_id, data):
    filter_by_id = {"task_id": _id}
    update = {"$set": {"recognized_text": str(data),
                                   "status": "Processed"}}
    recognized_text_db.update_one(filter_by_id, update)

def sent_to_ocr_engine(_id):
    filter_by_id = {"task_id": _id}
    update = {"$set": {"status": "Under Processing"}}
    recognized_text_db.update_one(filter_by_id, update)



