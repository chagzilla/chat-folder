# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:22:29 2017

@author: chagulwi
"""

import sys
import socket
import time

s = socket.socket()
host = input(str("Please enter the hostname of the server:"))
port = 8080
print(s.connect((host,port)))

print("conneced to chat server")
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Server : ",incoming_message)
    print("")
    message = input(str(">> "))
    message = message.encode()
    s.send(message)
    print("message had been sent...")
    print("")
    