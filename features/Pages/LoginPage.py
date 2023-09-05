from selenium.webdriver.common.by import By
from utilities.CommonFunction import CommonFunction


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_username = (By.NAME, 'username')
    locator_password = (By.NAME, 'password')
    locator_submit_button = (By.XPATH, "//button[@type='submit']")
    locator_dashboard_verify = (By.TAG_NAME, "h6")

    def enter_username_and_password(self, username, password):
        self.cf.wait_and_input_text(self.locator_username, username)
        self.cf.wait_and_input_text(self.locator_password, password)

    def click_submit_button(self):
        self.cf.wait_and_click(self.locator_submit_button)

    def verify_dashboardPage(self, text, filename):
        self.cf.verify_page(self.locator_dashboard_verify, text)
        self.cf.get_png_allure_image(filename)