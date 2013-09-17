#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
from __future__ import print_function  # For compability with python2
import libcommon  # Helps with debugging, logging, documentation and unittesting
import logging
import unittest
import sys

#HANDLES COMPATIBILITY FOR PYTHON2
if sys.version_info[0] == 2:
    input = raw_input

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"


#DEFINES WRAPPER FUNCTIONS
#DEFINES FUNCTIONS
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
