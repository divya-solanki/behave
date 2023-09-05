import time
from behave import *
from features.Pages.PIMPage import PIMPage

emp_name = ""


@given(u'I navigate to  PIM module and click on Add Employee')
def step_impl(context):
    context.pimPage = PIMPage(context.driver)
    context.pimPage.click_add_employee()

    # context.driver.find_element(By.LINK_TEXT, 'PIM').click()
    # assert context.driver.find_element(By.TAG_NAME, "h6").text == 'PIM'
    # context.driver.find_element(By.XPATH, '//*[contains(text(), "Add Employee")]').click()
    # url = context.driver.current_url
    # assert url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'


@when(u'enter "{FirstName}" and "{LastName}" and click on save button')
def step_impl(context, FirstName, LastName):
    context.pimPage.input_firstname_and_lastname(FirstName, LastName)
    time.sleep(2)
    context.pimPage.click_submit_button()
    emp_name = FirstName + " " + LastName


@then(u'verify Employee name is displayed in Personal Details page')
def step_impl(context):
    context.pimPage.verify_employee_added(emp_name, 'emp_saved')
