from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait


class SearchCustomer():
    txt_email_id = "SearchEmail"
    txt_firstname_id="SearchFirstName"
    txt_lastname_id="SearchLastName"
    search_button_xpath="//button[@id='search-customers']"
    search_result_table_xpath="//table[@role='grid']"
    table_result_xpath="//table[@id='customers-grid']"
    tablerows_xpath="//table[@id='customers-grid']//tbody/tr"
    tablecolumn_xpath="//table[@id='customers-grid']//tbody/tr/td"



    def __init__(self,driver):
        self.driver=driver

    def setemail(self, email):
        self.driver.find_element_by_id(self.txt_email_id).clear()
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def setfirstname(self, firstname):
        self.driver.find_element_by_id(self.txt_firstname_id).clear()
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(firstname)

    def setlastname(self, lastname):
        self.driver.find_element_by_id(self.txt_lastname_id).clear()
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lastname)
    def clickSearch(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    def getNoRows(self):
        return len(self.driver.find_elements_by_xpath(self.tablerows_xpath))

    def getNoColumn(self):
        return len(self.driver.find_elements_by_xpath(self.tablecolumn_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        print("row=",self.getNoRows())
        for r in range(1, self.getNoRows()+1):
            table = self.driver.find_element_by_xpath(self.table_result_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email==emailid:
                flag= True
                break
        return flag

    def searchCustomerName(self, Name):
        flag = False
        for r in range(1, self.getNoRows()+1):
            table = self.driver.find_element_by_xpath(self.table_result_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag