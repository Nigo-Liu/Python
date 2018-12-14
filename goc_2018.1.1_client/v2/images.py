from gocloud.client import request_utils


class Images():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_images(self, group_id=None, solution_id=None):
        service_url = "/v2/images/"
        if group_id is not None:
            service_url = service_url + ('?group=%d' % int(group_id))
            if solution_id is not None:
                service_url = service_url + ('&solution=%d' % int(solution_id))
        elif solution_id is not None:
            service_url = service_url + ('?solution=%d' % int(solution_id))
        return self.req_get(url=service_url)

    def get_image_detail(self, image_id):
        service_url = "/v2/images/%(image_id)s/"
        service_url = service_url % {'image_id': image_id}
        return self.req_get(url=service_url)

    def create_image(self,
                     name,
                     platform,
                     group_id=None,
                     desc=""):
        service_url = "/v2/images/"
        data = {'name': name,
                'desc': desc,
                'platform': platform}
        if group_id:
            data['group'] = str(group_id)
        return self.req_post(url=service_url,
                             data=data)

    def delete_image(self, image_id):
        service_url = "/v2/images/%(image_id)s/"
        service_url = service_url % ({'image_id': image_id})
        return self.req_delete(url=service_url)

    def upload_image(self, image_id, image_file):
        service_url = "/v2/images/%(image_id)s/file/"
        service_url = service_url % ({'image_id': image_id})
        return self.req_put(url=service_url,
                            files={'data': image_file})

    def save_image(self, server_id, name, group_id,
                   platform='Linux', desc=""):
        service_url = "/v2/images/%(server_id)s/save/"
        service_url = service_url % ({'server_id': server_id})
        data = {'name': name,
                'group': group_id,
                'platform': platform,
                'desc': desc}
        return self.req_put(url=service_url,
                            data=data)
