import allure
from allure_commons.types import AttachmentType
from behave import *
from features.Pages.LoginPage import LoginPage


@given(u'I open orangeHRM Homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    allure.attach(context.driver.get_screenshot_as_png(), name='login page',
                  attachment_type=AttachmentType.PNG)


@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.enter_username_and_password(user, pwd)


@when(u'Click on login button')
def step_impl(context):
    context.loginPage.click_submit_button()


@then(u'verify navigation to Dashboard page is successful')
def dashboard_page(context):
    context.loginPage.verify_dashboardPage('Dashboard', 'login')

        # text = context.driver.find_element(By.XPATH,
        #                                    "//div[@class='oxd-alert-content oxd-alert-content--error']/p").text
        #
        # if text == 'Dashboard':
        #     # context.driver.close()
        #     assert True, "Test passed"
        # elif text == 'Invalid credentials':
        #     context.driver.close()
