from gocloud.client import request_utils


class Flavors():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get

    def get_flavor_by_id(self, flavor_id):
        service_url = "/v1/flavors/%(flavor_id)s/"
        service_url = service_url % ({'flavor_id': flavor_id})
        return self.req_get(url=service_url)
