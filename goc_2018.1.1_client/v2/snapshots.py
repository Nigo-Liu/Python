from gocloud.client import request_utils


class Snapshots():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_snapshots(self, volume_id=None, group_id=None):
        service_url = "/v2/snapshots/"
        params = {'volume': volume_id, 'group_id': group_id}
        return self.req_get(url=service_url, params=params)

    def create_snapshot(self, name, volume_id, desc=None):
        service_url = "/v2/snapshots/"
        data = {'name': name, 'volume': volume_id}
        if desc is not None:
            data['desc'] = desc
        return self.req_post(url=service_url,
                             data=data)

    def delete_snapshot(self, snapshot_id):
        service_url = "/v2/snapshots/%(snapshot_id)s/"
        service_url = service_url % ({'snapshot_id': snapshot_id})
        return self.req_delete(url=service_url)

    def restore_snapshot(self, snapshot_id, name, desc=None):
        service_url = "/v2/volumes/"
        if desc is None:
            data = {'name': name, 'src_snapshot': snapshot_id}
        else:
            data = {'name': name, 'desc': desc, 'src_snapshot': snapshot_id}
        return self.req_post(url=service_url,
                             data=data)

    def get_detail(self, snapshot_id):
        service_url = "/v2/snapshots/%(snapshot_id)s/"
        service_url = service_url % ({'snapshot_id': snapshot_id})
        return self.req_get(url=service_url)
