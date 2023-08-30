import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I launch Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    time.sleep(5)


@when(u'I open orangeHRM Homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.driver.maximize_window()



@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.NAME, 'username').send_keys(user)
    context.driver.find_element(By.NAME, 'password').send_keys(pwd)


@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()



@then(u'I am on Dashbord page')
def dashboard_page(context):
    try:
        text = context.driver.find_element(By.TAG_NAME, "h6").text
    except:
        text = context.driver.find_element(By.XPATH,
                                           "//div[@class='oxd-alert-content oxd-alert-content--error']/p").text

        if text == 'Dashboard':
            # context.driver.close()
            assert True, "Test passed"
        elif text == 'Invalid credentials':
            context.driver.close()


