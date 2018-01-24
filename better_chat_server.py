# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:05:56 2017

@author: chagulwi
"""

import socket
import time

host = '127.0.0.1'
port = 8888

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False
print("Server Started.")

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)
        print(time.ctime(time.time()) + str(addr) + ": :" + str(data))
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()
            
