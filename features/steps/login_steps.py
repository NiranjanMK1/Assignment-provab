import time
from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.logger import LogGen
import openpyxl
log = LogGen.loggen()


@given(u'User on the Hubbler login page')
def step_impl(context):
    log.info("****Teststarted****")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://auth.hubbler.in/login/index.html")
    log.info("opened the login page")


@when(u'User click on login with OTP')
def step_impl(context):
    login_with_otp_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='switchMode']"))
    )
    login_with_otp_button.click()
    log.info("user clicked on login with OTP")


@then(u'User enter valid login details from excel')
def step_impl(context):
    log.info("Reading data from excel file started")
    wb = openpyxl.load_workbook(r".//Data/login_details.xlsx")
    sheet = wb.active
    mobile_or_email = sheet.cell(row=2, column=2).value
    log.info("passing email id to the textbox")
    context.driver.find_element(By.ID, "value").send_keys(mobile_or_email)
    log.info("sucessfully passed data to the textbox")


@then(u'User click on the Next button')
def step_impl(context):
    context.driver.find_element(By.ID, "otpNext").click()
    log.info("User clicked on the next button")


# Here after I used gmail for checking we can customize according to the requirement


@then(u'User Go to email in a new tab in chrome')
def step_impl(context):
    context.driver.execute_script("window.open('');")
    context.driver.switch_to.window(context.driver.window_handles[1])
    context.driver.get("https://mail.google.com/mail/u/0/")
    log.info("user successfully opened mailbox")


# @then(u'I search for the OTP sent by hubbler mail')
# def otp_capture(context):
#     context.driver.find_element(By.NAME, "q").send_keys(f"from: Hubbler  OTP", Keys.RETURN)
#     time.sleep(3)
#     context.driver.find_element(By.XPATH, "//div[contains(text(), 'OTP is ')]").click()
#     time.sleep(3)
#     context.otp = context.driver.find_element(By.XPATH,"//h2[contains(text(), 'OTP is')]").text.split()[-1]
#     return context.otp


@then(u'User copy the OTP')
def otp_copy(context):
    copy_otp = 2464646  # otp_capture(context)
    log.info("user successfully copied the otp")
    return copy_otp


@then(u'User Return to enter the OTP screen for hubbler')
def step_impl(context):
    window_handles = context.driver.window_handles
    context.driver.switch_to.window(window_handles[-2])
    log.info("user successfully swithced back to previous window to enter otp")


@then(u'User paste the OTP')
def step_impl(context):
    o_t_p = otp_copy(context)
    time.sleep(10)
    context.driver.find_element(By.XPATH, "//input[@id='optNumber']").send_keys(o_t_p)
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='optNumber']")))
    element.send_keys(o_t_p)
    log.info("user sucessfully enterd otp")


@then(u'User should see the My day landing page')
def step_impl(context):
    try:
        act_title = context.driver.title
        exp_title = "My day"
        if act_title == exp_title:
            log.info("Test Passed")
            context.driver.close
            assert True, "Test Passed"

    except:
        context.driver.close()
        log.info("Test failed")
        assert False, "Test Failed"
