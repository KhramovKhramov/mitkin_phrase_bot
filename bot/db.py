from pymongo import MongoClient
import settings

client = MongoClient(settings.MONGO_LINK)
db = client[settings.NAME_DB]

def add_phrase(check):
    db.phrases_collection.update_one({'level': '1'},
                                         {'$push': {'all_phrases': check}})
    return

