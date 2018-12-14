import importlib
import json

"""
usage:

from gocloud.client import client

ret = client.Client(user=request.user,
                    password='password',
                    url='10.12.20.19')
print ret.logs.list_logs()
"""


def Client(ip='127.0.0.1'):
    client = importlib.import_module(client_module)
    return client.Client(ip)
