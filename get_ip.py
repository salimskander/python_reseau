import psutil

print(psutil.net_if_addrs()['Wi-Fi'][1][1])