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
from selenium.webdriver.common.keys import Keys

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Library")



from datadriver import readjson
jsonread1 = readjson()

from Launchapplication import launchapplication
application = launchapplication()

tf = 'test_TestcaseNo100006'

#Test case No : 100006
class TestcaseNo100006(unittest.TestCase):
    def test_TestcaseNo100006(self) :
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            registrationform_locator = application.registrationform_locators()
            registrationform_testdata = application.registrationform_testdata()

            firstname = application.registrationform_firstname(browser,registrationform_locator)
            firstname.send_keys(registrationform_testdata['firstname'])

            lastname = application.registrationform_lastname(browser,registrationform_locator)
            lastname.send_keys(registrationform_testdata['lastname'])

            submit = application.registrationform_submit(browser,registrationform_locator)
            submit.click()

            validationmessage_username = browser.find_element_by_xpath(registrationform_locator['validationmessage_username'])
            validationmessage_password = browser.find_element_by_xpath(registrationform_locator['validationmessage_password'])
            validationmessage_confirmpassword = browser.find_element_by_xpath(registrationform_locator['validationmessage_confirmpassword'])
            validationmessage_email = browser.find_element_by_xpath(registrationform_locator['validationmessage_email'])

            self.assertEqual(validationmessage_username.text,'Please enter your Username')
            self.assertEqual(validationmessage_password.text,'Please enter your Password')
            self.assertEqual(validationmessage_confirmpassword.text,'Please confirm your Password')
            self.assertEqual(validationmessage_email.text,'Please enter your Email Address')

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No : 100006 is failed")
        finally:
            application.closebrower(browser)

if __name__ == '__main__':
    unittest.main()

