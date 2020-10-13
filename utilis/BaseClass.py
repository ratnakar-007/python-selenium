import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_text(self, text):
        wait = WebDriverWait(self.dr, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

    def select_option_by_text(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def get_logger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("C:\\Users\\ratnakar_pc\\PycharmProjects\\PythonSeleniumFramework\\logs\\logfile.log")
        formatHandler = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
        fileHandler.setFormatter(formatHandler)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
