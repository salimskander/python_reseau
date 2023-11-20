import socket
import os
import psutil
import sys

def lookup(nom):
    domain_ip = socket.gethostbyname(nom)
    print(domain_ip)

def ping(ip):
    ping_arg = (f"ping {ip}")
    os.system(ping_arg)

def ip():
    print(psutil.net_if_addrs()['Wi-Fi'][1][1])
   

if argv[1] == 'lookup':
    lookup(argv[2])
if argv[1] == 'ping':
    ping(argv[2])
if argv[1] == 'ip':
    ip()
else : 
    print (f"Déso.")



    






        
        