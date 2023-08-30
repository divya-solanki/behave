import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I click on PIM module')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'PIM').click()
    assert context.driver.find_element(By.TAG_NAME, "h6").text == 'PIM'


@when(u'I click on Add Employee')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[contains(text(), "Add Employee")]').click()
    url = context.driver.current_url
    assert url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'


@when(u'I enter First Name')
def step_impl(context):
    context.driver.find_element(By.NAME, 'firstName').send_keys('Toby')


@when(u'I enter Last name')
def step_impl(context):
    context.driver.find_element(By.NAME, 'lastName').send_keys('Jones')


@when(u'I click on save button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
    time.sleep(3)
