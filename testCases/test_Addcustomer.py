import pytest
from selenium import  webdriver
from pageObjects.LoginPage import *
from utilities.readProperties import *
from utilities.customLogger import *
from pageObjects.AddCustomerPage import *
import string
import random
import time



class Test_003_AddCustomer:
    baseURL= ReadConfig.getApplicationURL()
    user=ReadConfig.getUser()
    passw=ReadConfig.getPassw()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("****************Test_003_AddCustomer*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.user)
        self.lp.setPassword(self.passw)
        self.lp.clickLogin()
        self.logger.info("**********Login success***********")
        self.logger.info("**********Starting Add Customer Test*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnSubCustomerMenu()

        time.sleep(5)

        self.addcust.clickAddButton()

        self.logger.info("***************Provide customer info*********")
        time.sleep(2)

        self.email = random_generator() + "@gmail.com"
        print("Email"+self.email)
        self.addcust.setEmail(self.email)
        time.sleep(2)
        self.addcust.setPassword("test123")
        time.sleep(2)
        self.addcust.setFirstName("HVN")
        time.sleep(2)
        self.addcust.setLastName("Test")
        time.sleep(2)

        self.addcust.setGender("Male")
        time.sleep(2)
        self.addcust.setbirthday("04/04/1975")
        time.sleep(2)

        self.addcust.setcompany("Company")
        time.sleep(2)
        self.addcust.settaxexcempt()
        time.sleep(2)

       # self.addcust.setNewsletter("Test store 2")
        time.sleep(2)
        self.addcust.setRole("Registered")
        time.sleep(2)

        self.addcust.setVendor("Vendor 1")
        time.sleep(2)
        self.addcust.setAdmincomment("Admin comment")

        self.addcust.save()

        self.logger.info("**********Verify add customer*********")
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
