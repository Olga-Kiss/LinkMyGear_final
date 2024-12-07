import logging
from ctypes import HRESULT

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.network import set_data_size_limits_for_test
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from setuptools.command.build_ext import if_dl


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = ()
        self.page_devices = (By.XPATH, "")
        self.page_records = ()
        self.page_logbook = ()
        self.settings = ()
        self.button_logout = ()

    def locate_element(self, element: tuple[str, str]):
        elements = (WebDriverWait(self.driver, 15).
                    until(EC.presence_of_all_elements_located(element)))
        assert len(elements) == 1, f"Element {element[0]} in {elements} exists not once"
        return elements[0]


    def verify_page(self, page_header: tuple[str, str]):
        self.locate_element(page_header)

    def open_page_devices(self):
        pass
        # self.locate_element(self.page_devices).click()

