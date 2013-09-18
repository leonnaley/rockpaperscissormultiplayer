#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''DOCUMENTATION
    DEBUGGING
        If you want to debug this program, just append -debug as the parameters
        when running this program, the erro will be printed and you will find
        yourself in interactive mode at where the error occurred.
    LOGGING
        Logging in this program uses the builtin python system.
        Whenever you want to use logging, logging.debug("This text will be
        logged)

        You can change the it from the debug level to something more severe
        if you would like, anything from the level ERROR or worse will be
        logged automatically.

        Remember to  run this program with the parameter -log
        to turn on logging.

        To log to a file, add: filename='log.txt' as parameters
        into the basicconfig line in the logging part of this file
    UNITTESTING
        Unittesting is strongly encouraged and is implemented by the
        standard python library unittest, but also helped by a custom input
        function for those functions that require a keyboard input.

        Do not remove any "old" unit tests unless you know what you are doing.

        all unit tests are located in the unittests.py
        This file will be split up to test all the modules in its folder.
    NAMING OF FUNCTIONS, VARIABLES, OBJECTS, ETC...
        The naming system used is CamelBack, so every word for variables and
        whatnot starts with a capital letter to make reading easier.

        Every variable/object/classes/etc.. are also prefixed with one or more
        lowercase identifiers so you can easily determine the type.
        Examples: iMyInteger, sMyString

        If the type is a container (lists/tuples/sets/etc..)
        the first letter will determine the container type and the second one
        will determine what type it holds.
        Examples: liMyListOfIntegers, tfMyTupleOfFloats

        If the type is a function or method that returns something.
        the first letter will determine if it's a function or a method and
        the second one will determine what type it holds.
        Examples: fiMyFunctionReturnsAnInteger, mfMyMethodReturnsAFloat

        if there are functions returning containers or containers containing
        containers use common sense for when to stop prefixing.

        COMMON PREFIXES
            b       = boolean
            c       = class
            d       = dictionary
            i       = integer/bytes/floats
            o       = object
            ofile   = fileobject (a file)
            s       = string
            x       = unknown type or the type changes from time to time.
        CONTAINER PREFIXES
            l       = list
            t       = tuples
            z       = sets
        FUNCTION/METHODS PREFIXES
            f       = functions
            m       = methods'''

#IMPORTS AND SETS UP MODULES
from __future__ import print_function  # For compability with python2
import logging
import sys

#HANDLES COMPATIBILITY FOR PYTHON2
if sys.version_info[0] == 2:
    input = raw_input

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES FUNCTIONS
def fStartDebugger(type, value, tb):
    '''Prints the last exception message and starts the debugger. '''
    #Prints the last exception message
    traceback.print_exception(type, value, tb)

    #Starts the debugger
    pdb.post_mortem(tb)


def fxInput(Text=""):
    '''Returns input from the fxInput list '''
    fxInput.iInputExecuteCount += 1
    if (len(fxInput.lWantedInput) < fxInput.iInputExecuteCount
       or fxInput.lWantedInput[fxInput.iInputExecuteCount-1] == "Blank"):
        raise ValueError("The program demands atleast "
                         + str(len(fxInput.lWantedInput)+1) + " inputs")
    return fxInput.lWantedInput[fxInput.iInputExecuteCount-1]


def fSetInput(lxWantedInput):
    '''Sets the input the fxInput Function have to provide.
    The parameters passed to this function must be in the form of a list
    with every input you want to set in correct order.'''
    fxInput.lWantedInput = lxWantedInput
    fxInput.iInputExecuteCount = 0


#DEFINES EXCEPTIONS/CLASSES
#QUITS IF THIS FILE IS RUN AS A SCRIPT
if __name__ == "__main__":
    logging.critical('This is a library not a script, exiting')
    exit(1)

#HANDLES lOGGING
if "-log" in sys.argv:
    logging.basicConfig(level=logging.DEBUG,
                        format="%(levelname)s: %(message)s")
else:
    logging.basicConfig(level=logging.ERROR,
                        format="%(levelname)s: %(message)s")

#HANDLES DEBUGGING
if "-debug" in sys.argv:
    import pdb
    import traceback
    sys.excepthook = fStartDebugger
