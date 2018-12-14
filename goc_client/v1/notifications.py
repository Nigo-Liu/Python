# coding=UTF-8
from gocloud.client import request_utils


class Notifications():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def user_has_event(self):
        service_url = "/v1/notifications/"
        return self.req_get(url=service_url)

    def disable_user_event(self):
        service_url = "/v1/notifications/"
        return self.req_patch(url=service_url)

    def list_notification_event(self, is_read=None):
        service_url = "/v1/notifications/events/"
        params = "?%s=%s"
        if is_read is not None:
            service_url = service_url + (params % ("is_read", is_read))
        return self.req_get(url=service_url)

    def event_is_read(self, event_id):
        service_url = "/v1/notifications/events/%(event_id)s/"
        service_url = service_url % ({'event_id': event_id})
        return self.req_patch(url=service_url)

    def list_notificate_rule(self):
        service_url = "/v1/notifications/rules/"
        return self.req_get(url=service_url)

    def setup_notificate_rule(self, rules=None):
        service_url = "/v1/notifications/rules/"
        data = {'notification_rules': rules}
        return self.req_put(url=service_url,
                            data=data)
