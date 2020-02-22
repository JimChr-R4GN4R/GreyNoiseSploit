#!/bin/bash
RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[1;32m'
ORANGE='\033[0;33m'
GREY='\033[0;37m'


#############################
chmod +x gnql.sh           #### Set execute permissions at GreyNoise's scripts
chmod +x metadata.sh       ##
#############################


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
echo -e "                                               ______      __                   "
echo -e "  ____                  _   _       _          \  ___|_ __ \ \           _ _    "
echo -e " / ___|_ __ ___ _   _  | \ | | ___ (_)___  ___  \ \  | '_ \ \ \     ___ (_) |_  "
echo -e "| |  _| '__/ _ \ | | | |  \| |/ _ \| / __|/ _ \  > > | |_)   > \   / _ \| | __| "
echo -e "| |_| | | |  __/ |_| | | |\  | (_) | \__ \  __/ / /__| .__/ / ^ \ | (_) | | |_  "
echo -e " \____|_|  \___|\__, | |_| \_|\___/|_|___/\___|/_____|_|   /_/ \_\ \___/|_|\__| "
echo -e "                |___/                                                           "
                                               

}
logo
menu(){
echo -e "${GREY}"
echo "==========  Services  =========="
echo "==         1) Ip Lookup       =="
echo "==         2) GNQL            =="
echo "==         3) Metadata        =="
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
