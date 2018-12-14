# coding=UTF-8
from gocloud.client import request_utils


class Images():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_images(self, platform_name, group_id=None, solution_id=None):
        service_url = "/v2/%s/images/" % platform_name
        params = {'project': group_id, 'solution': solution_id}
        return self.req_get(url=service_url, params=params)

    def get_image_detail(self, platform_name, image_id):
        service_url = "/v2/%(platform_name)s/images/%(image_id)s/"
        service_url = service_url % {'image_id': image_id,
                                     'platform_name': platform_name}
        return self.req_get(url=service_url)

    def create_image(self,
                     platform_name,
                     name,
                     os,
                     os_version,
                     group_id=None,
                     desc=""):
        service_url = "/v2/%s/images/" % platform_name
        data = {'name': name, 'desc': desc, 'os': os,
                'os_version': os_version, 'project': group_id}
        return self.req_post(url=service_url,
                             data=data)

    def delete_image(self, platform_name, image_id):
        service_url = "/v2/%s/images/%(image_id)s/"
        service_url = service_url % {'image_id': image_id,
                                     'platform_name': platform_name}
        return self.req_delete(url=service_url)

    def upload_image(self, platform_name, image_id, image_file):
        service_url = "/v2/%s/images/%(image_id)s/file/"
        service_url = service_url % {'image_id': image_id,
                                     'platform_name': platform_name}
        return self.req_put(url=service_url,
                            files={'data': image_file})

    def save_image(self, platform_name, server_id, name, group_id,
                   os='Linux', desc=""):
        service_url = "/v2/%s/images/%(server_id)s/save/"
        service_url = service_url % {'server_id': server_id,
                                     'platform_name': platform_name}
        data = {'name': name,
                'group': group_id,
                'os': os,
                'desc': desc}
        return self.req_put(url=service_url,
                            data=data)
