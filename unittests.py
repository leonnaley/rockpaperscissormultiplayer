#!/usr/bin/env python
# coding=utf-8
#This module is runnable with python2.x and python3.x
'''For documentation, read the doclines in libcommon'''

#IMPORTS AND SETS UP MODULES
import libcommon  # Helps with debugging and logging
import logging
import unittest

#GENERAL INFORMATION
__author__ = "Leon Naley"
__copyright__ = "Copyright (c) 2013 Leon Naley"

#DEFINES WRAPPER FUNCTIONS
#DEFINES FUNCTIONS
#DEFINES PROCEDURES
#DEFINES EXCEPTIONS/CLASSES
class libcommonTests(unittest.TestCase):
    '''This class will contain all unit tests for this file.'''
    def test_placeholder_example(self):
        self.assertEqual(1, 1)

#DEFINES VARIABLES AND OBJECTS
#QUITS IF THIS FILE IS RUN AS A SCRIPT
if __name__ == "__main__":
    #Runs through all unit tests in this file
    unittest.main()