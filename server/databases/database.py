from pymongo import MongoClient

client = MongoClient()

db = client.my_database
recognized_text_db = db.recognized_text_db

def find_by_id(_id):
    return recognized_text_db.find_one({"task_id": _id})

def added_to_queue(_id):
    recognized_text_db.insert_one({"task_id": _id,
                                   "recognized_text": "",
                                   "status": "Added to queue"})


