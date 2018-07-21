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

tf = 'test_TestcaseNo100009'

#Test case No : 100009
class TestcaseNo100009(unittest.TestCase):
    def test_TestcaseNo100009(self) :
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            registrationform_locator = application.registrationform_locators()
            registrationform_testdata = application.registrationform_testdata()

            firstname = application.registrationform_firstname(browser,registrationform_locator)
            firstname.send_keys(registrationform_testdata['firstname'])

            lastname = application.registrationform_lastname(browser,registrationform_locator)
            lastname.send_keys(registrationform_testdata['lastname'])

            username = application.registrationform_username(browser,registrationform_locator)
            username.send_keys(registrationform_testdata['username'])

            dropdownselect = application.registrationform_dropdown(browser,registrationform_locator)
            dropdownselect.select_by_visible_text(registrationform_testdata['department_engineering'])

            password = application.registrationform_password(browser,registrationform_locator)
            password.send_keys(registrationform_testdata['password_12characterlimit'])

            confirmpassword = application.registrationform_confirmpassword(browser,registrationform_locator)
            confirmpassword.send_keys(registrationform_testdata['confirmpassword_12characterlimit'])

            email = application.registrationform_email(browser,registrationform_locator)
            email.send_keys(registrationform_testdata['valid_email'])

            contactno = application.registrationform_contactno(browser,registrationform_locator)
            contactno.send_keys(registrationform_testdata['valid_contactno'])

            submit = application.registrationform_submit(browser,registrationform_locator)
            submit.click()

            submission_failuremessage = browser.find_element_by_xpath(registrationform_locator['submission_failuremessage'])
            if submission_failuremessage.is_displayed():
                print('pass')
            else:
                self.fail("Test case No : 100009 is failed")

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No : 100009 is failed")
        finally:
            application.closebrower(browser)

if __name__ == '__main__':
    unittest.main()

