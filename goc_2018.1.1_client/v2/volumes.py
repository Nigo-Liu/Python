from gocloud.client import request_utils


class Volumes():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_volumes(self, group_id=None, attached_host=None):
        service_url = "/v2/volumes/"
        if group_id is None and attached_host is None:
            service_url = "/v2/volumes/"
        elif attached_host is None:
            service_url = "/v2/volumes/?group_id=%s" % group_id
        elif group_id is None:
            service_url = "/v2/volumes/?attached_host=%d" % attached_host
        else:
            service_url = "/v2/volumes/?group_id=%s" % group_id
            service_url = service_url + "&attached_host=%d" % attached_host
        return self.req_get(url=service_url)

    def create_volume(self, name, size, group_id,
                      status='ACTIVE', is_public=True,
                      desc=None):
        service_url = "/v2/volumes/"
        data = {'name': name, 'size': size,
                'group': group_id,
                'status': status,
                'is_public': is_public,
                'desc': desc}
        return self.req_post(url=service_url,
                             data=data)

    def delete_volume(self, volume_id):
        service_url = "/v2/volumes/%(volume_id)s/"
        service_url = service_url % ({'volume_id': volume_id})
        return self.req_delete(url=service_url)

    def get_detail(self, volume_id):
        service_url = "/v2/volumes/%(volume_id)s/"
        service_url = service_url % ({'volume_id': volume_id})
        return self.req_get(url=service_url)

    def attach_volume(self, volume_id, server_id, mountpoint=None):
        service_url = "/v2/volumes/%(volume_id)s/action/"
        service_url = service_url % ({'volume_id': volume_id})
        data = {'status': 'attach', 'server_id': server_id}
        if mountpoint:
            data.update({'mountpoint': mountpoint})
        return self.req_put(url=service_url,
                            data=data)

    def detach_volume(self, volume_id, server_id):
        service_url = "/v2/volumes/%(volume_id)s/action/"
        service_url = service_url % ({'volume_id': volume_id})
        data = {'status': 'detach', 'server_id': server_id}
        return self.req_put(url=service_url,
                            data=data)

    def extend_volume(self, volume_id, size):
        service_url = "/v2/volumes/%(volume_id)s/action/"
        service_url = service_url % ({'volume_id': volume_id})
        data = {'size': size}
        return self.req_patch(url=service_url,
                              data=data)

    def get_reports(self, begin_time=None, end_time=None,
                    group_id=None, user_id=None):
        service_url = "/v2/volumes/reports/"
        if begin_time or end_time or group_id or user_id:
            service_url += "?"
        if begin_time:
            service_url += "begin_time=%s&" % begin_time
        if end_time:
            service_url += "end_time=%s&" % end_time
        if group_id:
            service_url += "group_id=%s&" % group_id
        if user_id:
            service_url += "user_id=%s&" % user_id
        return self.req_get(url=service_url)
