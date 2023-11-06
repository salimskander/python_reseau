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
   


first_arg = sys.argv[1]
second_arg = sys.argv[2]

if first_arg == 'lookup':
    lookup(second_arg)
if first_arg == 'ping':
    ping(second_arg)
if first_arg == 'ip':
    ip()
else : 
    print (f"Déso.")
    






        
        