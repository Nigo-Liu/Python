from gocloud.client import request_utils


class Flavors():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get

    def list_flavors(self, flavor_type=None):
        service_url = "/v2/flavors/"
        params = {'type': flavor_type}
        return self.req_get(url=service_url, params=params)

    def get_flavor_by_id(self, flavor_id):
        service_url = "/v2/flavors/%(flavor_id)s/"
        service_url = service_url % ({'flavor_id': flavor_id})
        return self.req_get(url=service_url)
