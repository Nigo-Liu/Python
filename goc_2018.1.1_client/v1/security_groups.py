from gocloud.client import request_utils


class Security_groups():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch

    def get_security_groups(self, sg_id=None, server_id=None, group_id=None):
        service_url = "/v1/security_groups/?"
        params = "%s=%s&"
        if sg_id:
            service_url = service_url + (params % ("sg_id", sg_id))
        if server_id:
            service_url = service_url + (params % ("server_id", server_id))
        if group_id:
            service_url = service_url + (params % ("group_id", group_id))
        return self.req_get(url=service_url)

    def add_security_group_rule(self, security_group_id, direction,
                                port_range_min, port_range_max,
                                remote_ip_prefix, group, protocol=None):
        service_url = "/v1/security_groups/%s/" % security_group_id
        if protocol:
            data = {'direction': direction,
                    'port_range_min': port_range_min,
                    'port_range_max': port_range_max,
                    'remote_ip_prefix': remote_ip_prefix,
                    'protocol': protocol,
                    'group': group}
        else:
            data = {'direction': direction,
                    'port_range_min': port_range_min,
                    'port_range_max': port_range_max,
                    'remote_ip_prefix': remote_ip_prefix,
                    'group': group}
        return self.req_patch(url=service_url,
                              data=data)

    def del_security_group_rule(self, rule_id=None, group_id=None):
        service_url = "/v1/security_group_rules/%s/" % rule_id
        data = {'group': group_id}
        return self.req_delete(url=service_url,
                               data=data)
