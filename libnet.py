#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
import libcommon  # Helps with debugging and logging
import logging
import socket

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES WRAPPER FUNCTIONS
#DEFINES FUNCTIONS
def fHostNameToIpAdress(sHostName):
    '''Returns the ip adress of the given hostname'''
    sIPAdress = socket.gethostbyname(sHostName)[0]
    if sIPAdress.startswith("127"):
        sIPAdress = "127.0.0.1"
    return(sIPAdress)


def fIpAdressToHostName(sIPAdress):
    '''Returns the hostname of the given ip adress'''
    return(socket(gethostbyaddress(sIPAdress)[0]))


def fsSendAndReceive(sData, sIpAdress, sPort="8000"):
    '''Sends a string to an ip adress through a socket,
    then receives and returns a string from that ip adress'''
    iPort = int(sPort)

    #Creates a socket object
    oSock = oSocket.oSocket(oSocket.AF_INET, oSocket.SOCK_STREAM)

    #Tries to connect to the listening server
    while True:
        try:
            oSock.connect((sIpAdress, iPort))
        except:
            time.sleep(0.5)
        else:
            #Sends the string of characters on the socket
            oSock.send(sData)
            sReceivedData = oSock.recv(1024)
            break

    #Closes and deletes the socket to free up the port used
    oSock.close()
    del oSock
    return(sReceivedData)


def fsReceiveAndSend(sData="", sPort="8000"):
    iPort = int(sPort)

    #Creates a socket object
    oSock = oSocket.oSocket(oSocket.AF_INET, oSocket.SOCK_STREAM)

    #Binds the socket object to an ip adress and port and starts listening
    #   in on the socket
    oSock.bind(("127.0.0.1", iPort))
    oSock.listen(1)

    #Receives a socket and an ip adress from the sender
    oOutgoing, addr = oSock.accept()

    #Listen in on the receiversocket for up to 1024 bytes of data
    sData = oOutgoing.recv(1024)

    #Closes and deletes all sockets to free up ports
    oOutgoing.close()
    oSock.close()
    del oSock
    del oOutgoing

    #returns the data from the sender and the ip adress of the sender
    return(sData, addr)


#DEFINES PROCEDURES
#DEFINES EXCEPTIONS/CLASSES
#DEFINES VARIABLES AND OBJECTS
#QUITS IF THIS FILE IS RUN AS A SCRIPT
if __name__ == "__main__":
    logging.critical('This is a library not a script, exiting')
    exit(1)
