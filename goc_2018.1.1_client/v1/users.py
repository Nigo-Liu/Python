from gocloud.client import request_utils


class Users():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def create(self, username, password, email):
        service_url = "/v1/users/"
        data = {'username': username,
                'password': password,
                'email': email}
        return self.req_post(url=service_url,
                             data=data)

    def associate(self, user_id, group_id, role_id=None):
        service_url = "/v1/users/%s/associations/" % user_id
        data = {'group_id': group_id, 'role_id': role_id}
        return self.req_post(url=service_url,
                             data=data)

    def disassociate(self, user_id, group_id):
        service_url = "/v1/users/%s/associations/" % user_id
        data = {'group_id': group_id}
        return self.req_delete(url=service_url,
                               data=data)

    def change_own_password(self, old_password, new_password):
        service_url = "/v1/users/password/"
        data = {'old_password': old_password,
                'new_password': new_password}
        return self.req_put(url=service_url,
                            data=data)
