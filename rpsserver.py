#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
from __future__ import print_function  # For compability with python2
import libcommon  # Helps with debugging, logging and documentation
import libnet
import logging
import sys

#HANDLES COMPATIBILITY FOR PYTHON2
if sys.version_info[0] == 2:
    input = raw_input

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES WRAPPER FUNCTIONS
#DEFINES FUNCTIONS
def fTransmitToAll(sData, ddPlayers):
    '''Transmit a data stream to all players.'''
    lsPlayerIDs = ddPlayers.keys()
    #Loops until all players have received the data
    while lsPlayerIDs != []:
        sData = libnet.fsReceiveAndSend(iPort, sData)
        sEvent, sPlayerID = sData.split()
        if sPlayerID in lsPlayerIDs:
            lsPlayerIDs.remove(sPlayerID)

#DEFINES PROCEDURES
#DEFINES EXCEPTIONS/CLASSES
#DEFINES VARIABLES AND OBJECTS
iPort = 8000
ddPlayers = {}
sHostName = socket.gethostname()

#STARTS THE SERVER
if __name__ == "__main__":
    #Displays welcome screen and sets iPlayerCount
    print("\n"*40)
    print("Welcome to the Rock, Paper, Scissors Server")
    iPlayerCount = input("How Many players will there be?")

    #Displays screen
    print("\n")
    print("The players are now free to connect to", sHostName)
    print("Good luck :)")

    #Receive and Register all clients and their info in a list of dictionaries
    while iPlayerCount != 0:
        sData = libnet.fsReceiveAndSend(iPort)
        sEvent, sPlayerID = sData.split()
        if sEvent == "EVENT_RegisterNewPlayer":
            ddPlayers.update({sPlayerID:"Active"}
            iPlayerCount -= 1
        else:
            logging.ERROR("A client is sending the wrong data to the server")

    #Loop until the game has been won
    bGameWon = False
    while bGameWon == False:
        #   #Transmit score to all players
        fTransmitToAll("EVENT_Scores")
        pass
        #Make all players active
        for sPlayerID in ddPlayers.keys():
            ddPlayers[sPlayerID] = "Active"
        #Loop until only one player remains active (the round has been won)
        while "Active" in ddPlayers.values():
            #Request choices from all active players
            libnet.fTransmitToAll("EVENT_SendChoice")
            #Set all losing players to inactive

            #Transmit choices to all players

        #Reward the only player that's active with a point
    #Transmit score and the end of the game for all players, then exit

    exit(0)
