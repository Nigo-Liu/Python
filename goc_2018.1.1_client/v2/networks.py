from gocloud.client import request_utils


class Networks():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    # Macvlan api for k8s solutions.
    def create_macvlan_net(self, cidr, gateway):
        service_url = "/v2/k8snetwork/"
        data = {'cidr': cidr, 'gateway': gateway}
        return self.req_post(url=service_url,
                             data=data)

    def delete_macvlan_net(self, network_id):
        service_url = "/v2/k8snetwork/%s/" % network_id
        return self.req_delete(url=service_url)

    def list_macvlan_net(self):
        service_url = "/v2/k8snetwork/"
        return self.req_get(url=service_url)

    def get_network_detail(self, network_id):
        service_url = "/v2/k8snetwork/%s/" % network_id
        return self.req_get(url=service_url)

    def create_ip(self, network_id, ip):
        service_url = "/v2/k8snetwork/%s/ip/" % network_id
        data = {"ip": ip}
        return self.req_post(url=service_url,
                             data=data)

    def delete_ip(self, network_id, ip_id):
        service_url = "/v2/k8snetwork/%(network_id)s/ip/%(ip_id)s/"
        service_url = service_url % {"network_id": network_id, "ip_id": ip_id}
        return self.req_delete(url=service_url)

    def list_ips(self, network_id, pod=None):
        service_url = "/v2/k8snetwork/%s/ip/" % network_id
        if pod:
            service_url = service_url + "?pod=" + pod
        elif pod == '':
            service_url = service_url + "?pod="
        return self.req_get(url=service_url)

    def get_ip_detail(self, network_id, ip_id):
        service_url = "/v2/k8snetwork/%(network_id)s/ip/%(ip_id)s/"
        service_url = service_url % {"network_id": network_id, "ip_id": ip_id}
        return self.req_get(url=service_url)

    def ip_action(self, network_id, ip_id, action,
                  pod, namespace, mac_addr='', redo=False):
        service_url = "/v2/k8snetwork/%(network_id)s/ip/%(ip_id)s/"
        service_url = service_url % {"network_id": network_id, "ip_id": ip_id}
        data = {"action": action, "pod": pod,
                "namespace": namespace, "mac_addr": mac_addr, "redo": redo}
        return self.req_patch(url=service_url,
                              data=data)

    # Goc portal api in default situation.
    def list_networks(self, group_id=None):
        service_url = "/v2/networks/"
        if group_id is None:
            service_url = "/v2/networks/"
        else:
            service_url = "/v2/networks/?group=%s" % group_id
        return self.req_get(url=service_url)

    def create_network(self, name, cidr, gateway, group_id):
        service_url = "/v2/networks/"
        data = {'name': name, 'cidr': cidr,
                'gateway': gateway, 'group': group_id}
        return self.req_post(url=service_url,
                             data=data)

    def delete_network(self, network_id):
        service_url = "/v2/networks/%(network_id)s/"
        service_url = service_url % ({'network_id': network_id})
        return self.req_delete(url=service_url)

    def get_detail(self, network_id):
        service_url = "/v2/networks/%(network_id)s/"
        service_url = service_url % ({'network_id': network_id})
        return self.req_get(url=service_url)
