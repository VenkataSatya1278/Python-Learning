#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
import netmiko
import json

devices= [
{'ip':'192.168.0.110',
      'device_type':'cisco_ios',
	  'username':'cisco',
	  'password':'cisco'},

{'ip':'192.168.0.102',
      'device_type':'cisco_ios',
	  'username':'cisco',
	  'password':'cisco'},

{'ip':'192.168.0.12',
  'device_type':'cisco_ios',
  'username':'cisco',
  'password':'cisco'}
]

netmiko_exceptions= (netmiko.ssh_exception.NetMikoTimeoutException,
	netmiko.ssh_exception.NetMikoAuthenticationException)

for device in devices:
	try:
		print('connect to device',device['ip'])
		connection = netmiko.ConnectHandler(**device)
		print(connection.send_command('show ip int brief'))
		connection.disconnect()

	except netmiko_exceptions as e:
		print('failed to connect to', device['ip'], e)