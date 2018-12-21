import falcon
from request_parser import RequestParser
from responder import Responder


class IntentHandler(object):
    def on_post(self, req, resp):
        req = RequestParser(req)
        resp = Responder(resp, req.response)


app = falcon.API(media_type=falcon.MEDIA_JSON)
app.add_route('/', IntentHandler())