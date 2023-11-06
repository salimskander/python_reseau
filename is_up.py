from sys import argv
from os import system

print('UP !') if system('ping ' + argv[1] + ' > Nul') == 0 else print('DOWN !')


