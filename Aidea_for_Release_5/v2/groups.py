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

    def list_groups(self):
        service_url = "/v2/groups/"
        return self.req_get(url=service_url)

    def get_detail(self, group_id):
        service_url = "/v2/groups/%(group_id)s/"
        service_url = service_url % ({'group_id': group_id})
        return self.req_get(url=service_url)

    def get_solutions(self, group_id):
        service_url = "/v2/groups/%(group_id)s/solutions/"
        service_url = service_url % ({'group_id': group_id})
        return self.req_get(url=service_url)

    def update_solutions(self, group_id, solutions):
        service_url = "/v2/groups/%(group_id)s/solutions/"
        service_url = service_url % ({'group_id': group_id})
        data = {'solutions': solutions}
        return self.req_put(url=service_url, data=data)

    def add_solution(self, group_id, solution_id):
        service_url = "/v2/groups/%(group_id)s/solutions/%(solution_id)s/"
        service_url = service_url % ({'group_id': group_id,
                                      'solution_id': solution_id})
        return self.req_put(url=service_url)

    def remove_solution(self, group_id, solution_id):
        service_url = "/v2/groups/%(group_id)s/solutions/%(solution_id)s/"
        service_url = service_url % ({'group_id': group_id,
                                      'solution_id': solution_id})
        return self.req_delete(url=service_url)

    def update_quota(self, group_id, quotas):
        service_url = "/v2/groups/%(group_id)s/quota/"
        service_url = service_url % ({'group_id': group_id})
        return self.req_patch(url=service_url,
                              data=quotas)

    def get_assets_reports(self, group_id=None,
                           begin_time=None, end_time=None):
        service_url = "/v2/groups/reports/assets/"
        params = {'group_id': group_id}
        if begin_time:
            params.update({'begin_time': begin_time})
        if end_time:
            params.update({'end_time': end_time})
        return self.req_get(url=service_url, params=params)

    def get_statistics_reports(self, group_id=None,
                               begin_time=None, end_time=None):
        service_url = "/v2/groups/reports/statistics/"
        params = {'group_id': group_id}
        if begin_time:
            params.update({'begin_time': begin_time})
        if end_time:
            params.update({'end_time': end_time})
        return self.req_get(url=service_url, params=params)
