#!/usr/bin/env python
# coding=utf-8
#This module is made to be both runnable in python2.x and 3.x

'''DOCUMENTATION
    VERSION SYSTEM
        This program has a major revision and a minor revision.
        Version 2.2 has a major revision of 1, and a minor revision of 2.

        This program has unit tests which will demonstrate the uses of the
        functions/objects and classed found within this program.

        Whatever unit tests are present in the documentation part of this
        program will always be made sure to work on all later minor revisions.

        Whenever there's a major revision this will not necessarily
        hold true though.

    LOGGING
        Logging in this program uses the builtin python system.
        Whenever you want to use logging, use the log function like this:
        log("This Text will get logged", and this text also.")

        Remember to also turn on logging in the "logging" section or run this
        program with the parameter -log.

    NAMING OF FUNCTIONS, VARIABLES, OBJECTS, ETC...
        The naming system used is CamelBack, so every word for variables and
        whatnot starts with a capital letter to make reading easier.

        Every variable/object/classes/etc.. are also prefixed with one or more
        lowercase identifiers so you can easily determine the type.
        Examples: iMyInteger, sMyString,
                  liMyListOfIntegers, fiMyIntegerReturningFunction

        Any list/tuple/set/etc.. will be prefixed, and what types they hold
        inside also gets prefixed.
        Examples: liMyListOfIntegers,  tbMyTupleOfBooleans

        Any function or method which returns a variable/list/etc.. will be
        prefixed with the type, and then what types they return.
        Examples: fiMyFunction , mbMyMethod¸fliMyListOfIntegersReturningFunction

        COMMON PREFIXES
            b       = boolean
            c       = class
            d       = dictionary
            i       = integer/bytes/floats
            l       = list
            m       = method
            o       = object
            ofile   = fileobject (a file)
            s       = string
            t       = tuples

        GTK RELATED PREFIXES
            bu      = button
            w       = window
            co      = container
            la      = label

        PYGAME RELATED PREFIXES
            su      = surface (related to pygame)
            go      = group of objects (related to pygame)

    THINGS THAT NEEDS IMPROVING/IMPLEMENTATION IN THIS PROGRAM
        ...

    UNIT TESTING
        Unit tests are embedded into doclines. The unit tests embedded into
        this particular docline are divided into versions of this program.

        So you can guarantee backwards compability and forwards compability
        with any minor revisions, because when you make a new minor revision
        of this program, you do not remove any "old" unit tests, you simply
        append new ones, so you know that your new code will be compatible
        with your old code.

        To make a new unit test, just paste the next line and erase/change
        any parameters you want into the unit test
        &&& sCommandToTest='1+1', lCommandInput=[], ExpectedOutput=2,
            lExpressionsToTest=['True'] &&&

        or the shortened
        &&& '1+input()', [2], 3, ['True'] &&&

        When you want to run the unit tests, just run the unittesting
        module with your module name as a parameter.

    UNIT TESTS:
        VERSION 0.1

    '''

#MAKES THE PRINT FUNCTION IN PYTHON2 WORK AS THE ONE FROM PYTHON3
from __future__ import print_function

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"
__version_info__ = ["Alpha Version", "0", "1"]
__version__ = '.'.join(__version_info__[1:])

#IMPORTS AND SETS UP MODULES
import sys
import debug  # Remember to delete this line                                   ###
import socket

#MAKES THE INPUT FUNCTION IN PYTHON2 WORK AS THE ONE FROM PYTHON3
if sys.version_info[0] == 2:
    input = raw_input

#HANDLES LOGGING
if "-log" in sys.argv:
    import logging

    #To log to a file, add: filemode="w", filename='log.txt' as parameters
    #   into the next line (inside the basicconfig function)
    logging.basicConfig(level=logging.DEBUG, format='Log: %(message)s')

    def log(*Parameters):
        '''Takes all the parameters, converts them to a single string,
        and sends them to logging.debug'''
        lsParameters = []

        #Convert every parameter to a string, and appends it to a list
        for Parameter in Parameters:
            lsParameters.append(str(Parameter))

        #Converts the list to a string
        sOutput = "".join(lsParameters)

        #Logs the concatenated list
        logging.debug(sOutput)
else:
    def log(*parameters):
        '''Dummy log function'''


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

#RUNS THE MAIN PROGRAM
if __name__ == "__main__":
    log("Running ", __file__, " as a script")
    print("this module is not meant to be runned as a script, exiting")
    exit(1)
