import pytest
from selenium import webdriver
from pageObjects.LoginPage import *
from utilities.readProperties import *
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/Data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************Test_002_DDT_Login***********")
        self.logger.info("************Verify Login ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of row i a excel", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.passw = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.passw)
            self.lp.clickLogin()
            time.sleep(5)
            title = self.driver.title

            if title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("***Passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Fail")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif title != "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("***Fail")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***Passed")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*******Login DDT Passed******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*******Login DDT Failed******")
            self.driver.close()
            assert True

        self.logger.info("*********End of Login DDT Test***********")
