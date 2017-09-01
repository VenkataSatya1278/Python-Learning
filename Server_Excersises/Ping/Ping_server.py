#!/usr/bin/env python

import Ping_module

def main():
	ipaddress = input("Enter ipaddress:")
	server= Ping_module.Server(ipaddress,'venkatav-surf')
	server.ping(ipaddress)

if __name__ == '__main__'
	main()
