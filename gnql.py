import os
import readline
import shlex
import subprocess
import sys
import requests
from subprocess import call
from time import gmtime, strftime
import re 
import socket
import json


########################################################################################################################
class AutoCompleter(object):  # Custom completer                                                                     ###### Autocompleter for all script's available commands and extenders
																					                                 ###
	def __init__(self, options):
		self.options = sorted(options)

	def complete(self, text, state):
		if state == 0:  # on first trigger, build possible matches
			if str(text):  # cache matches (entries that start with entered text)
				self.matches = [s for s in self.options 
									if s and s.startswith(text)]
			else:  # no text entered, all matches possible
				self.matches = self.options[:]
			
		# return match indexed by state
		try: 
			return self.matches[state]
		except IndexError:
			return None

                                                                                                                     ###
                                                                                                                     ###
                                                                                                                     ###
########################################################################################################################

##############################################################################################################################
																															#### Autocomplete list maker
																															##
def List_Chooser(AutoComplete_List_number):
	if (AutoComplete_List_number == 1):

		commands_list = [ "help", "c_help", "ip_finder","ip:", "classification:", "first_seen:", "last_seen:", "actor:", "tags:", "metadata.category:", "metadata.os:", "metadata.country:", "metadata.country_code:", "metadata.city:", "metadata.organization:", "metadata.rdns:", "metadata.asn:", "metadata.tor:", "raw_data.scan.port:", "raw_data.scan.protocol:", "raw_data.web.paths:", "raw_data.web.useragents:", "raw_data.ja3.fingerprint:", "raw_data.ja3.port:", "examples ip", "examples classification", "examples first_seen", "examples last_seen", "examples actor", "examples tags", "examples metadata.category", "examples metadata.country", "examples metadata.country_code", "examples metadata.city", "examples metadata.organization", "examples metadata.rdns", "examples metadata.asn", "examples metadata.tor", "examples raw_data.scan.port", "examples raw_data.scan.protocol", "examples raw_data.web.paths", "examples raw_data.web.useragents", "examples raw_data.ja3.fingerprint", "examples raw_data.ja3.port", "examples tools", "examples worms", "examples search_engines", "examples metadata.os" ]

	completer = AutoCompleter(commands_list) # autocomplete list (commands + extenders)
	readline.set_completer(completer.complete)  
	readline.parse_and_bind('tab: complete')  
																															##
																															##
##############################################################################################################################

#########################################
AutoComplete_List_number = 1           #### First load autocomplete list
List_Chooser(AutoComplete_List_number) ##
#########################################

###########################################################################################################################################################################################
##                                                                                                                                                                                      ###### API Area
##                                                                                                                                                                                      ###
																																														###
def api_length(api_file):    
######################################################################## 
	lines=0                                                           #### Check API's length
	words=0                                                           ##
	characters=0                                                      ##
	for line in api_file:                                             ##
		wordslist=line.split()                                        ##
		lines=lines+1                                                 ##
		words=words+len(wordslist)                                    ##
		characters += sum(len(word) for word in wordslist)            ##
	return characters                                                 ##
########################################################################
							### /\
							### ||### 1.Check API's length
							### ||
##################################################################################################################################
																																#### Read and Verify API key 
##########################################################################                                                      ##
api_file = open('greynoise_api_v2.txt','r')                             #### Read API key and check it's length                 ##
api_length_chars = int(api_length(api_file)) # Check API's key length   ##                                                      ##
api_file.close() # after read for while condition,close file            ##                                                      ##
##########################################################################                                                      ##
																																##
																																##
while (api_length_chars != 64): # If API's file is empty or less than 64 chars (because API keys have 64 chars)                 ##
																																##
	##############################################################################                                              ##
																				##                                              ##
	api_file = open('greynoise_api_v2.txt','w') #open file with write perms     ##                                              ##
																				##                                              ##
																				##                                              ##
	api_key = input("Please type your API here:")                               ##                                              ##
																				##                                              ##
																				##                                              ##
	api_file.write(api_key)                                                     ##### Write API key in greynoise_api_v2.txt     ##
	api_file.close()                                                            ##                                              ##
	##############################################################################                                              ##
																																##
																																##
	######################################################                                                                      ##
	api_file = open('greynoise_api_v2.txt','r')         #### Check new API key's length                                         ##
	api_length_chars = int(api_length(api_file))        ##                                                                      ##
	######################################################                                                                      ##
																																##
																																##
																																##
																																##
																																##
api_file.close() # Final close file                                                                                             ##
																																##
##################################################################################################################################
							###||
							###||### 2.Copy validated API key in $api_key
							###\/
##############################################
api_file = open('greynoise_api_v2.txt','r') #### Copy validated API key in $api_key
api_key = api_file.read().replace('\n','')  ##
api_file.close()                            ##
##############################################
																																														###
##                                                                                                                                                                                      ###
##                                                                                                                                                                                      ###
###########################################################################################################################################################################################



#############################################################################################
																						  ###### Check IP' valid format
																						  ###
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def check_valid_ip(ip):

	if(re.search(regex, ip)):  # If ip's format is x.x.x.x then

		###############################
		try:                         #### Check if it contains characters except numbers
			socket.inet_aton(ip)     ## 
			return 1                 ##
		except socket.error:         ##
			return 0                 ##
		###############################
		  
	else: # If ip's format is not x.x.x.x then
		return 0

																						  ###
																						  ###
#############################################################################################
		


def file_name_generator():
	############################################################
	time = strftime("%Y-%m-%d:-:%H:%M:%S:", gmtime())         #### get time and make file's name with the results (main_command:-:target:-:date:-:time.txt)
	file_name = command+":-:"+time+".txt"                     ##
	file_name = file_name.replace('/','_').replace('&','_')   ### '&' is replaced,cause of API reasons
	return file_name                                          ##
	############################################################


def results(file_name):
	##################################
	result = open(file_name,'r')    #### read and print the results
	result = result.read()          ##
	print(result)                   ##
	##################################


os.chdir("GNQL") # Get in IP_Lookup folder

#####################################################################################
main_command = input("\033[0;37mGNQL/>>>\033[1;32;0m").replace(' AND ','%20')      #### Input
#####################################################################################


while main_command != "exit":
###################################################################################################################################################################################################################################################################
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###

	
	sub_command = main_command.split()

	try:

		command = sub_command[0]


		##############################################################################################--query
		if command.startswith( "query=" ) == True:

			print()
			file_name = file_name_generator()
			shell_command = call("curl -s -X GET 'https://api.greynoise.io/v2/experimental/gnql?"+command+"' -H 'Accept: application/json' -H 'key: "+api_key+"' | jq > "+file_name, shell=True)
			results(file_name) # print(results)
			print()
		##############################################################################################__query


		##############################################################################################--ip_finder
		elif command == "ip_finder": 

			ip = sub_command[1]

			shell_command = call("host '"+ip+"' | awk '/has address/ { print $4 }'", shell=True)
		##############################################################################################__ip_finder


		##############################################################################################--Examples
		elif command == "examples":

			##################################################################################################
			if sub_command[1] == "-a":                                                                     ###### -a means show all examples for actor or tags facet,else show normal lists.
				facet = sub_command[2].replace(':','')                                                     ###     added remove : for extra security
                                                                                                           ###
				if (facet == "actor") or (facet == "tags"):                                                ###
					print()                                                                                ###
					shell_command = call("cd examples ; cat "+facet+"_a_list.txt ; cd ..", shell=True)     ###
					print()                                                                                ###
				else:                                                                                      ###
					print()                                                                                ###
					shell_command = call("cd examples ; cat "+facet+"_list.txt ; cd ..", shell=True)       ###
					print()                                                                                ###
            ##################################################################################################
			else: # show normal lists.

				facet = sub_command[1].replace(':','') # added remove : for extra security

				print()
				shell_command = call("cd examples ; cat "+facet+"_list.txt ; cd ..", shell=True)
				print()
		##############################################################################################__Examples


		##############################################################################################--help
		elif command == "help":

			print("\033[0;37m")
			shell_command = call("cat help.txt", shell=True)
			print("\033[1;32;0m")
		##############################################################################################__help


		##############################################################################################--c_help
		elif command == "c_help":

			print("\033[0;37m")
			shell_command = call("cat codes_help.txt", shell=True)
			print("\033[1;32;0m")
		##############################################################################################__c_help


		###############################################--clear
		elif command == "clear": 

			shell_command = call("clear", shell=True)
		###############################################__clear



		#################################################--exit
		elif command == "exit":
			call("cd .. ; ./greynoise.sh", shell=True)
		#################################################__exit



	##############
	except:     #### If there is no or not valid command,then read again
		pass    ##
	##############



	#####################################################################################
	main_command = input("\033[0;37mGNQL/>>>\033[1;32;0m").replace(' AND ','%20')      #### Input
	#####################################################################################


###                                                                                                                                                                                                                                                         ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###################################################################################################################################################################################################################################################################

