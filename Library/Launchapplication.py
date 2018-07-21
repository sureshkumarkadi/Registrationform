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

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

import os
import sys

#Getting current working folder
dir_path = os.path.dirname(os.path.realpath(__file__))

#Getting parent of current working folder
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

#Navigating to the desired folder
sys.path.insert(0,folder_path+"\Syslibrary")

#Imoprting module from Syslibrary
from datadriver import readjson

#Creating class object and instance of that object
jsonread1 = readjson()

class launchapplication():
    def intializebrowser(self):
        #from instance object calling function 'jsonread'
        env = jsonread1.jsonread(folder_path+'\Env\setup.json')
        if env['browser']  == 'chrome':
            # Intializing chrome browser
            browser = webdriver.Chrome(folder_path+'\Env\chromedriver.exe')
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'firefox':
            # Intializing firefox browser
            browser = webdriver.Firefox(executable_path=folder_path+'\Env\geckodriver.exe')
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser

        elif env['browser'] =='headlessChrome':
            # Intializing headless chrome browser
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_driver = folder_path+'\Env\chromedriver.exe'
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
            browser.implicitly_wait(10)
            return browser

    def closebrower(self,browser):
        browser.close()

    def inputurl(self,browser):
        url = jsonread1.jsonread(folder_path+'\Env\setup.json')
        if url['url']  == 'prestagurl':
            prestagurl = jsonread1.jsonread(folder_path+'\Env\setup.json')
            browser.get(prestagurl['prestagurl'])

        elif url['url']  == 'stagurl':
            stagurl = jsonread1.jsonread(folder_path+'\Env\setup.json')
            browser.get(stagurl['stagurl'])

    def registrationform_locators(self):
        registrationform_locator = jsonread1.jsonread(folder_path+'\Object\locators.json')
        return registrationform_locator

    def registrationform_testdata(self):
        registrationform_testdata = jsonread1.jsonread(folder_path+'\Data\Testdata.json')
        return registrationform_testdata

    def registrationform_firstname(self,browser,registrationform_locator):
        firstname = browser.find_element_by_xpath(registrationform_locator['firstname'])
        return firstname

    def registrationform_lastname(self,browser,registrationform_locators):
        lastname = browser.find_element_by_xpath(registrationform_locators['lastname'])
        return lastname

    def registrationform_dropdown(self,browser,registrationform_locators):
        dropdownselect = Select(browser.find_element_by_xpath(registrationform_locators['dropdownselect']))
        return dropdownselect

    def registrationform_username(self,browser,registrationform_locators):
        username = browser.find_element_by_xpath(registrationform_locators['username'])
        return username

    def registrationform_password(self,browser,registrationform_locators):
        password = browser.find_element_by_xpath(registrationform_locators['password'])
        return password

    def registrationform_confirmpassword(self,browser,registrationform_locators):
        confirmpassword = browser.find_element_by_xpath(registrationform_locators['confirmpassword'])
        return confirmpassword

    def registrationform_email(self,browser,registrationform_locators):
        email = browser.find_element_by_xpath(registrationform_locators['email'])
        return email

    def registrationform_contactno(self,browser,registrationform_locators):
        contactno = browser.find_element_by_xpath(registrationform_locators['contactno'])
        return contactno

    def registrationform_submit(self,browser,registrationform_locators):
        submit = browser.find_element_by_xpath(registrationform_locators['submit'])
        return submit










