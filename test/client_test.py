import json
import sys
import job_test

SETTINGS_PATH = 'settings.json'

if __name__ == '__main__':

	with open(SETTINGS_PATH) as json_data:
	    settings = json.load(json_data)
	    get_val = lambda sets, key: sets[key].encode() if key in sets else None
	    account = get_val(settings, 'account')
	    password = get_val(settings, 'password')
	    GOC_endpoint = get_val(settings, 'GOC_endpoint')
	    headers = get_val(settings, 'headers')

        print(account, GOC_endpoint, password, headers)

        y = job_test.req_get(GOC_endpoint)
        x = job_test.get_users(GOC_endpoint)
        print x.text
          
        


