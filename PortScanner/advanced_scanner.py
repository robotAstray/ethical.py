#!/usr/bin/python3

import optparse
from threading import *
from socket import *

def connectionScanner(targetHost,targetPort):
	try:
		network_socket = socket(AF_INET, SOCK_STREAM)
		network_socket.connect((targetHost, targetPort))
		print('%d/tcp Open' % targetPort)
	except:
		print('%d/tcp Closed' % targetPort)
	finally:
		network_socket.close()

def portScanner(targetHost, targetPorts):
	try:
		targetIP = gethostbyname(targetHost)
	except:
		print('Host %s cannot be found' % targetHost)
	try:
		targetName = gethostbyaddr(targetIP)
		print('Scan Results For: ' + targetName[0])
	except:
		print('Scan Results For: ' + targetIP)
	setdefaulttimeout(1)
	for targetPort in targetPorts:
		t = Thread(target=connectionScanner, args=(targetHost, int(targetPort)))
		t.start()

def main():
	parser = optparse.OptionParser("Usage:" + "--host <target host> --port <target port>")
	parser.add_option('--host', dest='targetHost', type='string', help='specify target host')
	parser.add_option('--port', dest='targetPort', type='string', help='specify target ports separated by a comma')
	(options, args) = parser.parse_args()
	targetHost = options.targetHost
	targetPorts = str(options.targetPort).split(',')
	if  targetHost == None or targetPorts[0] == None:
		print(parser.usage)
		exit(0)
	portScanner(targetHost, targetPorts)



if __name__=='__main__':
	main()
