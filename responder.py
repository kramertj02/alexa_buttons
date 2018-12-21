class Responder(object):
    def __init__(self, resp, request_response):
        self.resp = resp
        self.rr = request_response
        self.rr['version'] = '1.0'
        self.resp.status = 200
        self.resp.content_type = 'application/json'
        self.resp.content = self.rr
