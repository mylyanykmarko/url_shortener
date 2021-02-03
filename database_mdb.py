import pymongo
import datetime
from config import MONGO_CONNECTION_STRING


class MongoDB:
    def __init__(self):
        self.myclient = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        self.urls_db = self.myclient["urls"]
        self.urls_collection = self.urls_db["short_links"]
        self.urls_collection.create_index("expire_time", expireAfterSeconds=7776000)

    def add_new_url(self, url):
        timestamp = datetime.datetime.utcnow()
        ready_url = url.converted_for_db()
        ready_url["expire_time"] = timestamp + datetime.timedelta(minutes=url.lifetime)
        self.urls_collection.insert_one(ready_url)
        # self.urls_db.command('collMod', 'short_links', index={'name': 'index_name', 'expireAfterSeconds': url.lifetime})

    def find_original_url(self, hash_id):
        pass


my_db = MongoDB()
