#!/usr/bin/env python

import os,stat,sys,string,commands
from__future__import absolute_import, division, print_function


def get_input(prompt='')
	try:
		line = raw_input(prompt)
	except NameError:
		line = input(prompt)
	return line

def filepermission(pattern):
	try:
		#commandString = "find " + pattern
		commandString = "ls -l " + pattern
		commandOutput = commands.getoutput(commandString)
		findResults = string.split(commandOutput,"\n")
		for file in findResults:
			file=string.split(file," ")
			file1=string.split(file[-1],"/")
			print"\nPermissions for a file",file1[-1],":",file[0]
	except:
		print("See the above error")

#pattern = raw_input("Enter the file pattern to search\n")
#filepermission(pattern)
