from selenium.webdriver.common.by import By
from utilities.CommonFunction import CommonFunction


class Admin:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_navigate_to_admin_page = (By.LINK_TEXT, 'Admin')
    locator_verify_admin_page = (By.TAG_NAME, "h6")
    locator_username = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    locator_search_button = (By.XPATH, "//button[@type='submit']")
    locator_verify_search = (By.XPATH, "//div[@class='oxd-table-card']//div[2]//div[1]")

    def navigate_to_admin_page(self):
        self.cf.wait_and_click(self.locator_navigate_to_admin_page)
        self.cf.verify_page(self.locator_verify_admin_page, "Admin")

    def input_username(self, username):
        self.cf.wait_and_input_text(self.locator_username, username)

    def click_search_button(self):
        self.cf.wait_and_click(self.locator_search_button)

    def verify_search_results(self, search_result):
        self.cf.verify_page(self.locator_verify_search, search_result)
        self.cf.get_png_allure_image('search_result')
