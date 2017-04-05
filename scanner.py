#!/usr/bin/python
# -*-coding:utf8;-*-
import socket, os, threading, argparse, sys
parser = argparse.ArgumentParser(prog='scanner', usage='%(prog)s [options]')
parser.add_argument("-sc", 'sockconn', help='performes an sock connection')
parser.add_argument('host', type=str, help='host to scan')

args = parser.parse_args()

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect()
        s.close()
        print("[+] " + host + " has " + port + " open.")
    except:
        pass



class config(object):
    def __init__(self):
        pass


try:
    print("press a key for time")
    while not input():
        sys.stdout.write()
        sys.stdout.flush()
except KeyboardInterrupt:
    os.popen("kill -9 " + str(os.getpid()))