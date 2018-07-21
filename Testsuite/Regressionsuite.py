#-------------------------------------------------------------------------------
# Name:        Registration Form
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     21-07-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys
import unittest


dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Testscritps")

from HTMLTestRunner import HTMLTestRunner

#importing individual test scripts
#Note :Reason for making individual test scripts - As per standard framework guidelines - Each test script should be independent one

from testcaseNo100001 import TestcaseNo100001
from testcaseNo100003 import TestcaseNo100003
from testcaseNo100004 import TestcaseNo100004
from testcaseNo100005 import TestcaseNo100005
from testcaseNo100006 import TestcaseNo100006
from testcaseNo100007 import TestcaseNo100007
from testcaseNo100008 import TestcaseNo100008

from testcaseNo100009 import TestcaseNo100009
from testcaseNo100010 import TestcaseNo100010
from testcaseNo100011 import TestcaseNo100011
from testcaseNo100012 import TestcaseNo100012
from testcaseNo100013 import TestcaseNo100013
from testcaseNo100014 import TestcaseNo100014

from testcaseNo100015 import TestcaseNo100015
from testcaseNo100016 import TestcaseNo100016
from testcaseNo100017 import TestcaseNo100017
from testcaseNo100018 import TestcaseNo100018
from testcaseNo100019 import TestcaseNo100019
from testcaseNo100020 import TestcaseNo100020

from testcaseNo100021 import TestcaseNo100021
from testcaseNo100022 import TestcaseNo100022
from testcaseNo100023 import TestcaseNo100023
from testcaseNo100024 import TestcaseNo100024
from testcaseNo100025 import TestcaseNo100025
from testcaseNo100026 import TestcaseNo100026
from testcaseNo100027 import TestcaseNo100027
from testcaseNo100028 import TestcaseNo100028
from testcaseNo100029 import TestcaseNo100029
from testcaseNo100030 import TestcaseNo100030

from testcaseNo100031 import TestcaseNo100031
from testcaseNo100032 import TestcaseNo100032
from testcaseNo100034 import TestcaseNo100034
from testcaseNo100035 import TestcaseNo100035
from testcaseNo100036 import TestcaseNo100036
from testcaseNo100037 import TestcaseNo100037
from testcaseNo100038 import TestcaseNo100038

from testcaseNo100040 import TestcaseNo100040

suite = unittest.TestSuite()
#Collecting as a suite

suite.addTest(TestcaseNo100001('test_TestcaseNo100001'))
suite.addTest(TestcaseNo100003('test_TestcaseNo100003'))
suite.addTest(TestcaseNo100004('test_TestcaseNo100004'))
suite.addTest(TestcaseNo100005('test_TestcaseNo100005'))
suite.addTest(TestcaseNo100006('test_TestcaseNo100006'))
suite.addTest(TestcaseNo100007('test_TestcaseNo100007'))

suite.addTest(TestcaseNo100008('test_TestcaseNo100008'))
suite.addTest(TestcaseNo100009('test_TestcaseNo100009'))
suite.addTest(TestcaseNo100010('test_TestcaseNo100010'))
suite.addTest(TestcaseNo100011('test_TestcaseNo100011'))
suite.addTest(TestcaseNo100012('test_TestcaseNo100012'))
suite.addTest(TestcaseNo100013('test_TestcaseNo100013'))

suite.addTest(TestcaseNo100014('test_TestcaseNo100014'))
suite.addTest(TestcaseNo100015('test_TestcaseNo100015'))
suite.addTest(TestcaseNo100016('test_TestcaseNo100016'))
suite.addTest(TestcaseNo100017('test_TestcaseNo100017'))
suite.addTest(TestcaseNo100018('test_TestcaseNo100018'))
suite.addTest(TestcaseNo100019('test_TestcaseNo100019'))

suite.addTest(TestcaseNo100020('test_TestcaseNo100020'))
suite.addTest(TestcaseNo100021('test_TestcaseNo100021'))
suite.addTest(TestcaseNo100022('test_TestcaseNo100022'))
suite.addTest(TestcaseNo100024('test_TestcaseNo100024'))
suite.addTest(TestcaseNo100025('test_TestcaseNo100025'))
suite.addTest(TestcaseNo100026('test_TestcaseNo100026'))

suite.addTest(TestcaseNo100027('test_TestcaseNo100027'))
suite.addTest(TestcaseNo100028('test_TestcaseNo100028'))
suite.addTest(TestcaseNo100029('test_TestcaseNo100029'))
suite.addTest(TestcaseNo100030('test_TestcaseNo100030'))
suite.addTest(TestcaseNo100031('test_TestcaseNo100031'))
suite.addTest(TestcaseNo100032('test_TestcaseNo100032'))

suite.addTest(TestcaseNo100034('test_TestcaseNo100034'))
suite.addTest(TestcaseNo100035('test_TestcaseNo100035'))
suite.addTest(TestcaseNo100036('test_TestcaseNo100036'))
suite.addTest(TestcaseNo100037('test_TestcaseNo100037'))
suite.addTest(TestcaseNo100038('test_TestcaseNo100038'))
suite.addTest(TestcaseNo100040('test_TestcaseNo100040'))

outfile = file(folder_path+'\Regressionreport\Regressionreport.html','w+')

runner = HTMLTestRunner(stream=outfile,verbosity=1, title='DeltaX', description='Regressionreport',dirTestScreenshots=folder_path+'\Screenshots')

runner.run(suite)

outfile.close()




