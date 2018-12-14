# coding=UTF-8
from gocloud.client import request_utils


class Buckets():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch

    def list_buckets(self, platform):
        service_url = "/v2/%s/buckets/" % platform
        return self.req_get(url=service_url)
