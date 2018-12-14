# coding=UTF-8
from gocloud.client import request_utils


class Repositories():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_repos(self, group_id, keyword=None):
        service_url = "/v1/repositories/?"
        if keyword:
            service_url = service_url + ('keyword=%s&' % keyword)
        service_url = service_url + ('group_id=%d' % group_id)
        return self.req_get(url=service_url)

    def list_tags(self, repo_name):
        service_url = "/v1/repositories/tags/?repo_name=%s"
        service_url = service_url % repo_name
        return self.req_get(url=service_url)

    def delete_repo(self, repo_name, tag=None):
        service_url = "/v1/repositories/?"
        if tag:
            service_url = service_url + ('tag=%s&' % tag)
        service_url = service_url + ('repo_name=%s' % repo_name)
        return self.req_delete(url=service_url)

    def list_tag_manifests(self, repo_name, tag):
        service_url = "/v1/repositories/manifests/?repo_name=%s&tag=%s"
        service_url = service_url % (repo_name, tag)
        return self.req_get(url=service_url)
