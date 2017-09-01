#!/usr/bin/env python

import ping
import snmp

#print ('\nChoose the Operation you want to perform:\n\n1 - Ping_Test\n2 - SNMP_Test\n3 - SSH_Test\ne - Exit program')

while True:
	#User input
	print ('\nChoose the Operation you want to perform:\n\n1 - Ping_Test\n2 - SNMP_Test\n3 - SSH_Test\ne - Exit program')

	user_choice = input('\nEnter your choice: ')

	if user_choice == '1':
		#ipaddress = input('\nEnter the IPaddress: ')

		ipaddress = input("Enter ipaddress:")
		server= ping.Server(ipaddress,'venkatav-surf')
		server.ping(ipaddress)
		continue

	elif user_choice == '2':

		snmp.snmp_test()
	
		continue

	elif user_choice == '3':
		
	
		continue

	elif user_choice == 'e':
		print ('\nExiting program...\n'
	)
		break

	else:
		print ('\nInvalid input. Exiting...\n')

		break

#End Of Program
