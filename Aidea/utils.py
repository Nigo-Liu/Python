def get_service_url(ip=None, port='8000', url=''):
    tmpl = "http://%(ip)s:%(port)s/api%(url)s"
    content = {'ip': (ip or '127.0.0.1'), 'port': port, 'url': url}
    return tmpl % content
