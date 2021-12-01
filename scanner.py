#!/usr/bin/python

import socket
import argparse

# Define flags host and port

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('--host', type=str,
                    help='host')
parser.add_argument('--port', type=int,
                    help='port number')
args = parser.parse_args()

# assign host to a variable host

host = args.host

# Define network socket

network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portscanner(port):
        if network_socket.connect_ex((host,port)):
                print "Port %d is closed" % (port)
        else: 
                print "port %d is open" % (port)

portscanner(args.port)
