from selenium.webdriver.common.by import By


class LoginPageLocators:
    username = (By.NAME, 'username')
    password = (By.NAME, 'password')
    submit_button = (By.XPATH, "//button[@type='submit']")
    verify_homepage = (By.TAG_NAME, "h6")
