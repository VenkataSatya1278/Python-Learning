#!/usr/bin/env python

import os,subprocess,time

class Server(object):
	def __init__(self,ip,hostname):
		self.ip= ip
		self.hostname=hostname
	def set_ip(self,ip):
		self.ip=ip
	def set_hostname(self,hostname):
		self.hostname=hostname
	def ping(self,ip_addr):
		output= subprocess.getoutput("ping %s -c 3" %(ip_addr))
		time.sleep(10)
		results = output.split("\n")
		for line in results:
			if 'packet loss' in line:
				status= line
				if ' 0% packet loss' in status:
					print("%s is Reachable" % (ip_addr))
				else:
					print("%s is NotReachable" % (ip_addr))

ipaddress = input("Enter ipaddress:")
server= Server(ipaddress,'venkatav-surf')
server.ping(ipaddress)