import json
import sys

SETTINGS_PATH = 'settings.json'

if __name__ == '__main__':
# 	argv = sys.argv
	# delay_time = 60
	# if argv[1] and argv[1].isdigit():
	# 	delay_time = int(argv[1])
	# else:
	# 	print("%s Invalid arguments: python checkin_cli.py [delay minutes(:num)] %s" % (FAIL, END))
	# 	sys.exit(1)

	with open(SETTINGS_PATH) as json_data:
		settings = json.load(json_data)

		get_val = lambda sets, key: sets[key].encode() if key in sets else None
		account = get_val(settings, 'account')
		password = get_val(settings, 'password')
		project_id = get_val(settings, 'tenant_id')
		GOC_endpoint = get_val(settings, 'GOC_endpoint')
	    

	print(account, password, GOC_endpoint, project_id)

	if not account or not password:
		print("%s Invalid settings: account or password %s" % (FAIL, END))
		sys.exit(1)

    
    

	# if salt:
	# 	email = decode(salt, email)
	# 	pwd = decode(salt, pwd)

	# now = datetime.datetime.now()
	# checkin_time = now + datetime.timedelta(seconds= delay_time * 60)
	# print("%s System will checkin at %s %s" % (COLOR, checkin_time.strftime('%H:%M:%S'), END))

	# time.sleep(60 * delay_time)
	# checkin(email, pwd)
	# print("%s Checkin completed!! %s" % (COLOR, END))
