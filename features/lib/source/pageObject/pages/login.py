from features.lib.source.pageObject.pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from features.logger import *

logger = set_logger()


class LoginPage(Base):

    EMAIL_ADDRESS_TEXT_INPUT_FIELD_BY_ID = "credentials"
    PASSWORD_TEXT_INPUT_FIELD_BY_ID = "password"
    LOG_IN_BUTTON = "//button"

    def __init__(self, browser):
        Base.__init__(self, browser)

        try:
            self.__email = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, f'{LoginPage.EMAIL_ADDRESS_TEXT_INPUT_FIELD_BY_ID}'))
            )
            self.__password = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, f'{LoginPage.PASSWORD_TEXT_INPUT_FIELD_BY_ID}'))
            )
            self.__login_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{LoginPage.LOG_IN_BUTTON}'))
            )
        except (NoSuchElementException, TimeoutException):
            logger.debug("Some of the elements are not found on user account main page!")

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_login_button(self):
        return self.__login_button

    def email_send_text(self, email):
        self.get_email().clear()
        self.get_email().send_keys(email)

    def password_send_text(self, password):
        self.get_password().clear()
        self.get_password().send_keys(password)

    def login_button_click(self):
        self.get_login_button().click()

    def login_user(self, email, password):
        self.email_send_text(email)
        self.password_send_text(password)
        self.login_button_click()
