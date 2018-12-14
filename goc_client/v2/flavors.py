# coding=UTF-8
from gocloud.client import request_utils


class Flavors():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get

    def list_flavors(self, platform_name):
        service_url = "/v2/%s/flavors/" % platform_name
        return self.req_get(url=service_url)

    def get_flavor_by_id(self, platform_name, flavor_id):
        service_url = "/v2/%s/flavors/%s/" % (platform_name, flavor_id)
        return self.req_get(url=service_url)
