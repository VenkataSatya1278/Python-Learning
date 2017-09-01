#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
import netmiko
import json

devices='''192.168.0.110
192.168.0.102'''.strip().splitlines()

device_type='cisco_ios'

username='cisco'
password='cisco'

netmiko_exceptions= (netmiko.ssh_exception.NetMikoTimeoutException,
	netmiko.ssh_exception.NetMikoAuthenticationException)

for device in devices:
	try:
		print('connect to device',device)
		connection = netmiko.ConnectHandler(ip=device,device_type=device_type,
											username=username,password=password)
		print(connection.send_command('show ip int brief'))
		connection.disconnect()

	except netmiko_exceptions as e:
		print('failed to', device, e)