import os 
from sys import argv

ping_arg = (f"ping {argv[1]}")

os.system(ping_arg)