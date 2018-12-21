import json

from requests import *


class RequestParser(object):
    def __init__(self, req):
        self.req = req
        self.body = req.stream.read()
        self.json = json.loads(self.body.decode('utf-8'))
        self.request_type = json['type']
        self.response = REQUESTS[self.request_info](self.json)
