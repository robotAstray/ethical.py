#!/usr/bin/python3

import argparse
import socket


parser = argparse.ArgumentParser(description="Command Line Interface Port Scanner")

parser.add_argument('host', type=str, 
                        help='host')

parser.add_argument('--start', type=int, 
			help="The first port you wish to scan from")
parser.add_argument('--end', type=int,
			help="The last port you wish to scan to")
args = parser.parse_args()

# Define socket family

socket_family = socket. AF_INET

# Define socket type

socket_type = socket.SOCK_STREAM

# Define Network Socket 
network_socket = socket.socket(socket_family, socket_type)

socket.setdefaulttimeout(1)

# Set host variable to args.host

host = args.host

# Set start variable to args.start

start = args.start

# Set end variable to args.end

end = args.end
# Define portscanner function 

def portscanner(port):
	if network_socket.connect_ex((host, port)):
		print("Port number %d is closed" % (port))
	else: 
		print("Port number %d is open" % (port))

if start  < end: 
	for port in range (start, end):
		portscanner(port)
else:
	print("--start is smaller than --end, please start again")
