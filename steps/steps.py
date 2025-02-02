from time import sleep

from behave import step
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.forgot_password import ForgotPasswordPage
from pages.login import LoginPage, login
from pages.profile import ProfilePage


@step('Open "{env}" environment')
def open_url(context, env):

    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }
    context.logger.info(f"Open environment '{env}' form {environments}")
    context.driver.get(environments[env])
    context.logger.warning("Create LoginPage object")
    context.login_page = LoginPage(context.driver)
    context.logger.error("LoginPage object created")
    context.current_page = context.login_page


@step('Verify presence of element "{element_name}"')
def verify_element_presence(context, element_name):
    element = None

    if element_name.lower() == "forgot password link":
        element = context.current_page.forgot_password_link
    elif element_name.lower() == "your email field":
        element = context.current_page.your_email
    elif element_name.lower() == "send button":
        element = context.current_page.send
    else:
        assert False, f"Unknown element: {element_name}"

    assert context.current_page.locate_element(element).is_displayed(), f"Element '{element_name}' is not displayed"


@step('The user enters "{text}" into the "{field_name}" field')
def enter_text_into_field(context, text, field_name):
    if field_name.lower() == "your email":
        context.current_page.enter_text(context.current_page.your_email, text)
    else:
        assert False, f"Unknown field: {field_name}"

@step('Click button "{button_name}"')
def click_button(context, button_name):
    if button_name.lower() == "send":
        context.current_page.click_element(context.current_page.send)
    else:
        assert False, f"Unknown button: {button_name}"

@step('Click "{element_name}" element')
def click_element_by_name(context, element_name):
    if element_name.lower() == "forgot password":
        context.login_page.click_forgot_password()
        context.forgot_password_page = ForgotPasswordPage(context.driver)
        context.current_page = context.forgot_password_page
        context.forgot_password_page.verify_page()
    else:
        assert False, f"Unknown element: {element_name}"

@step('Verify the "{page_name}" page is displayed')
def verify_page_is_displayed(context, page_name):
    if page_name.lower() in ["login", "log in"]: #handles variations
        context.login_page.verify_page()
    elif page_name.lower() == "forgot password":
        context.forgot_password_page.verify_page()
    elif page_name.lower() == "devices":
        context.devices_page.verify_page()
    elif page_name.lower() == "records":
        context.records_page.verify_page()
    elif page_name.lower() == "logbook":
        context.logbook.verify_page()
    elif page_name.lower() == "profile":
        context.profile.verify_page()
    else:
        assert False, f"Unknown page: {page_name}"

@step('The user enters a valid "{email}" into the "{field_name}" field')
def enter_valid_email(context, email, field_name):
    if field_name.lower() == "your email":
        context.current_page.enter_email(email)
    else:
        assert False, f"Unknown field: {field_name}"

@step('A confirmation message appears')
def verify_confirmation_message(context):
    assert context.current_page.is_confirmation_message_displayed(), "Confirmation message did not appear"

@step('Click element "{element_name}"')
def click_element_by_name(context, element_name):
    context.profile.click_element_by_name(element_name)

# @step('Click save button')
# def click_save_button(context):
#     page = context.current_page()
#     if page == "profile":
#         context.profile.click_element_by_name("Save")



@step('Type "{text}" into "{field_name}"')
def type_text(context, text, field_name):
    profile_page = ProfilePage(context.driver)
    field_locator = getattr(profile_page, field_name)
    profile_page.type_text(field_locator, text)


@step('Verify text "{expected_text}" is in "{field_name}"')
def step_impl(context, expected_text, field_name):
    profile_page = ProfilePage(context.driver)
    field_locator = getattr(profile_page, field_name)
    element = profile_page.locate_element(field_locator)
    assert element.get_attribute("value") == expected_text, f"Expected {expected_text}, but got {element.get_attribute('value')}"


@step('Toggle SMS acceptance to {state}')
def step_impl(context, state):
    profile_page = ProfilePage(context.driver)
    profile_page.toggle_sms_acceptance(state.lower() == "true")


@step('Rename the device with name "{current_name}" to "{new_name}"')
def rename_device(context, current_name, new_name):
    context.devices.rename_device_by_name(current_name, new_name)

@step('Rename the device with imei "{imei}" to "{new_name}"')
def rename_device(context, imei, new_name):
    context.devices.rename_device_by_imei(imei, new_name)
