from gocloud.client import request_utils


class Servers():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch

    def list_servers(self, site_id=None, image_id=None,
                     group_id=None, all_users=0):
        service_url = "/v1/servers/"
        params = {'site_id': site_id, 'image_id': image_id,
                  'tenant': group_id, 'all_users': all_users}
        return self.req_get(url=service_url,
                            params=params)

    def get_detail(self, server_id):
        service_url = "/v1/servers/%d/"
        service_url = service_url % (server_id)
        return self.req_get(url=service_url)

    def get_reports(self, begin_time=None, end_time=None,
                    group_id=None, user_id=None, site_id=None):
        service_url = "/v1/servers/reports/"
        params = {'group_id': group_id, 'user_id': user_id, 'site_id': site_id}
        if begin_time:
            params.update({'begin_time': begin_time})
        if end_time:
            params.update({'end_time': end_time})
        return self.req_get(url=service_url,
                            params=params)
