#Importing the necessary module
#execute below commands to 
from easysnmp import Session

#Asking the user for input

def snmp_test():
	ip = input('\nEnter the device IP address: ')

	community = input('\nEnter the SNMP community: ')

	#oid = input('\nEnter the OID or MIB name to work on: ')

	#Opening the SNMP session to the device
	session = Session(hostname = ip, community = community, version = 2)

	while True:
		#User input
		print ('\nChoose the SNMP operation you want to perform:\n\n1 - SNMP GET\n2 - SNMP SET\n3 - SNMP WALK\ne - Exit program')

		user_choice = input('\nEnter your choice: ')

		if user_choice == '1':
			oid = input('\nEnter the OID or MIB name to work on: ')


			#Performing SNMP GET
			snmp_get = session.get(oid)

			#Getting the value returned by the device and coverting it to ASCII
			result = snmp_get.value

			#Printing the value
			print('\nThe result of SNMP GET on %s is:' % oid )
			print ('\n' + result + '\n')

			continue

		elif user_choice == '2':

			oid = input('\nEnter the OID or MIB name to work on: ')

			#Asking the user what value should be set for oid
			value = input('\nEnter the value for the object: ')
		
			#Performing SNMP SET
			snmp_set = session.set(oid, value)

			print ('\nDone. Please check device %s.\n' % ip)
		
			continue

		elif user_choice == '3':
			oid = input('\nEnter the OID or MIB name to work on: ')

			#Performing SNMP WALK
			snmp_walk = session.walk(oid)

			#Printing the result
			print ('\nThe result of SNMP WALK on %s is:' % oid)

			for obj in snmp_walk:
				print ('\n' + obj.value)
		
			continue

		elif user_choice == 'e':
			print ('\nExiting program...\n'
		)
			break

		else:
			print ('\nInvalid input. Exiting...\n')

			break

#End Of Program