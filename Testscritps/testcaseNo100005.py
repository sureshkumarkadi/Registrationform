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
import unittest
import os
import sys
import traceback

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Library")



from datadriver import readjson
jsonread1 = readjson()

from Launchapplication import launchapplication
application = launchapplication()

tf = 'test_TestcaseNo100005'

#Test case No : 100005
class TestcaseNo100005(unittest.TestCase):
    def test_TestcaseNo100005(self) :
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            registrationform_locator = application.registrationform_locators()
            registrationform= browser.find_elements_by_xpath(registrationform_locator['Regformfileds'])

            self.assertEqual(registrationform[3].text,'Username *')
            self.assertEqual(registrationform[4].text,'Password *')
            self.assertEqual(registrationform[0].text,'First Name *')
            self.assertEqual(registrationform[1].text,'Last Name *')
            self.assertEqual(registrationform[5].text,'Confirm Password *')
            self.assertEqual(registrationform[6].text,'E-Mail *')

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No : 100005 is failed")
        finally:
            application.closebrower(browser)

if __name__ == '__main__':
    unittest.main()

