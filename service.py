#!/usr/bin/env python3
#filename:service.py

from socket import *
from time import ctime

HOST = ''
PORT = 21566
ADDR = (HOST,PORT,)


tcpServSock = socket(AF_INET,SOCK_STREAM)
tcpServSock.bind(ADDR) 
tcpServSock.listen(5)
BUFSIZE = 1024

while True:
    print('waiting for connection... ')
    tcpClinSock,addr = tcpServSock.accept()
    print('connected from: ',addr)

    while True:
        data = tcpClinSock.recv(BUFSIZE).decode()
        if not data:
            break
        tcpClinSock.send(('[%s] %s' % (ctime(),data)).encode())

    tcpClinSock.close()
tcpServSock.close()
        
