import short_url
import hashlib
from config import SHORT_URL_PATTERN


class Url:
    def __init__(self, original_url, lifetime=90):
        self.original_url = original_url
        self.last_part_of_url = original_url.split("/")[-1]
        self.lifetime = lifetime
        self.url_id = self.convert_to_number()
        self.encoded_url = self.encode()
        self.decoded_url = self.decode()

    def convert_to_number(self):
        return int(hashlib.sha256(self.last_part_of_url.encode('utf-8')).hexdigest(), 16) % 10**8

    def encode(self):
        return short_url.encode_url(self.url_id, 6)

    def decode(self):
        return short_url.decode_url(self.encoded_url)

    def create_short_url(self):
        return SHORT_URL_PATTERN.format(self.encode())

    def converted_for_db(self):
        return {"url_id": self.url_id, "original_link": self.original_url, "short_link": self.encoded_url,
                "expire_time": self.lifetime}
