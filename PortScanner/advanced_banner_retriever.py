#!/usr/bin/python

import socket 
import argparse

def returnBanner(ip, port):
        try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((ip, port))
                banner = s.recv(1024)
                return banner
        # in case it does not work return the fucntion itself
        except:
                return


def main():
	parser = argparse.ArgumentParser(description="Command Line Interface Banner Retriever")

	parser.add_argument('--start', type=int,
				help='The first port you wish to scan from')
	parser.add_argument('--end', type=int,
				help='The last port you wish to scan from')
	args = parser.parse_args()
	start = args.start
	end = args.end
        # retrieve a banner from a sigle port
        ip = raw_input("[*] Enter IP Address: ")
        # create a variable storing the result of actual ports sending us banner back
	for port in range(start, end):  
     		banner = returnBanner(ip, port)
        	if banner:
               		print("[+]" + ip + "/" + str(port) + " : " + banner).strip('/n')


main()

