import requests
import json
import logging

logger = logging.getLogger(__name__)
_headers = {'Content-Type': 'application/json'}

def get_users(endpoint):
    auth = requests.auth.HTTPBasicAuth('admin','admin')
    url = '{0}/api/v2/users'.format(endpoint)
    return requests.get(url=url, auth=auth, verify=False)
 
def req_get(endpoint):
    url = endpoint
    r = requests.get(url=url ,verify=False)
    print(r.status_code)