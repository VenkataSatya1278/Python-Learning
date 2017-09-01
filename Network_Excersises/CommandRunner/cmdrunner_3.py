#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
import netmiko
import json

netmiko_exceptions= (netmiko.ssh_exception.NetMikoTimeoutException,
	netmiko.ssh_exception.NetMikoAuthenticationException)

with open('devices.json') as dev_file:
	devices = json.load(dev_file)

for device in devices:
	try:
		print('connect to device',device['ip'])
		connection = netmiko.ConnectHandler(**device)
		print(connection.send_command('show ip int brief'))
		connection.disconnect()

	except netmiko_exceptions as e:
		print('failed to connect to', device['ip'], e)