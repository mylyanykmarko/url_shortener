import pymongo
import datetime
from config import MONGO_CONNECTION_STRING, DEFAULT_LIFETIME


class MongoDB:
    def __init__(self):
        self.myclient = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        self.urls_db = self.myclient["urls"]
        self.urls_collection = self.urls_db["short_links"]
        self.urls_collection.create_index("expire_time", expireAfterSeconds=DEFAULT_LIFETIME)

    def add_new_url(self, url):
        timestamp = datetime.datetime.utcnow()
        ready_url = url.converted_for_db()
        ready_url["expire_time"] = timestamp + datetime.timedelta(days=url.lifetime)
        if self.urls_collection.find({"url_id": ready_url["url_id"]}).count() == 0:
            self.urls_collection.insert_one(ready_url)

    def find_original_url(self, hash_id):
        return self.urls_collection.find_one({'short_link': str(hash_id)})


my_db = MongoDB()
