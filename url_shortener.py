import datetime
import short_url
import hashlib

SHORT_URL_PATTERN = "http://srt.mm/{}"
url = "how-to-make-unique-short-url-with-python"
num = int(hashlib.sha256(url.encode('utf-8')).hexdigest(), 16) % 10**8
print(url)


class Url:
    def __init__(self, original_url, lifetime=90):
        self.original_url = original_url
        self.lifetime = lifetime
        self.url_id = self.convert_to_number()

    def convert_to_number(self):
        return int(hashlib.sha256(self.original_url.encode('utf-8')).hexdigest(), 16) % 10**8

    def encode(self):
        return short_url.encode_url(self.url_id, 6)

    def decode(self):
        return short_url.decode_url(self.original_url)

    def create_short_url(self):
        return SHORT_URL_PATTERN.format(self.encode())


new = Url(url, 90)

short = new.create_short_url()
print(short)
