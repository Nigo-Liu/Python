# coding=UTF-8
from gocloud.client import request_utils


class Version():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def get(self):
        service_url = "/v1/version/"
        return self.req_get(url=service_url)
