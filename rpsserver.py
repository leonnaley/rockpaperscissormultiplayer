#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
from __future__ import print_function  # For compability with python2
import libcommon  # Helps with debugging, logging and documentation
import libnet
import logging
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
#DEFINES FUNCTIONS
#DEFINES PROCEDURES
#DEFINES EXCEPTIONS/CLASSES
#DEFINES VARIABLES AND OBJECTS
sHostName = socket.gethostname()
lPlayers = []

#STARTS THE SERVER
if __name__ == "__main__":
    #Displays hostname and lets the administrator know that the players
    #   are now free to connect
    print("The players are now free to connect to", sHostName)
    print("Good luck :)")

    #Receive and Register all clients and their info in a list of dictionaries

    #Loop until the game has been won
        #Transmit score to all players
        #Make all players active
        #Loop until only one player remains active (the round has been won)
            #Request choices from all active players
            #Set all losing players to inactive
            #Transmit choices to all players
        #Reward the only player that's active with a point
    #Transmit score and the end of the game for all players, then exit

    exit(0)
