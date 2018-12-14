from gocloud.client import request_utils


class Infra():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_nodes(self, hostname=None, role=None):
        name_query = 'hostname=%s' % hostname if hostname else ''
        role_query = 'role=%s' % role if role else ''
        if hostname and role:
            service_url = "/v1/infrastructure/hosts/?%s&%s" % (name_query,
                                                               role_query)
        elif hostname or role:
            service_url = "/v1/infrastructure/hosts/?%s" %\
                (name_query or role_query)
        else:
            service_url = "/v1/infrastructure/hosts/"
        return self.req_get(url=service_url)

    def get_node_detail(self, host_id):
        service_url = "/v1/infrastructure/hosts/%s/" % host_id
        return self.req_get(url=service_url)

    def get_pods_on_node(self, host_id):
        service_url = "/v1/infrastructure/hosts/%s/pods/" % host_id
        return self.req_get(url=service_url)
