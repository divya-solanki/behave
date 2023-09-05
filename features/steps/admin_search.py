import time
from behave import *
from features.Pages.Admin import Admin
from selenium.webdriver.common.by import By


@given(u'I am on Dashboard page')
def step_impl(context):
    pass

@when(u'navigate to Admin page')
def step_impl(context):
    context.admin = Admin(context.driver)
    context.admin.navigate_to_admin_page()


@when(u'enter "{username}" to search')
def step_impl(context, username):
    context.admin.input_username(username)


@when(u'click on search button')
def step_impl(context):
    context.admin.click_search_button()


@then(u'search result with "{username}" is shown in bottom pane.')
def step_impl(context, username):
    context.admin.verify_search_results(username)
    time.sleep(2)
