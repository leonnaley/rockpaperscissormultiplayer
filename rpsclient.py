#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
from __future__ import print_function  # For compability with python2
import libcommon  # Helps with debugging, logging and documentation
import libnet
import logging
import random
import socket
import sys
import time

#HANDLES COMPATIBILITY FOR PYTHON2
if sys.version_info[0] == 2:
    input = raw_input

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES WRAPPER FUNCTIONS
#DEFINES EVENT FUNCTIONS
def fRegisterPlayer():
    '''Registers a player against the server, returns True if succesful'''
    libnet.fSend("Player_Register " + sUniqueID + " " + sPlayerName,
                 socket.gethostbyname(sServerHostName))
    pass

def fWelcome_Player():
    '''Welcomes the player with a welcome screen,
    and asks for name and hostname of the server'''
    pass

def fQuit():
    '''Displays a goodbye screen and quits the game'''
    pass

#DEFINES FUNCTIONS
def fClearScreen():
    '''Prints 40 blank lines, effectively clearing the terminal screen'''
    print("\n"*40)

def fsReceiveEvent(sHostName, iPort):
    '''Connects to a server, identifies itself and receives an event from
    that server which it returns'''
    pass

def fEventHandler(sEvent):
    '''Connects to the server and receives a string of characters from it,
    which determines what screen this client should display'''
    d = {"Register_Player": fRegisterPlayer,
         "Receive_Results": fReceiveResults,
         "Receive_Choices": fReceiveChoices,
         "Welcome_Player": fWelcomePlayer,
         "Quit": fQuit}

    d[sDataReceived.split()[0]](sDataReceived)


#DEFINES PROCEDURES
#DEFINES EXCEPTIONS/CLASSES
#DEFINES VARIABLES AND OBJECTS
sUniqueID = str(random.randrange(1000000, 9999999))

#STARTS THE CLIENT
if __name__ == "__main__":
    #Tells the eventhandler to open up the welcome screen
    fEventHandler("Welcome_Player")

    #Tells the eventhandler to register the player against the server
    fEventHandler("Register_Player")

    #Receive and perform all events from the connected server,
    #   until the connected server disconnects
    while True:
        sEvent = fReceiveEvent()
        fEventHandler(sEvent)
