import os
import readline
import sys
import requests
from subprocess import call
from time import gmtime, strftime
import re 
import socket
import json


#######################################################################################################################################
class AutoCompleter(object):  # Custom completer                                                                                    ###### Autocompleter for all script's available commands and extenders
                                                                                                                                    ###
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

commands_list = ["context", "quick", "multi", "ip_finder", "hname2ip","list"] # List of the available commands
completer = AutoCompleter(commands_list) # autocomplete list (commands + extenders)
readline.set_completer(completer.complete)                                                                                          ###
readline.parse_and_bind('tab: complete')                                                                                            ###
#######################################################################################################################################



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



def hname2ip(host_name):
    ########################################################################################################
    ip = call("host '"+host_name+"' | awk '/has address/ { print $4 }' > temp.txt", shell=True)           #### Find host's ip
    ip = open('temp.txt','r')                                                                             ##
    ip = ip.readline().replace('\n','')                                                                   ##
    open('temp.txt', 'w').close() # erase everything in temp.txt                                          ##
    return ip                                                                                             ##
    ########################################################################################################



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
    ####################################################
    time = strftime("%Y-%m-%d:-:%H:%M:%S", gmtime())  #### get time and make file's name with the results (main_command:-:target:-:date:-:time.txt)
    file_name = command+":-:"+ip+":-:"+time+".txt"    ##
    file_name = file_name.replace('/','_')            ##
    return file_name                                  ##
    ####################################################



def results_quick_multi(file_name):
    ###############################################################################################################################################################################################################################################################################################################################
    ##                                                                                                                                                                                                                                                                                                                          ###### If command was quick,then go here and edit the results and then go to results() function
    ##                                                                                                                                                                                                                                                                                                                          ###
                                                                                                                                                                                                                                                                                                                                ###
    with open(file_name, 'r') as json_file:                                                                                                                                                                                                                                                                                     ###
                                                                                                                                                                                                                                                                                                                                ###
        ######################################################
        errors_generated = 0                                #### If there are no errors,then errors_generated = 0 else errors_generated > 0
        file_items_str = str(json_file)                     ##
        errors_generated = file_items_str.count('error')    ##
        ######################################################

        if errors_generated > 0: # If there are errors,then print them

            pass # Go directly and print the error

        else: # if there are no errors, we expect normal results to print

            ##########################################################################
            file_results=json_file.read()                                           #### Read results
            file_items = json.loads(file_results)                                   ##
            ##########################################################################


            

            ######################################################################################################################################################################################################################################################
                                                                                                                                                                                                                                                                #### Print code's meaning and then the results in file.txt
                                                                                                                                                                                                                                                                ##



            ##########################################################################################################################################################################################################
            if str(file_items['code']) == "0x00":                                                                                                                                                                   ##
                print("Code: "+str(file_items['code'])+" (The IP has never been observed scanning the Internet)")                                                                                                   #### Find and print what the code means
            elif str(file_items['code']) == "0x01":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (The IP has been observed by the GreyNoise sensor network)")                                                                                               ##
            elif str(file_items['code']) == "0x02":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (The IP has been observed scanning the GreyNoise sensor network, but has not completed a full connection, meaning this can be spoofed)")                   ##
            elif str(file_items['code']) == "0x03":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (The IP is adjacent to another host that has been directly observed by the GreyNoise sensor network)")                                                     ##
            elif str(file_items['code']) == "0x04":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (Reserved)")                                                                                                                                               ##
            elif str(file_items['code']) == "0x05":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (This IP is commonly spoofed in Internet-scan activity)")                                                                                                  ##
            elif str(file_items['code']) == "0x06":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (This IP has been observed as noise, but this host belongs to a cloud provider where IPs can be cycled frequently)")                                       ##
            elif str(file_items['code']) == "0x07":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (This IP is invalid)")                                                                                                                                     ##
            elif str(file_items['code']) == "0x08":                                                                                                                                                                 ##
                print("Code: "+str(file_items['code'])+" (This IP was classified as noise, but has not been observed engaging in Internet-wide scans or attacks in over 60 days)")                                  ##
            else:                                                                                                                                                                                                   ##
                print("Code: " + str(file_items['code']))                                                                                                                                                           ##      
            ##########################################################################################################################################################################################################
            print()                                                                                                                                                                                                                                         ##
                                                                                                                                                                                                                                                            ##
        ######################################################################################################################################################################################################################################################
        results(file_name) # Go and print the edited results                                                                                                                                                                                                                                                                    ###
                                                                                                                                                                                                                                                                                                                                ###
    ##                                                                                                                                                                                                                                                                                                                          ###
    ##                                                                                                                                                                                                                                                                                                                          ###
    ###############################################################################################################################################################################################################################################################################################################################
        ###     ||
        ###     ||### If command was quick, then print the edited results
        ###     ||
        ###     \/
def results(file_name):
    ##################################
    result = open(file_name,'r')    #### read and print the results
    result = result.read()          ##
    print(result)                   ##
    ##################################


os.chdir("IP_Lookup") # Get in IP_Lookup folder

##########################################################################
main_command = input("\033[0;37m┌─[IP Lookup]\n└──╼>>>\033[1;32;0m")    #### Input
##########################################################################


while main_command != "exit":
###################################################################################################################################################################################################################################################################
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###

    extender = 0 # If extender=0, then user did not put -extender.

    
    sub_command = main_command.split()

    try:

        command = sub_command[0]

        ##################################################
        try:                                            #### If extender > 0, then user tries to put an extender.
            extender = int(sub_command[1].count('-'))   ##
        except:                                         ##
            pass                                        ##
        ##################################################


        ##############################################################################################--context
        if command == "context":

            ip = sub_command[1]

            if sub_command[1] == "-hname2ip": # context -hname2ip host.com

                ###############################
                host_name = sub_command[2]   #### find host's ip and put it in $ip variable
                ip = hname2ip(host_name)     ##
                ###############################


                file_name = file_name_generator() # generate save file's name
                shell_command = call("curl -s -X GET 'https://api.greynoise.io/v2/noise/context/"+ip+"' -H 'Accept: application/json' -H 'key: "+api_key+"' | jq > "+file_name , shell=True) # save API's results in file_name.txt
                results(file_name) # print(results)

            elif extender > 0:
                print("Invalid extender!")

            else: # context xxx.xxx.xxx.xxx


                ##################################################
                check_valid_ip(ip)                              #### Check if IP has valid format
                while check_valid_ip(ip) == 0:                  ##
                    ip = input("Please type a valid IP: ")      ##
                                                                ##
                    if ip == "": # If empty,then cancel         ##
                        break                                   ##
                ##################################################

                if check_valid_ip(ip) == 1: # If ip was valid then continue
                    print()
                    file_name = file_name_generator()
                    shell_command = call("curl -s -X GET 'https://api.greynoise.io/v2/noise/context/"+ip+"' -H 'Accept: application/json' -H 'key: "+api_key+"' | jq > "+file_name , shell=True)
                    results(file_name) # print(results)
                    print()
        ##############################################################################################__context



        ##############################################################################################--quick
        elif command == "quick":



            if sub_command[1] == "-hname2ip": # quick -hname2ip host.com

                ###############################
                host_name = sub_command[2]   #### find host's ip and put it in $ip variable
                ip = hname2ip(host_name)     ##
                ###############################


                file_name = file_name_generator() # generate save file's name
                shell_command = call("curl -s -X GET 'https://api.greynoise.io/v2/noise/quick/"+ip+"' -H 'Accept: application/json' -H 'key: "+api_key+"' | jq > "+file_name , shell=True)
                results(file_name) # print(results)

            elif extender > 0: # If -extender is not -hname2ip, then print error
                print("Invalid extender!")

            else: # quick xxx.xxx.xxx.xxx


                ip = sub_command[1]

                ##################################################
                check_valid_ip(ip)                              #### Check if IP has valid format
                while check_valid_ip(ip) == 0:                  ##
                    ip = input("Please type a valid IP: ")      ##
                                                                ##
                    if ip == "": # If empty,then cancel         ##
                        break                                   ##
                ##################################################

                if check_valid_ip(ip) == 1: # If ip was valid then continue
                    print()
                    file_name = file_name_generator()
                    shell_command = call("curl -s -X GET 'https://api.greynoise.io/v2/noise/quick/"+ip+"' -H 'Accept: application/json' -H 'key: "+api_key+"' | jq > "+file_name , shell=True)
                    results_quick_multi(file_name) # Print results
                    print()
        ##############################################################################################__quick





        ##############################################################################################--multi
        elif command == "multi":

            

            if sub_command[1] == "-list": # multi -list list/path/ip_list.txt

                list_path = sub_command[2]
                list_path_file = open(list_path,'r')
                list_path_file = list_path_file.read().replace('\n',',').replace(' ',',').replace(',,',',')

                print()
                ip = list_path.replace('/','-') # give at filename,the list path
                file_name = file_name_generator()
                shell_command = call("curl -s -X GET 'https://api.greynoise.io/v2/noise/multi/quick?ips="+list_path_file+"' -H 'Accept: application/json' -H 'key: "+api_key+"' | jq > "+file_name , shell=True)
                results(file_name) # print(results)
                print()

            elif extender > 0:
                print("Invalid extender!")

            else: # multi x.x.x.1,x.x.x.2,3.2.1.1

                ip = sub_command[1]

                print()
                file_name = file_name_generator()
                shell_command = call("curl -s -X GET 'https://api.greynoise.io/v2/noise/multi/quick?ips="+ip+"' -H 'Accept: application/json' -H 'key: "+api_key+"' | jq > "+file_name , shell=True)
                results(file_name) # print(results)
                print()
        ##############################################################################################__multi




        ##############################################################################################--ip_finder
        elif command == "ip_finder": 

            ip = sub_command[1]

            shell_command = call("host '"+ip+"' | awk '/has address/ { print $4 }'", shell=True)
        ##############################################################################################__ip_finder




        ##############################################################################################--help
        elif command == "help":

            print("\033[0;37m")
            shell_command = call("cat help.txt", shell=True)
            print("\033[1;32;0m")
        ##############################################################################################__help


        ##############################################################################################--help
        elif command == "c_help":

            print("\033[0;37m")
            shell_command = call("cat codes_help.txt", shell=True)
            print("\033[1;32;0m")
        ##############################################################################################__help



        ###############################################--clear
        elif command == "clear": 

            shell_command = call("clear", shell=True)
        ###############################################__clear



        #################################################--exit
        elif command == "exit":
            commands_list = []
            call("cd .. ; ./greynoise.sh", shell=True)
        #################################################__exit



    ##############
    except:     #### If there is no or not valid command,then read again
        pass    ##
    ##############


    
    ##########################################################################
    main_command = input("\033[0;37m┌─[IP Lookup]\n└──╼>>>\033[1;32;0m")    #### Input
    ##########################################################################


###                                                                                                                                                                                                                                                         ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###                                                                                                                                                                                                                                                             ###
###################################################################################################################################################################################################################################################################
