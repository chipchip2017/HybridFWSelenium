import pytest
from selenium import  webdriver
from pageObjects.LoginPage import *
from utilities.readProperties import *
from utilities.customLogger import *


class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    user=ReadConfig.getUser()
    passw=ReadConfig.getPassw()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_HomePageTitle(self, setup):
        self.logger.info("************Test_001_Login************")
        self.logger.info("************Verify Home Page Title ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title
        if title=="Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("************Home Page title is passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************Home Page title is failed ************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************Verify Login ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.user)
        self.lp.setPassword(self.passw)
        self.lp.clickLogin()
        title = self.driver.title

        if title =="Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("************Verify Login is Passed ************")
        else:
            self.logger.error("************Verify Login is failed ************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False


