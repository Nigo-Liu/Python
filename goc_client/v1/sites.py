# coding=UTF-8
from gocloud.client import request_utils
import logging

logger = logging.getLogger(__name__)


class Sites():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def create_site(self,
                    name,
                    tenant,
                    solution_id,
                    desc,
                    **kwargs):
        service_url = "/v1/sites/"
        data = {'name': name,
                'group': str(tenant),
                'solution': str(solution_id),
                'desc': desc}
        if 'servers_account' in kwargs.keys():
            account_info = {'servers_account': kwargs.pop('servers_account')}
            if 'servers_passwd' in kwargs.keys():
                account_info['servers_passwd'] = kwargs.pop('servers_passwd')
            if 'servers_key' in kwargs.keys():
                account_info['servers_key'] = kwargs.pop('servers_key')
            data.update(account_info)
        headers = {}
        for key in kwargs:
            key_name = 'x-extra-property-%s' % key.replace('_', '-')
            headers[key_name] = str(kwargs[key])
        return self.req_post(url=service_url,
                             data=data,
                             headers=headers)

    def delete_site(self, site_id):
        service_url = "/v1/sites/%(site_id)s/"
        service_url = service_url % ({'site_id': site_id})
        return self.req_delete(url=service_url)

    def site_action(self, site_id, status):
        service_url = "/v1/sites/%(site_id)s/action/"
        service_url = service_url % ({'site_id': site_id})
        data = {'status': status}
        return self.req_put(url=service_url,
                            data=data)

    def get_list(self, tenant=None, solution=None, all_users=0):
        service_url = "/v1/sites/"
        params = {'tenant': tenant, 'solution': solution,
                  'all_users': all_users}
        return self.req_get(url=service_url, params=params)

    def get_detail(self, site_id):
        service_url = "/v1/sites/%(site_id)s/"
        service_url = service_url % ({'site_id': site_id})
        return self.req_get(url=service_url)

    def get_container_detail(self, site_id):
        service_url = "/v1/sites/%(site_id)s/container/"
        service_url = service_url % ({'site_id': site_id})
        return self.req_get(url=service_url)
