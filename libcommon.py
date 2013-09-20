#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x

#IMPORTS AND SETS UP MODULES
import sys
import logging

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
