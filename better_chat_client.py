# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:57:58 2017

@author: chagulwi
"""

import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(addr))
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1', 8888)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = input("Name: ")
message = input(alias + "-> ")
while message != "q":
    if message != '':
        s.sendto((alias + ": " + message).encode(), server)
    tLock.acquire()
    message = input(alias + "-> ")
    tLock.release()
    time.sleep(0.2)
shutdown = True
rT.join()

    