# coding=UTF-8
from gocloud.client import request_utils


class LoadBalancers():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list(self, private_net=None, tenant=None):
        service_url = "/v1/loadbalancers/"
        params = {'private_net': private_net, 'tenant': tenant}
        return self.req_get(url=service_url,
                            params=params)

    def create(self,
               name,
               protocol,
               protocol_port,
               lb_method,
               private_net,
               desc=None):
        service_url = "/v1/loadbalancers/"
        data = {'name': name,
                'protocol': protocol,
                'protocol_port': protocol_port,
                'lb_method': lb_method,
                'private_net': private_net}
        if desc is not None:
            data['desc'] = desc
        return self.req_post(url=service_url,
                             data=data)

    def delete(self, lb_id):
        service_url = "/v1/loadbalancers/%(loadbalancer_id)s/"
        service_url = service_url % ({'loadbalancer_id': lb_id})
        return self.req_delete(url=service_url)

    def update(self, lb_id, lb_method=None, members=None):
        service_url = "/v1/loadbalancers/%(loadbalancer_id)s/"
        service_url = service_url % ({'loadbalancer_id': lb_id})
        data = {}
        if lb_method is not None:
            data['lb_method'] = lb_method
        if members is not None:
            data['members'] = members
        return self.req_patch(url=service_url,
                              data=data)

    def get_detail(self, lb_id):
        service_url = "/v1/loadbalancers/%(loadbalancer_id)s/"
        service_url = service_url % ({'loadbalancer_id': lb_id})
        return self.req_get(url=service_url)
