import os
import socket
import sys
import logging
from subprocess import Popen,PIPE
import traceback
import validators
from scapy.layers.inet import traceroute
import requests
import json
from mapper import mapIt

logging.basicConfig(level=logging.INFO, format='%(process)d-%(levelname)s-%(message)s')
if len(sys.argv) == 2:
    hostname = sys.argv[1]
    try:
        logging.info("Starting traceroute for [ " + hostname + " ]")
        COMMAND = "echo \"pas here\" | sudo -S tcptraceroute -n " + hostname + " | awk '{print $2}'"
        RESULT = Popen(COMMAND,stdout=PIPE,shell=True)
        BASE_URL="http://ip-api.com/json/"
        latitudes = []
        longitudes = []
        while True:

            line = RESULT.stdout.readline();
            if not line:
                break
            else:
                try:
                    ip = socket.gethostbyname(line)
                    print(ip)
                    FINAL_URL = BASE_URL + ip
                    response = requests.get(FINAL_URL)
                    parsed_json = json.loads(response.content)
                    print(parsed_json["lat"])
                    latitudes.append(parsed_json["lat"])
                    longitudes.append(parsed_json["lon"])
                    print(latitudes)
                    print(longitudes)
                    # TODO: curl fire a request for each ip
                except:
                    if validators.domain(line):
                        print(line)
                        # TODO: curl fire to find ip of domain , the curl to get location of ip
                    else:
                        traceback.print_exc()

        mapIt(latitudes,longitudes)
    except Exception as exception:
        traceback.print_exc()
else:
    logging.error("Usage: tracer.py <hostname> , no hostname provided !")
