#!/bin/bash
RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[1;32m'
ORANGE='\033[0;33m'
GREY='\033[0;37m'

current_version='1.0.0'


########################################################
wget -q --spider http://duckduckgo.com                #### Check internet connection by viewing duckduckgo.com
                                                      ##
if [ $? -eq 0 ]; then                                 ##
    clear                                             ##
                                                      ##
else                                                  ##
    wget -q --spider http://google.com                #### In case duckduckgo.com is offline,then check google.com to confirm that there is no internet connection
                                                      ##
    if [ $? -eq 0 ]; then                             ##
        clear                                         ##
    else                                              ##
        echo "You do not have internet connection"    ##
        exit                                          ##
    fi                                                ##
fi                                                    ##
########################################################



pkgs='jq curl' # required packages
################################################
if ! dpkg -s $pkgs >/dev/null 2>&1; then      #### If packages are not installed,then install them
  sudo apt-get install $pkgs                  ##
fi                                            ##
################################################


logo(){
echo -e "${GREY}"
echo -e "                                               "
echo -e "                       +osssssso+              "
echo -e "                /oyhhhyso++++++osyhhhs         "
echo -e "             ohdyo       ++oo++                "
echo -e "          /yds    /shhhhyssooosyyhhho          "
echo -e "        /hh+  /ohhy                            "
echo -e "            /hds   /oyhhhhs                    "
echo -e "          /hd+  /sdhs                          "
echo -e "         smo  /hdo   /shhhhhhhhhhs+            "
echo -e "        hd/  ymo  /ydyo/          \dy+         "
echo -e "       hd  /dh   ydo                \dh        "
echo -e "      om/  dy  /my                    y        "
echo -e "      No  sm  /ms                              "
echo -e " yy   d   No  yd        Coded                  "
echo -e " ds       M/  ms                               "
echo -e " ms       M/  ms         By     ohhhhhhhhh   y "
echo -e " hh  om    No yd                        sm  /N "
echo -e " oN   No   yd /No       R4GN4R         +N+  yd "
echo -e "  ms  sm    d\ /ms                    omo  oN/ "
echo -e "  oN/  hh       /yd+                +hd/  sm+  "
echo -e "   sm/  hd/       /ydy+          +sdh+  /hh/   "
echo -e "    ym/  sm+         +shhhhhhhhhhy+   +hd+     "
echo -e "     omo   dh+                     oydy+       "
echo -e "      /hh/  +hdo    /yhhhyyssyyhhhhs/          "
echo -e "        +dh+   shhs                            "
echo -e "          +hds    ayhhhyssooooosyhhhy+         "
echo -e "             ohdy      +++0000+++              "
echo -e "                +shhhyso++////+/               "
echo -e "                                               "                                       
echo -e "                                               ______      __                                    "
echo -e "  ____                  _   _       _          \  ___|_ __ \ \           _ _                     "
echo -e " / ___|_ __ ___ _   _  | \ | | ___ (_)___  ___  \ \  | '_ \ \ \     ___ (_) |_                   "
echo -e "| |  _| '__/ _ \ | | | |  \| |/ _ \| / __|/ _ \  > > | |_)   > \   / _ \| | __|                  "
echo -e "| |_| | | |  __/ |_| | | |\  | (_) | \__ \  __/ / /__| .__/ / ^ \ | (_) | | |_                   "
echo -e " \____|_|  \___|\__, | |_| \_|\___/|_|___/\___|/_____|_|   /_/ \_\ \___/|_|\__| $current_version "
echo -e "                |___/                                                                            "


}
logo

menu(){
echo -e "${GREY}"
echo "==========  Services  =========="
echo "==         1) Ip Lookup       =="
echo "==         2) GNQL            =="
echo "==         3) Metadata        =="
echo "==         4) Update Check    =="
echo "================================"
}
menu

while [[ "$option" != "exit" ]]; do

printf "${GREY}└──╼>>>${NC}"; read option

if [[ "$option" == "1" ]]; then
	python3 ip_lookup.py

elif [[ "$option" == "2" ]]; then
	python3 gnql.py

elif [[ "$option" == "3" ]]; then
	api_key=$(cat greynoise_api_v2.txt)
	cd Metadata
	curl -s -X GET 'https://api.greynoise.io/v2/meta/metadata' -H 'Accept: application/json' -H "key: $api_key" | jq > metadata_output.txt
	cat metadata_output.txt
	cd ..

elif [[ "$option" == "4" ]]; then
	latest_version=$(curl -s https://raw.githubusercontent.com/JimChr-R4GN4R/GreyNoiseSploit/master/.version.md)
	if [[ "$latest_version" == "$current_version" ]]; then
		echo "You are up to date!"
	else
		echo "Latest Version is: $latest_version"
	fi

elif [[ "$option" == "clear" ]]; then
	clear
	menu

elif [[ "$option" == "menu" ]]; then
	menu

elif [[ "$option" == "exit" ]]; then
	exit

else
	
	if [[ "${option}" != "" ]]; then
		echo "Invalid input! PLease try again."
	fi

fi

done
