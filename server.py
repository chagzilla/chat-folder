# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:21:04 2017

@author: chagulwi
"""

import socket
import sys
import time

#end of imports

### init variables
s = socket.socket()
host = ''
print(host)
port = 8080
s.bind((host,port))
print("|")
print("server done binding to host and port successfully")
print("|")
s.listen(1)
connection, addr = s.accept()
print(addr, " had connect to the server and is now online..")
print("")
print(connection)
while 1:
    message = input(str(">> "))
    message = message.encode()
    connection.send(message)
    print("")
    print("message had been sent...")
    incoming_message = connection.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Client : ",incoming_message)
    print("")
