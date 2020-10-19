from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer():
    lnk_customerMenu_xpath="//a[@href='#']/span[text()='Customers']"
    lnk_customerSubMenu_xpath="//span[@class='menu-item-title'][text()='Customers']"
    add_new_button_xpath="//a[@href='/Admin/Customer/Create']"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txt_email_id="Email"
    txt_password_id="Password"
    txt_firstname_id="FirstName"
    txt_lastname_id="LastName"
    txt_MaleGender_id="Gender_Male"
    txt_FeMaleGender_id = "Gender_Female"
    birthday_id ="DateOfBirth"
    company_id="Company"
    checkbox_taxexcempt_id="IsTaxExempt"

    #newsletter_xpath="//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    newsletter_xpath_parent ="//div[@class='k-multiselect-wrap k-floatwrap']"
    newsletter_xpath="//div[contains(@class,'input-group input-group-required')] [@xpath='1']"
    newsletter_test_store2="//li[contains(text(),'Test store 2')]"
    select_newsletter="//select[@id='SelectedNewsletterSubscriptionStoreIds']"

    select_customerRole_xpath="//select[@id='SelectedCustomerRoleIds']"
    select_managerVendor_xpath="//select[@id='VendorId']"
    checkbox_isActive_xpath="//input[@id='Active']"
    txt_AdminComment_xpath="//textarea[@id='AdminComment']"
    button_save_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnk_customerMenu_xpath).click()

    def clickOnSubCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnk_customerSubMenu_xpath).click()

    def clickAddButton(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txt_email_id).clear()
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def setPassword(self, passw):
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(passw)

    def setFirstName(self, firstName):
        self.driver.find_element_by_id(self.txt_firstname_id).clear()
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.txt_lastname_id).clear()
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lastName)

    def setGender(self, gender):
        if gender=='Male':
            self.driver.find_element_by_id(self.txt_MaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element_by_id(self.txt_FeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.txt_MaleGender_id).click()
    def setbirthday(self, birthday):
        self.driver.find_element_by_id(self.birthday_id).clear()
        self.driver.find_element_by_id(self.birthday_id).send_keys(birthday)

    def setcompany(self, company):
        self.driver.find_element_by_id(self.company_id).clear()
        self.driver.find_element_by_id(self.company_id).send_keys(company)

    def settaxexcempt(self):
        self.driver.find_element_by_id(self.checkbox_taxexcempt_id).click()

    def setNewsletter(self, newsletter):

        self.element = WebDriverWait(self.driver, 100).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div")))
        drp=Select(self.driver.find_element_by_xpath(self.select_newsletter))
        time.sleep(3)
        drp.select_by_index(1)
        #self.driver.find_element_by_xpath("//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div").send_keys(newsletter)
        #self.driver.find_element_by_xpath("//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div").send_keys(Keys.ENTER)

        time.sleep(3)

        # self.elements = self.driver.find_elements_by_xpath(self.newsletter_xpath_parent)
        # print("len=", len(self.elements))
        # for i in range(len(self.elements)):
        #     if i == 0:
        #         print("element", self.elements[0])
        #         self.elements[0].click()
        #         time.sleep(3)
        #         self.element = WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_newsletter)))
        #         select = Select(self.element)
        #         select.select_by_value(newsletter)
        #         ##self.elements[0].send_keys(newsletter)
        #         ##self.elements[0].send_keys(Keys.ENTER)
        #         ##drp = Select(self.elements[0])
        #        # drp.first_selected_option()
        #         #drp.select_by_value(newsletter)
        # time.sleep(3)


        # self.element = WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable((By.ID, 'SelectedNewsletterSubscriptionStoreIds')))
        # select = Select(self.element)
        # select.select_by_value(newsletter)



       # drp = Select(self.driver.find_element_by_xpath(self.newsletter_test_store2))
       # drp.select_by_value(newsletter)

       # self.driver.find_element_by_xpath(self.newsletter_xpath).click()

       # time.sleep(2)
        # if newsletter=='Test store 2':
        #     self.listitem=self.driver.find_element_by_xpath(self.newsletter_test_store2)
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].click()", self.listitem)
        #drp=Select(self.driver.find_element_by_xpath(self.newsletter_xpath))
       # drp.select_by_visible_text(newsletter)
        #drp.select_by_value(newsletter)

    def setRole(self, role):
        drp=Select(self.driver.find_element_by_xpath(self.select_customerRole_xpath))
        drp.select_by_visible_text(role)

    def setVendor(self, vendor):
        drp=Select(self.driver.find_element_by_xpath(self.select_managerVendor_xpath))
        drp.select_by_visible_text(vendor)

    def setAdmincomment(self, comment):
        self.driver.find_element_by_xpath(self.txt_AdminComment_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_AdminComment_xpath).send_keys(comment)

    def save(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()