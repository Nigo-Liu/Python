import yaml
import os

def load_yaml_file(yaml_file):
	file_location = os.getcwd()
	template_path = file_location + '/Default_network_template/'
	print template_path
	y = yaml.load(file(template_path + yaml_file))
	print y 

load_yaml_file('network-template-vlan-2-nic-default.yaml')    

	