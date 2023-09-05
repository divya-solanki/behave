import time
from behave import *
from features.Pages.PIMPage import PIMPage


@Then(u'Enter "{SSN}" and "{DOB}"')
def step_impl(context, SSN, DOB):
    time.sleep(3)
    context.pimPage = PIMPage(context.driver)
    context.pimPage.input_SSN_and_DOB(SSN, DOB)

@then(u'select Nationality')
def step_impl(context):
    context.pimPage.select_nationality()


@then(u'Select Marital Status and Gender')
def step_impl(context):
    context.pimPage.select_marital_status()
    context.pimPage.select_gender()


@then(u'click save button')
def step_impl(context):
    context.pimPage.save_details()
