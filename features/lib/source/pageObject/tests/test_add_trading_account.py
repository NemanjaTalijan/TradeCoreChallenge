from features.lib.source.pageObject.pages.portal_page import PortalBasePage
from features.helpers.processing import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestAddTradingAccount(PortalBasePage):

    CURRENCY = "form___fieldId___chosen"
    CREATE_BUTTON_BY_ID = "portal-button-account-add"

    def __init__(self, browser):
        PortalBasePage.__init__(self, browser)

        try:
            self.__currency_initial = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, f"{TestAddTradingAccount.CURRENCY}"))
            )
            self.__currency_choice = None
            self.__create_account_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, f"{TestAddTradingAccount.CREATE_BUTTON_BY_ID}"))
            )
        except TimeoutException:
            print("Some of the elements are not found on page  - Add a new trading account!")

    def get_currency_initial(self):
        return self.__currency_initial

    def currency_initial_click(self):
        self.get_currency_initial().click()

    def get_currency_choice(self, currency):
        try:
            self.__currency_choice = self.__currency_initial = WebDriverWait(self.browser, 10).until(
                  EC.element_to_be_clickable((By.XPATH, f"//div[1]/div/ul/li[{check_trading_currency(currency)}]"))
              )
            return self.__currency_choice
        except TimeoutException:
            print("Currency choice not found on page - Add a new trading account!")

    def get_create_account_button(self):
        return self.__create_account_button

    def add_trading_account(self, currency):
        self.get_add_new_trading_account_tab().click()
        self.currency_initial_click()
        self.get_currency_choice(currency).click()
        self.get_create_account_button().click()

    def check_add_trading_assount(self):
        pass


