from gocloud.client import request_utils


class Logs():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch

    def list_logs(self):
        service_url = "/v2/logs/"
        return self.req_get(url=service_url)

    def list_logfiles_by_server(self, server_id, user_id=None):
        service_url = "/v2/logs/?server_id=%s"
        service_url = service_url % server_id
        params = "&%s=%s&"
        if user_id:
            service_url = service_url + (params % ("user_id", user_id))
        return self.req_get(url=service_url)

    def get_logs(self, log_id, begin_time=None, end_time=None,
                 past_time=None, search=None):
        service_url = "/v2/logs/%(log_id)s/content/"
        service_url = service_url % {'log_id': log_id}
        # append params to url
        params = {}
        if begin_time and end_time:
            params.update({'begin_time': begin_time,
                           'end_time': end_time})
        if search:
            params.update({'search': search})
        if past_time:
            params.update({'past_time': past_time})
        if len(params) > 0:
            service_url += '?'
            for key in params:
                tmp = "%s=%s&" % (key, params[key])
                service_url += tmp
        if service_url[-1] == "&":
            service_url = service_url[:-1]
        return self.req_get(url=service_url)

    def get_logs_by_keyword(self, log_id, keyword=None, past_time="3m"):
        return self.get_logs(log_id, search=keyword, past_time=past_time)

    def set_log(self, server_id, path, keywords=[]):
        service_url = "/v2/logs/"
        data = {'server': server_id, 'path': path}
        if keywords is not None:
            data.update({'keywords': keywords})
        return self.req_post(url=service_url,
                             data=data)

    def delete_log(self, log_id):
        service_url = "/v2/logs/%(log_id)s/"
        service_url = service_url % ({'log_id': log_id})
        return self.req_delete(url=service_url)

    def patch_log(self, log_id, keywords=[]):
        service_url = "/v2/logs/%(log_id)s/"
        service_url = service_url % ({'log_id': log_id})
        data = {'keywords': keywords}
        return self.req_patch(url=service_url,
                              data=data)

    def get_keywords(self):
        service_url = "/v2/logs/keywords/"
        return self.req_get(url=service_url)

    def create_keyword(self, keyword, description=None):
        service_url = "/v2/logs/keywords/"
        data = {'keyword': keyword, 'description': description}
        return self.req_post(url=service_url,
                             data=data)

    def delete_keyword(self, keyword_id):
        service_url = "/v2/logs/keywords/%(keyword_id)s/"
        service_url = service_url % ({'keyword_id': keyword_id})
        return self.req_delete(url=service_url)
