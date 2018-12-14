# coding=UTF-8
from gocloud.client import request_utils


class Solutions():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_solutions(self):
        service_url = "/v1/solutions/"
        return self.req_get(url=service_url)

    def create_solution(self, category_id, name, desc):
        service_url = "/v1/solutions/"
        data = {'category': category_id, 'name': name, 'desc': desc}
        return self.req_post(url=service_url,
                             data=data)

    def upload_package(self, solution_id, package):
        service_url = "/v1/solutions/%(solution_id)s/file/"
        service_url = service_url % ({'solution_id': solution_id})
        return self.req_put(url=service_url,
                            files={'data': package})

    def delete_solution(self, solution_id):
        service_url = "/v1/solutions/%(solution_id)s/"
        service_url = service_url % ({'solution_id': solution_id})
        return self.req_delete(url=service_url)

    def get_solution_detail(self, solution_id):
        service_url = "/v1/solutions/%s/"
        service_url = service_url % solution_id
        return self.req_get(url=service_url)

    def check_solution_state(self, solution_id):
        service_url = "/v1/solutions/%(solution_id)s/actions/check/"
        service_url = service_url % ({'solution_id': solution_id})
        return self.req_post(url=service_url)
