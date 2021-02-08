import socket

devices_found = []

# hacky way of targeting the router IP by default. 
ip = socket.gethostbyname(socket.gethostname())
r_ip = ip.split('.')
r_ip[-1] = "1"
ip = ".".join(r_ip)