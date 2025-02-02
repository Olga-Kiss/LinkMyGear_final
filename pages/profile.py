
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains

from pages.base import BasePage
# from pages.login import LoginPage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_my_profile = (By.XPATH, "//button[contains(text(), 'My Profile')]")
        self.my_email = (By.XPATH, "//input[@name='username']")  # how to refer login.py?
        self.my_password = (By.XPATH, "//input[@name='password']")  # how to refer login.py?
        self.my_login_button = (By.XPATH, "//button[contains(text(), 'Login')]")  # how to refer login.py?
        self.my_profile_icon = (By.XPATH, "//a[@href='#/profile']")
        self.first_name_field = (By.XPATH, "(//input[@type='text' and contains(@class, 'el-input__inner') and "
                                           "@autocomplete='off'])[1]")
        self.last_name_field = (By.XPATH, "(//input[@type='text' and contains(@class, 'el-input__inner') and "
                                          "@autocomplete='off'])[2]")
        self.email_field = (By.XPATH, "//div[@class='el-input__wrapper']//input[@class='el-input__inner' and "
                                      "@type='text' and @disabled]")
        self.add_phone_button = (By.XPATH, "//button[contains(text(), 'Add Phone')]")
        self.select_prefix = (By.XPATH, "//div[@class='el-select']/div[@class='el-select__wrapper is-filterable "
                                        "el-tooltip__trigger el-tooltip__trigger']")
        self.prefix_us = (By.XPATH, "//span[contains(text(),'+1684')]")
        self.enter_phone = (By.XPATH, "//input[@type='text' and @placeholder='Enter Phone']")
        self.delete_phone = (By.XPATH, "//div[@class='repeater-input']//button[@type='button']")
        self.sms_checkbox = (By.XPATH, "//span[@class='el-checkbox__inner']")
        self.save_button = (By.XPATH, "//button[contains(text(), 'Save')]")
        self.change_password_h5 = (By.XPATH, "//h5[text() = 'Change password'")
        self.current_password_field = (By.XPATH, "//div[contains(@class, 'el-form-item') and .//div[text()="
                                                 "'Please input your old password']]//input[@type='password']")
        self.new_password_field = (By.XPATH, "(//div[contains(@class, 'el-form-item') and contains(@class, 'is-required"
                                             "') and contains(@class, 'asterisk-left')]//div[contains(@class, 'el-input"
                                             "') and contains(@class, 'is-disabled')])[1]//input[@type='password']")
        self.confirm_password_field = (By.XPATH, "//div[contains(@class, 'el-form-item')][3]//input[@type='password']")
        self.change_password_button = (By.XPATH, "//button[contains(text(), 'Change password')]")

    def ok_verify_page(self):
        super().verify_page(self.page_my_profile)

    def open_page_my_profile(self):
        self.locate_element(self.page_my_profile).click()

    # def type_text(self, field_locator: tuple, text: str):
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(field_locator))
    #     element.clear()
    #     element.send_keys(text)

    # def click_element(self, element_locator: tuple):
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element_locator))
    #     element.click()

    def click_element_by_name(self, element_name: str):
        element = None
        if element_name.lower() == "first name":
            element = self.first_name_field
        elif element_name.lower() == "last name":
            element = self.last_name_field
        elif element_name.lower() == "my email":
            element = self.my_email
        elif element_name.lower() == "select_prefix":
            element = self.select_prefix
        elif element_name.lower() == "prefix_us":
            element = self.prefix_us

        self.click_element(element)


    def toggle_sms_acceptance(self, accept: bool):
        checkbox = self.locate_element(self.sms_checkbox)
        self.driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        if checkbox.is_selected() != accept:
            checkbox.click()
