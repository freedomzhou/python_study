#!/usr/bin/env python3

from socket import *

#HOST = '119.29.23.102'
HOST = '127.0.0.1'
PORT = 21566
ADDR = (HOST,PORT)
BUFSIZE = 1024

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()

