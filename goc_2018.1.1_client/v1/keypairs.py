from gocloud.client import request_utils


class Keypairs():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete

    def list_keypairs(self):
        service_url = "/v1/keypairs/"
        return self.req_get(url=service_url)

    def get_detail(self, name):
        service_url = "/v1/keypairs/%s/" % name
        return self.req_get(url=service_url)

    def delete_keypair(self, name):
        service_url = "/v1/keypairs/%s/" % name
        return self.req_delete(url=service_url)

    def create_keypair(self, name, public_key=None):
        service_url = "/v1/keypairs/"
        data = {'name': name, 'public_key': public_key}
        return self.req_post(url=service_url,
                             data=data)
