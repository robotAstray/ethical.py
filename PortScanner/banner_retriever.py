#!/usr/bin/python

import socket 


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
        # retrieve a banner from a sigle port
        port = 22
        ip = "192.168.1.6"
        # create a variable storing the result of actual ports sending us banner back
        banner = returnBanner(ip, port)
        if banner:
                print("[+]" + ip + ":" + banner)


main()
