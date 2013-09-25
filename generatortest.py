#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
from __future__ import print_function  # For compability with python2
import libcommon  # Helps with debugging and logging
import logging
import socket
import time

#HANDLES COMPATIBILITY FOR PYTHON2
import sys
if sys.version_info[0] == 2:
    input = raw_input

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES WRAPPER FUNCTIONS
#DEFINES FUNCTIONS
def EVENT_TEST():
    print("test completed")


def fSend(sData, sIPAdress, iPort):
    '''Sends a string to a receiving socket.'''
    #Creates a socket object
    oSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Tries to connect to the listening server
    while True:
        try:
            print(sIPAdress)
            oSocket.connect((sIPAdress, iPort))
        except Exception as e:
            print(e)
            time.sleep(0.5)
        else:
            #Sends the string of characters on the socket
            oSock.send(sData)
            break

    #Closes and deletes the socket to free up the port used
    oSock.close()
    del oSock

def fsSendAndReceives(sData, sIPAdress, iPort):
    '''Sends a string to a receiving socket.'''
    #Creates a socket object
    oSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Tries to connect to the listening server
    while True:
        try:
            oSocket.connect((sIPAdress, iPort))
        except Exception as e:
            print(e)
            time.sleep(0.5)
        else:
            #Sends the string of characters on the socket
            oSocket.send(sData)
            sOutput = oSocket.recv(1024)
            break

    #Closes and deletes the socket to free up the port used
    oSocket.close()
    del oSocket

    #Returns the reply
    return(sOutput)

def fReceive(iPort):
    '''Receives and returns a string from a connection socket.'''

    #Creates a socket object
    oSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Binds the socket object to an ip adress and port and starts listening
    #   in on the socket
    oSocket.bind(("127.0.0.1", iPort))
    oSocket.listen(1)

    #Receives a socket and an ip adress from the sender
    oSocket2, sIPAdress = oSocket.accept()

    #Listen in on the receiversocket for up to 1024 bytes of data
    sData = oSocket2.recv(1024)

    #Closes and deletes all sockets to free up ports
    oSocket2.close()
    oSocket.close()
    del oSocket
    del oSocket2

    #returns the data from the sender and the ip adress of the sender
    return(sData, sIPAdress)

def ftsReceiveAndReply(iPort, sData):
    '''Receives and returns a string from a connection socket.'''

    #Creates a socket object
    oSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Binds the socket object to an ip adress and port and starts listening
    #   in on the socket
    oSocket.bind(("127.0.0.1", iPort))
    oSocket.listen(1)

    #Receives a socket and an ip adress from the sender
    oSocket2, sIPAdress = oSocket.accept()
    print(sIPAdress)
    #Receive up to 1024 bytes of data, and reply with sData
    sOutput = oSocket2.recv(1024)
    oSocket2.send(sData)

    #Closes and deletes all sockets to free up ports
    oSocket2.close()
    oSocket.close()
    del oSocket
    del oSocket2

    #returns the data from the sender and the ip adress of the sender
    return(sOutput, sIPAdress)

class cEventMaster():
    '''Receives an incoming connection from an EventSlave,
    stores its ip adress and assigns it a port to listen to for new events.'''
    def __init__(self, iServerPort, iClientPort):
        self.iClientPort = iClientPort
        #import pdb;pdb.set_trace()
        sData, self.sClientIPAdress = ftsReceiveAndReply(iServerPort, str(iClientPort))
        print(self.sClientIPAdress)
        print(sData)

    def mSend(self, sData):
        '''Sends a EventSlave a message using the fSend function.'''
        fSend(sData, self.sClientIPAdress, self.iClientPort)

class cEventSlave():
    '''Connects to an EventMaster, gets handed a port to listen to,
    listens to that port for new events and executes those events.'''
    def __init__(self, sServerIP, iServerPort):
        self.iClientPort = int(fsSendAndReceives("Register_Player",
                                                 sServerIP, iServerPort))
    def msRequestEvent(self):
        '''Listens in on the receiving socket,
        and returns any events thats given to it.'''
        sData = fReceive(self.iClientPort)
#DEFINES VARIABLES AND OBJECTS
#QUITS IF THIS FILE IS RUN AS A SCRIPT
if __name__ == "__main__":
    if input("Server or Client?") == "s":
        oConnection = cEventMaster(8000, 9001)
        oConnection.mSend("EVENT_TEST")
    else:
        oConnection = cEventSlave(sServerIP="127.0.0.1", iServerPort=8000)
        exec(oConnection.msRequestEvent())
