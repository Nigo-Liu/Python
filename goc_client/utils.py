# coding=UTF-8
def get_service_url(ip=None, port='443', url=''):
    tmpl = "https://%(ip)s:%(port)s/api%(url)s"
    content = {'ip': (ip or '127.0.0.1'), 'port': port, 'url': url}
    return tmpl % content
