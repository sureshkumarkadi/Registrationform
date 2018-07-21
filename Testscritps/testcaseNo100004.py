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
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Library")



from datadriver import readjson
jsonread1 = readjson()

from Launchapplication import launchapplication
application = launchapplication()

tf = 'test_TestcaseNo100004'

#Test case No : 100004
class TestcaseNo100004(unittest.TestCase):
    def test_TestcaseNo100004(self) :
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            registrationform_locator = application.registrationform_locators()

            placeholder_firstname = browser.find_element_by_xpath(registrationform_locator['placeholder_firstname'])
            placeholder_lastname = browser.find_element_by_xpath(registrationform_locator['placeholder_lastname'])
            placeholder_username = browser.find_element_by_xpath(registrationform_locator['placeholder_username'])
            placeholder_password = browser.find_element_by_xpath(registrationform_locator['placeholder_password'])
            placeholder_confirmpassword = browser.find_element_by_xpath(registrationform_locator['placeholder_confirmpassword'])
            placeholder_email = browser.find_element_by_xpath(registrationform_locator['placeholder_email'])
            placeholder_contactno = browser.find_element_by_xpath(registrationform_locator['placeholder_contactno'])

            self.assertEqual(placeholder_firstname.get_attribute('placeholder'),'First Name')
            self.assertEqual(placeholder_lastname.get_attribute('placeholder'),'Last Name')
            self.assertEqual(placeholder_username.get_attribute('placeholder'),'Username')
            self.assertEqual(placeholder_password.get_attribute('placeholder'),'Password')
            self.assertEqual(placeholder_confirmpassword.get_attribute('placeholder'),'Confirm Password')
            self.assertEqual(placeholder_email.get_attribute('placeholder'),'E-Mail Address')
            self.assertEqual(placeholder_contactno.get_attribute('placeholder'),'(+91)')

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No : 100004 is failed")
        finally:
            application.closebrower(browser)

if __name__ == '__main__':
    unittest.main()

