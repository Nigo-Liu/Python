import yaml
import os

def check_folder(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)
		print " Default_network_template_folder_dose_not_existed."
		print " Please put in the default network template files in this folder."
	else:
		print "Default_network_template_folder_existed."


check_folder('./Default_network_template')


def modify_nic_mapping(nic1,nic2,nic3,nic4,nic5):
		file_location = os.getcwd()
		y = yaml.load(file('./Default_network_template/network-templat-nic_mapping.yaml'))
		return y



def load_yaml_file(yaml_file):
	file_location = os.getcwd()
	template_path = file_location + '/Default_network_template/'
	print template_path
	y = yaml.load(file(template_path + yaml_file))
	return y

dictionary = load_yaml_file('network-template-vlan-2-nic-nic.yaml')


def generator_yaml(name, text):
	yamlfile = name + '.yaml' 
	file = open(yamlfile, 'w')
	file.write(text)
	file.close()
	
text = yaml.dump(dictionary)
generator_yaml('Network_template_2_NIC_NIC', text) 











