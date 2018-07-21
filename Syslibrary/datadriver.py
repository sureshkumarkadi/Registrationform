#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     21-07-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
import unittest

class readjson():
    def jsonread(self,filename):         # run time will provide the filepath
        with open(filename) as jsonfile: # opens the json object
            value = json.load(jsonfile)  # converts json object into python object
            return value                 # returns value




