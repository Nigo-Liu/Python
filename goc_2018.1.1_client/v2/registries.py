from gocloud.client import request_utils


class Registries():
    def __init__(self, request, ip):
        req = request_utils.Request(request, ip)
        self.req_get = req.req_get
        self.req_post = req.req_post
        self.req_delete = req.req_delete
        self.req_patch = req.req_patch
        self.req_put = req.req_put

    def list_repos(self, reg_name, project_id, keyword=None):
        service_url = "/v2/registries/%s/projects/%d/repo/" % \
            (reg_name, project_id)
        params = {'keyword': keyword}
        return self.req_get(url=service_url, params=params)

    def delete_repo(self, reg_name, project_id, repo_name, tag=None):
        service_url = "/v2/registries/%s/projects/%d/repo/" % \
            (reg_name, project_id)
        params = {'repo_name': repo_name, 'tag': tag}
        return self.req_delete(url=service_url, params=params)

    def list_tag_manifests(self, reg_name, project_id, repo_name, tag):
        service_url = "/v2/registries/%s/projects/%d/repo/manifests/?"
        service_url = service_url + "repo_name=%s&tag=%s"
        service_url = service_url % (reg_name, project_id, repo_name, tag)
        return self.req_get(url=service_url)
