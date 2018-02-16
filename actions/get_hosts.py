from pyzabbix import ZabbixAPI
from st2common.runners.base_action import Action

#zapi = ZabbixAPI("http://192.168.56.101/zabbix")
#zapi.login("Admin", "zabbix")
#print("Connected to Zabbix API Version %s" % zapi.api_version())

class getHosts(Action):
	def run(self):
		hosts=[]
		zapi = ZabbixAPI("http://192.168.56.101/zabbix")
		zapi.login("Admin", "zabbix")

		for h in zapi.host.get(output="extend"):
			print h['name']
			hosts.append(h['name'])
		print hosts
		return hosts
