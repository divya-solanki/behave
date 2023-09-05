import time

from selenium.webdriver.common.by import By
from utilities.CommonFunction import CommonFunction


class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_navigate_to_PIM = (By.LINK_TEXT, 'PIM')
    locator_verify_PIM_page = (By.TAG_NAME, "h6")
    locator_add_employee = (By.XPATH, '//*[contains(text(), "Add Employee")]')
    locator_firstname = (By.NAME, 'firstName')
    locator_lastname = (By.NAME, 'lastName')
    locator_submit_button = (By.XPATH, "//button[@type= 'submit']")
    locator_verify_emp_added = (By.XPATH, '//h6[@class = "oxd-text oxd-text--h6 --strong"]')

    locator_SSN = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[7]")
    locator_DOB = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
    locator_find_nationality_list = (By.XPATH, "(//div[@clear='false'][normalize-space()='-- Select --'])[1]")
    locator_select_nationality = (By.XPATH, '//*[contains(text(), "British")]')
    locator_find_marital_status_list = (By.XPATH, "(//div)[105]")
    locator_select_marital_status_list = (By.XPATH, '//*[contains(text(), "Single")]')
    locator_select_gender = (By.XPATH, "(//label[normalize-space()='Male'])[1]")
    locator_save_button = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")

    def click_add_employee(self):
        self.cf.wait_and_click(self.locator_navigate_to_PIM)
        time.sleep(2)
        self.cf.get_png_allure_image('PIM Page')
        self.cf.verify_page(self.locator_verify_PIM_page, "PIM")
        self.cf.wait_and_click(self.locator_add_employee)

    def input_firstname_and_lastname(self, firstname, lastname):
        self.cf.wait_and_input_text(self.locator_firstname, firstname)
        self.cf.wait_and_input_text(self.locator_lastname, lastname)

    def click_submit_button(self):
        self.cf.wait_and_click(self.locator_submit_button)

    def verify_employee_added(self, employee_name, filename):
        self.cf.verify_page(self.locator_verify_emp_added, employee_name, filename)

    def input_SSN_and_DOB(self, SSN,DOB):
        self.cf.wait_and_input_text(self.locator_SSN, SSN)
        self.cf.wait_and_input_text(self.locator_DOB, DOB)

    def select_nationality(self):
        self.cf.wait_and_click(self.locator_find_nationality_list)
        self.cf.wait_and_click(self.locator_select_nationality)

    def select_marital_status(self):
        self.cf.wait_and_click(self.locator_find_marital_status_list)
        self.cf.wait_and_click(self.locator_select_marital_status_list)

    def select_gender(self):
        self.cf.wait_and_click(self.locator_select_gender)

    def save_details(self):
        self.cf.wait_and_click(self.locator_submit_button)
        time.sleep(2)
        self.cf.get_png_allure_image('Employee Details')