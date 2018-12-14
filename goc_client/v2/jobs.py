# coding=UTF-8
from gocloud.client import request_utils


class Jobs():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def create_job(self, group_id, job_type, command=None, job_template=None):
        service_url = "/v2/jobs/"
        post_data = {'data': {'group': group_id,
                     'type': job_type, 'command': command}}
        if job_template is not None:
            post_data['files'] = {'data': job_template}
        return self.req_post(url=service_url, **post_data)

    def list_jobs(self, platform, user_id=None, group_id=None):
        service_url = "/v2/%s/jobs/" % platform
        params = {'project': group_id, 'user': user_id}
        return self.req_get(url=service_url, params=params)

    def get_detail(self, platform, job_id):
        service_url = "/v2/%s/jobs/%s/" % (platform, job_id)
        return self.req_get(url=service_url)

    def delete_job(self, platform, job_id):
        service_url = "/v2/%s/jobs/%s/" % (platform, job_id)
        return self.req_delete(url=service_url)
