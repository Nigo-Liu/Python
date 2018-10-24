import yaml
import os

# dict_network_assignments = {'network_assignments': {'management': {'ep': 'br-mgmt'}, 'storage': {'ep': 'br-storage'}, 'public': {'ep': 'br-ex'}, 'private': {'ep': 'br-prv'}, 'fuelweb_admin': {'ep': 'br-fw-admin'}}}



# dict_nic_mapping = {'default': {'if4': 'eth3', 'if5': 'eth4', 'if1': 'eth0', 'if2': 'eth1', 'if3': 'eth2'}, 'node-1': {'admin': 'eno1', 'api': 'eno2.102', 'storage': 'eno2.101', 'pub': 'eno2.1056', 'priv': 'eno2'}, 'node-3': {'admin': 'enp8s0f0', 'api': 'enp8s0f1.102', 'storage': 'enp8s0f1.101', 'pub': 'enp8s0f1.1056', 'priv': 'enp8s0f1'}, 'node-2': {'admin': 'eth0', 'api': 'eth1.102', 'storage': 'eth1.101', 'pub': 'eth1.1056', 'priv': 'eth1'}}

# dict_network_scheme_physical = {'fuel_fw_admin': {'endpoints': ['br-fw-admin'], 'transformations': [{'action': 'add-br', 'name': 'br-fw-admin'}, {'action': 'add-port', 'bridge': 'br-fw-admin', 'name': '<% admin %>'}], 'roles': {'admin/pxe': 'br-fw-admin', 'fw-admin': 'br-fw-admin'}}, 'api': {'endpoints': ['br-mgmt'], 'transformations': [{'action': 'add-br', 'name': 'br-mgmt'}, {'action': 'add-port', 'bridge': 'br-mgmt', 'name': '<% api %>'}], 'roles': {'murano/api': 'br-mgmt', 'keystone/api': 'br-mgmt', 'neutron/api': 'br-mgmt', 'mgmt/database': 'br-mgmt', 'sahara/api': 'br-mgmt', 'ironic/baremetal': 'br-mgmt', 'mongo/db': 'br-mgmt', 'ceilometer/api': 'br-mgmt', 'glance/api': 'br-mgmt', 'ceph/public': 'br-mgmt', 'mgmt/messaging': 'br-mgmt', 'management': 'br-mgmt', 'swift/api': 'br-mgmt', 'mgmt/vip': 'br-mgmt', 'mgmt/memcache': 'br-mgmt', 'mgmt/api': 'br-mgmt', 'heat/api': 'br-mgmt', 'mgmt/corosync': 'br-mgmt', 'zabbix': 'br-mgmt', 'nova/api': 'br-mgmt', 'murano/cfapi': 'br-mgmt', 'aodh/api': 'br-mgmt', 'horizon': 'br-mgmt', 'nova/migration': 'br-mgmt', 'cinder/api': 'br-mgmt', 'ironic/api': 'br-mgmt'}}, 'storage': {'endpoints': ['br-storage'], 'transformations': [{'action': 'add-br', 'name': 'br-storage'}, {'action': 'add-port', 'bridge': 'br-storage', 'name': '<% storage %>'}], 'roles': {'swift/replication': 'br-storage', 'storage': 'br-storage', 'cinder/iscsi': 'br-storage', 'ceph/replication': 'br-storage'}}, 'public': {'endpoints': ['br-ex'], 'transformations': [{'action': 'add-br', 'name': 'br-ex'}, {'action': 'add-br', 'name': 'br-floating', 'provider': 'ovs'}, {'action': 'add-patch', 'bridges': ['br-floating', 'br-ex'], 'provider': 'ovs', 'mtu': 65000}, {'action': 'add-port', 'bridge': 'br-ex', 'name': '<% pub %>'}], 'roles': {'ceph/radosgw': 'br-ex', 'public/vip': 'br-ex', 'neutron/floating': 'br-floating', 'ex': 'br-ex'}}, 'private': {'endpoints': ['br-prv'], 'transformations': [{'action': 'add-br', 'name': 'br-prv', 'provider': 'ovs'}, {'action': 'add-br', 'name': 'br-aux'}, {'action': 'add-patch', 'bridges': ['br-prv', 'br-aux'], 'provider': 'ovs', 'mtu': 65000}, {'action': 'add-port', 'bridge': 'br-aux', 'name': '<% priv %>'}], 'roles': {'neutron/private': 'br-prv', 'neutron/mesh': 'br-prv'}}}

# dict_network_scheme_vm = {'network_scheme': {'vm_api': {'endpoints': ['br-mgmt'], 'transformations': [{'action': 'add-br', 'name': 'br-mgmt'}, {'action': 'add-port', 'bridge': 'br-mgmt', 'name': '<% if5 %>'}], 'roles': {'murano/api': 'br-mgmt', 'keystone/api': 'br-mgmt', 'neutron/api': 'br-mgmt', 'mgmt/database': 'br-mgmt', 'sahara/api': 'br-mgmt', 'ironic/baremetal': 'br-mgmt', 'mongo/db': 'br-mgmt', 'ceilometer/api': 'br-mgmt', 'glance/api': 'br-mgmt', 'ceph/public': 'br-mgmt', 'mgmt/messaging': 'br-mgmt', 'management': 'br-mgmt', 'swift/api': 'br-mgmt', 'mgmt/vip': 'br-mgmt', 'mgmt/memcache': 'br-mgmt', 'mgmt/api': 'br-mgmt', 'heat/api': 'br-mgmt', 'mgmt/corosync': 'br-mgmt', 'zabbix': 'br-mgmt', 'nova/api': 'br-mgmt', 'murano/cfapi': 'br-mgmt', 'aodh/api': 'br-mgmt', 'horizon': 'br-mgmt', 'nova/migration': 'br-mgmt', 'cinder/api': 'br-mgmt', 'ironic/api': 'br-mgmt'}}, 'vm_fuel_fw_admin': {'endpoints': ['br-fw-admin'], 'transformations': [{'action': 'add-br', 'name': 'br-fw-admin'}, {'action': 'add-port', 'bridge': 'br-fw-admin', 'name': '<% if1 %>'}], 'roles': {'admin/pxe': 'br-fw-admin', 'fw-admin': 'br-fw-admin'}}, 'vm_storage': {'endpoints': ['br-storage'], 'transformations': [{'action': 'add-br', 'name': 'br-storage'}, {'action': 'add-port', 'bridge': 'br-storage', 'name': '<% if2 %>'}], 'roles': {'swift/replication': 'br-storage', 'storage': 'br-storage', 'cinder/iscsi': 'br-storage', 'ceph/replication': 'br-storage'}}, 'vm_public': {'endpoints': ['br-ex'], 'transformations': [{'action': 'add-br', 'name': 'br-ex'}, {'action': 'add-br', 'name': 'br-floating', 'provider': 'ovs'}, {'action': 'add-patch', 'bridges': ['br-floating', 'br-ex'], 'provider': 'ovs', 'mtu': 65000}, {'action': 'add-port', 'bridge': 'br-ex', 'name': '<% if4 %>'}], 'roles': {'ceph/radosgw': 'br-ex', 'public/vip': 'br-ex', 'neutron/floating': 'br-floating', 'ex': 'br-ex'}}, 'vm_private': {'endpoints': ['br-prv'], 'transformations': [{'action': 'add-br', 'name': 'br-prv', 'provider': 'ovs'}, {'action': 'add-br', 'name': 'br-aux'}, {'action': 'add-patch', 'bridges': ['br-prv', 'br-aux'], 'provider': 'ovs', 'mtu': 65000}, {'action': 'add-port', 'bridge': 'br-aux', 'name': '<% if3 %>'}], 'roles': {'neutron/private': 'br-prv', 'neutron/mesh': 'br-prv'}}}}

# dict_node_role = {'templates_for_node_role': {'ceph-osd': ['fuel_fw_admin', 'private', 'storage', 'public', 'api'], 'controller': ['vm_fuel_fw_admin', 'vm_private', 'vm_storage', 'vm_public', 'vm_api'], 'compute': ['fuel_fw_admin', 'private', 'storage', 'public', 'api'], 'mongo': ['vm_fuel_fw_admin', 'vm_private', 'vm_storage', 'vm_public', 'vm_api'], 'cinder': ['fuel_fw_admin', 'private', 'storage', 'public', 'api'], 'virt': ['fuel_fw_admin', 'private', 'storage', 'public', 'api']}}

dict_shell = {'adv_net_template': {'default': {}}}
dict_nic_mapping_shell = {'nic_mapping': {}}
dict_node_role_shell = {'templates_for_node_role': {}}

# dict_network_scheme_vm['network_scheme']['fuel_fw_admin'] = dict_network_scheme_physical['fuel_fw_admin']
# dict_network_scheme_vm['network_scheme']['api'] = dict_network_scheme_physical['api']
# dict_network_scheme_vm['network_scheme']['storage'] = dict_network_scheme_physical['storage']
# dict_network_scheme_vm['network_scheme']['private'] = dict_network_scheme_physical['private']
# dict_network_scheme_vm['network_scheme']['public'] = dict_network_scheme_physical['public']

# dict_shell['adv_net_template']['default']['network_assignments'] = dict_network_assignments['network_assignments']
# dict_shell['adv_net_template']['default']['network_scheme'] = dict_network_scheme_vm['network_scheme']
# dict_shell['adv_net_template']['default']['templates_for_node_role'] = dict_node_role['templates_for_node_role']
# dict_shell['adv_net_template']['default']['nic_mapping'] = dict_nic_mapping['nic_mapping']

# print dict_shell
# print yaml.dump(dict_shell)

# n = yaml.load(file('./Default_network_template/network-template-nic_mapping.yaml'))
# n['nic_mapping']['default']['if4'] = 'eth10'
# print n

def check_folder(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)
		print " Default_network_template_folder_dose_not_existed."
		print " Please put in the default network template files in this folder."
	else:
		print "Default_network_template_folder_existed."

check_folder('./Default_network_template')

def modify_nic_mapping(nic):
	# n = yaml.load(file('./Default_network_template/network-template-nic_mapping.yaml'))
	n = dict_nic_mapping
	n['default']['if4'] = nic
	n['default']['if5'] = nic
	n['node-1']['admin'] = nic
	# n['nic_mapping']['default']['if4']['node-1']['admin'] = 'eth9'
	print n
     
def yaml_to_dict(filename):
	y = yaml.load(file('./Default_network_template/' + filename))
	return y

def dict_to_yaml(filename):
	d = yaml.dump(filename)
	return d 

def dict_get_values(dict_file, value):
	v = dict_file.get(value)
	return v	

dict_network_assignments = yaml_to_dict('network-template-vxlan-network_assignments.yaml')
dict_network_scheme_physical = yaml_to_dict('network-template-vxlan-network_scheme-physical.yaml')
dict_network_scheme_vm = yaml_to_dict('network-template-vxlan-network_scheme-vm.yaml')
dict_nic_mapping = yaml_to_dict('network-template-nic_mapping.yaml')
dict_node_role = yaml_to_dict('network-template-role.yaml')

d = dict_get_values(dict_nic_mapping, 'node-1')
print d

dict_nic_mapping_shell['nic_mapping']['default'] = dict_nic_mapping['default']
dict_nic_mapping_shell['nic_mapping']['node-1'] = dict_nic_mapping['node-1']
dict_nic_mapping_shell['nic_mapping']['node-2'] = dict_nic_mapping['node-2']
dict_node_role_shell['templates_for_node_role'] = dict_node_role['ceph-osd']
dict_network_scheme_vm['network_scheme']['fuel_fw_admin'] = dict_network_scheme_physical['fuel_fw_admin']
dict_shell['adv_net_template']['default']['network_assignments'] = dict_network_assignments['network_assignments']
dict_shell['adv_net_template']['default']['network_scheme'] = dict_network_scheme_vm['network_scheme']
dict_shell['adv_net_template']['default']['nic_mapping'] = dict_nic_mapping_shell['nic_mapping']
dict_shell['adv_net_template']['default']['templates_for_node_role'] = dict_node_role_shell['templates_for_node_role']

d = dict_to_yaml(dict_shell)
print d

# modify_nic_mapping(nic='eth10')
# dict_nic_mapping_shell['nic_mapping']['default'] = dict_nic_mapping['default']
# dict_nic_mapping_shell['nic_mapping']['node-1'] = dict_nic_mapping['node-1']
# dict_shell['adv_net_template']['default']['nic_mapping'] = dict_nic_mapping_shell['nic_mapping']

# test = dict_to_yaml(dict_shell)
# print test

# dict_nic_mapping_shell = yaml_to_dict('network-template-nic_mapping-shell.yaml')
# print dict_nic_mapping_shell





