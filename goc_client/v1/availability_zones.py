# coding=UTF-8
from gocloud.client import request_utils


class AvailabilityZones():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_azs(self):
        service_url = "/v1/availability_zones/"
        return self.req_get(url=service_url)

    def get_detail(self, az_id):
        service_url = "/v1/availability_zones/%s/" % az_id
        return self.req_get(url=service_url)

    def create_az(self, name, desc, zone_type='VM'):
        service_url = "/v1/availability_zones/"
        data = {'name': name, 'type': zone_type,
                'desc': desc}
        return self.req_post(url=service_url,
                             data=data)

    def delete_az(self, az_id):
        service_url = "/v1/availability_zones/%s/" % az_id
        return self.req_delete(url=service_url)

    def update_az(self, az_id, hosts):
        service_url = "/v1/availability_zones/%s/" % az_id
        data = {'hosts': hosts}
        return self.req_patch(url=service_url,
                              data=data)
