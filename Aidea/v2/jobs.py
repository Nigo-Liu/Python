import request_utils


class Jobs():
    def __init__(self, ip):
        req = request_utils.Request(ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def create_job(self, group_id, job_type, job_image, job_flavor, job_name, schedule=None, volumes=None, az=None, runs=None, command=None, job_template=None):
        service_url = "/v2/jobs/"
        post_data = {'data': {'project': group_id,
                     'type': job_type, 'image': job_image, 'flavor': job_flavor, 'name': job_name, 'schedule':schedule, 'volumes': volumes, 'availability_zone': az, 'runs': runs, 'command': command}}
        if job_template is not None:
            post_data['files'] = {'data': job_template}
        return self.req_post(url=service_url, **post_data)
                    
    def submit_job(self, job_id, action):
        service_url = "/v2/jobs/"
        post_data = {'data': {'job_id': job_id, 'action': action}}
        return self.req_post(url=service_url, **post_data)

    def update_job(self, group_id, job_type, job_image, job_flavor, job_name, schedule=None, volumes=None, az=None, runs=None, command=None, job_template=None):
        service_url = "/v2/jobs" 
        post_data = {'data': {'project': group_id,
                     'type': job_type, 'image': job_image, 'flavor': job_flavor, 'name': job_name, 'schedule':schedule, 'volumes': volumes, 'availability_zone': az, 'runs': runs, 'command': command}}
        return self.req_patch(url=service_url, **post_data)

    def get_runs(self, job_id):
        service_url = "/v2/jobs/%s" % job_id
        return self.req_get(url=service_url)

    def get_runs_detail(self, job_id, run_id):
        service_url = "/v2/jobs/"
        params = {'job_id': job_id, 'run_id': run_id}
        return self.req_get(url=service_url, params=params)
        
    def list_jobs(self, group_id=None, job_type=None):
        service_url = "/v2/jobs/"
        params = {'project': group_id, 'type': job_type}
        return self.req_get(url=service_url, params=params)

    def get_job_detail(self, job_id):
        service_url = "/v2/jobs/%s/" % job_id
        return self.req_get(url=service_url)

    def delete_job(self, job_id):
        service_url = "/v2/jobs/%s/" % job_id
        return self.req_delete(url=service_url)