import importlib
from config.config import GeminiConfig

"""
usage:

from gocloud.client import client

ret = client.Client(user=request.user,
                    password='password',
                    url='10.12.20.19')
print ret.logs.list_logs()
"""


def Client(request, ip='127.0.0.1'):
    api_version = GeminiConfig.get_config('general').get('default',
                                                         'api_version')
    client_module = "gocloud.client.v%s.client" % api_version
    client = importlib.import_module(client_module)
    return client.Client(request, ip)
