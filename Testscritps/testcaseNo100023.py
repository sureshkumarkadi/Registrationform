#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     13-07-2018
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

tf = 'test_TestcaseNo100023'

#Test case No : 100023
class TestcaseNo100023(unittest.TestCase):
    def test_TestcaseNo100023(self) :
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            registrationform_locator = application.registrationform_locators()
            registrationform_testdata = application.registrationform_testdata()

            password = application.registrationform_password(browser,registrationform_locator)
            password.send_keys(registrationform_testdata['password_lessthan8characterlimit'])

            validationmessage_firstname = browser.find_element_by_xpath(registrationform_locator['failure_image'])
            if validationmessage_firstname.is_displayed():
                print('pass')
            else:
                self.fail("Test case No : 100023 is failed")
            time.sleep(2)

            validationmessage_invalidinput = browser.find_elements_by_xpath(registrationform_locator['validationmessage_invalidinput'])

            self.assertEqual(validationmessage_invalidinput[3].text,'This value is not valid')

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No : 100023 is failed")
        finally:
            application.closebrower(browser)

if __name__ == '__main__':
    unittest.main()

