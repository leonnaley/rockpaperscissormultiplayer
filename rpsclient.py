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
import sys
import time

#HANDLES COMPATIBILITY FOR PYTHON2
if sys.version_info[0] == 2:
    input = raw_input

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES WRAPPER FUNCTIONS
#DEFINES FUNCTIONS
def fbRegisterPlayer(sName, sHostIP, sPort):
    '''Registers a player against the server.'''
    sData = "EVENT_RegisterNewPlayer " + sName

    #Sends a request to the server to be registered
    sDataReceived = libnet.fsSendAndReceive(sData, sIpAdress, sPort)

    #Receives a message from the server,
    #   returns if it's a confirmation from the server
    if sDataReceived == "Player Registered":
        return()
    else:
        logging.CRITICAL("The server can't register the player, quitting")
        exit(1)


def ftsWelcomePlayer():
    '''Welcomes the player with a welcome screen,
    and asks for name and hostname of the server'''
    print("\n")
    print("Welcome to the Rock, Paper, Scissor Multiplayer game!")
    sName = input("Please input your name: ")
    sHost = input("Please input the servers hostname")
    sPort = input("Please input the severs portnumber")
    return(sName, sHost, sPort)


def fEVENT_Wait():
    '''Waits 1 second before resuming operation'''
    time.sleep(1)


def fEVENT_Quit():
    '''Displays a goodbye screen and quits the game'''
    print("\n"*40)
    print("The Game has ended, Thank you for playing")
    exit(0)


def fsReceiveEvent(sName, sIpAdress, sPort):
    '''Connects to a server, identifies itself and receives an event from
    that server which it returns'''
    sData = "EVENT_RequestEvent " + sName

    #Sends a request to the server to be registered
    sDataReceived = libnet.fsSendAndReceive(sData, sIpAdress, sPort)

    #Receives a message from the server,
    #   returns if it's a confirmation from the server
    return(sDataReceived)


def fEventHandler(sEvent):
    '''Runs the appropriate functions according to what events
    it has received.'''
    dEvents = {"EVENT_Quit": fEvent_Quit,
               "EVENT_Wait": fEvent_Wait}

    fEvent = dEvents[sEvent]

    fEvent()

#DEFINES PROCEDURES
#DEFINES EXCEPTIONS/CLASSES
#DEFINES VARIABLES AND OBJECTS
slastEvent = ""
#STARTS THE CLIENT
if __name__ == "__main__":
    #Opens up a welcome screen and registers the player to the server
    sName, sHost = ftsWelcomePlayer("Welcome_Player")
    sHostIP = libnet.fHostNameToIPAdress(sHost)
    fbRegisterPlayer(sName, sHostIP, sPort)

    #Receive and perform all events from the connected server,
    #   until the connected server disconnects
    while True:
        while True:
            sEvent = fsReceiveEvent(sName, sHostIP, sPort)
            if sEvent != sLastEvent:
                break
            else:
                time.sleep(1)
        fEventHandler(sEvent)
