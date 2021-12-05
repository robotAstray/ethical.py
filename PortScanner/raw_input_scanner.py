#!/usr/bin/python

import socket

host = raw_input("[*] Enter host: ")
port = int(raw_input("[*] Enter port: "))

network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def portscanner(port):
    if network_socket.connect_ex((host, port)):

            print("Port %d is closed" % (port))
    else:
            print("Port %d is open" % (port))

portscanner(port)