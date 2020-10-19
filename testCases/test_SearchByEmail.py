import pytest
from selenium import  webdriver
from pageObjects.LoginPage import *
from utilities.readProperties import *
from utilities.customLogger import *
from pageObjects.AddCustomerPage import *
from pageObjects.searchCustomerPage import *
import string
import random
import time

class Test_004_SearchCustomerEmail:
    baseURL= ReadConfig.getApplicationURL()
    user=ReadConfig.getUser()
    passw=ReadConfig.getPassw()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerEmail(self, setup):
        self.logger.info("****************Test_004_SearchCustomerEmail*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.user)
        self.lp.setPassword(self.passw)
        self.lp.clickLogin()
        self.logger.info("**********Login success***********")
        self.logger.info("**********Starting Test_004_SearchCustomerEmail Test*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(5)
        self.addcust.clickOnSubCustomerMenu()
        time.sleep(5)

        self.searchCustomer = SearchCustomer(self.driver)
        self.searchCustomer.setemail("victoria_victoria@nopCommerce.com")
        time.sleep(2)
        self.searchCustomer.clickSearch()
        time.sleep(2)
        self.logger.info("**********Verify Result Test_004_SearchCustomerEmail Test*********")

        result = self.searchCustomer.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert result==True
        self.logger.info("*******Result Test_004_SearchCustomerEmail Test PASS*********")
        self.driver.close()