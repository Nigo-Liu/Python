import request_utils


class Flavors():
    def __init__(self, ip):
        req = request_utils.Request(ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def create_flavors(self, flavor_name, flavor_type, desc="", cpu=None, memory=None, disk=None, gpu=None, metadata=None):
        service_url = "/v2/flavors/"
        post_data = {'data': {'name': flavor_name, 'type': flavor_type, 'desc': desc, 'cpu': cpu, 'memory': memory, 'disk': disk, 'gpu': gpu, 'metadata': metadata}}
        return self.req_post(url=service_url, **post_data)

    def list_flavors(self, flavor_type=None):
        service_url = "/v2/flavors/"
        params = {'type': flavor_type}
        return self.req_get(url=service_url, params=params)

    def get_flavor_by_id(self, flavor_id):
        service_url = "/v2/flavors/%(flavor_id)s/"
        service_url = service_url % ({'flavor_id': flavor_id})
        return self.req_get(url=service_url)
