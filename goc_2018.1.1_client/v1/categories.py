from gocloud.client import request_utils


class Categories():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch

    def list_categories(self):
        service_url = "/v1/categories/"
        return self.req_get(url=service_url)
