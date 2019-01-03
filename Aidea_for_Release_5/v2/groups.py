import request_utils


class Groups():
    def __init__(self, ip, account, password):
        req = request_utils.Request(ip, account, password)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def create_group(self, name, desc="",
                     sp_admin=None, sp_admin_passwd=None):
        service_url = "/v2/groups/"
        data = {'name': name, 'desc': desc,
                'sp_admin': sp_admin, 'sp_admin_passwd': sp_admin_passwd}
        return self.req_post(url=service_url, data=data)

    def list_groups(self, platform_name):
        service_url = "/v2/%s/projects/" % platform_name 
        return self.req_get(url=service_url)

    def get_detail(self, group_id):
        service_url = "/v2/groups/%(group_id)s/"
        service_url = service_url % ({'group_id': group_id})
        return self.req_get(url=service_url)


 
