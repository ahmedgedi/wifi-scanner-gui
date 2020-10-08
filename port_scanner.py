#!/bin/python3

import sys, socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate any given host to IPv4
else:
    print("invalid amount of arguments given!")
    print("Syntax: python3 port_scanner.py <ip>")
    sys.exit()

# Banner
print("#" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("#" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open!")
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program...")
    sys.exit()

except socket.gaierror:
    print("\n Hostname could not be resolved. Exiting program...")
    sys.exit()

except socket.error:
    print("\n Couldn't connect to server. Exiting program...")
    sys.exit()



