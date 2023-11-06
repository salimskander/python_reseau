import socket
import os
from sys import argv

nom = argv[1]
ip = socket.gethostbyname(nom)
print(ip)