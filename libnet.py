#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
from __future__ import print_function  # For compability with python2
import libcommon  # Helps with debugging, logging, documentation and unittesting
import logging
import unittest
import socket
import sys

#HANDLES COMPATIBILITY FOR PYTHON2
if sys.version_info[0] == 2:
    input = raw_input

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES WRAPPER FUNCTIONS
#DEFINES FUNCTIONS
def fSend(sData, sIpAdress, iPort=8000):
    '''Sends a string of characters to an ip adress.'''
    #Creates a socket object
    oSock = oSocket.oSocket(oSocket.AF_INET, oSocket.SOCK_STREAM)

    #Figures out the ip adress (if the client is on the same server,
    #   set it to 127.0.0.1)
    sIpAdress = oSocket.gethostbyname(sHostName)
    if sIpAdress.startswith("127"):
        sIpAdress = "127.0.0.1"

    #Tries to connect to the listening server
    while True:
        try:
            oSock.connect((sIpAdress, iPort))
        except:
            time.sleep(0.5)
        else:
            #Sends the string of characters on the socket
            oSock.send(sData)
            break

    #Closes and deletes the socket to free up the port used
    oSock.close()
    del oSock


def fsReceive(iPort=8000):
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
#DEFINES EXCEPTIONS/CLASSES/UNITTESTS
class unittests(unittest.TestCase):
    '''This class will contain all unit tests for this file.'''
    def test_placeholder_example(self):
        libcommon.fSetInput(["test"])
        self.assertEqual("test", input())

#HANDLES UNITTESTING
if "-test" in sys.argv:
    sys.argv = [sys.argv[0]]
    input = libcommon.fxInput
    unittest.main()

#DEFINES VARIABLES AND OBJECTS
#QUITS IF THIS FILE IS RUN AS A SCRIPT
if __name__ == "__main__":
    logging.critical('This is a library not a script, exiting')
    exit(1)
