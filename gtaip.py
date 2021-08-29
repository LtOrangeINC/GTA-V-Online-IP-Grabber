import requests
from scapy.all import *
import socket
from ip2geotools.databases.noncommercial import DbIpCity
import time

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
    
def pc(packet):
    if packet.proto == 17:
        udp = packet.payload

print("CTRL + C TO STOP")
while True:
 x = sniff(filter="udp and port 6672", prn=pc, store=1, count=1)# GTA V Online UDP default Port is 6672
 y = x[0][IP].src
 z = x[0][IP].dst
 if z == local_ip:
     pass
 else:
    print("-----------------------------------------------------------")
    try:
        time.sleep(5)
        print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}] Region: [{DbIpCity.get(z, api_key='free').region}] City: [{DbIpCity.get(z, api_key='free').city}]")
    except:
        time.sleep(5)
        print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}]")
        print("-----------------------------------------------------------")


        


    





