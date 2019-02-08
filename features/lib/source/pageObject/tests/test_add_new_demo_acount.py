from features.lib.source.pageObject.tests.test_add_trading_account import TestAddTradingAccount
from features.helpers.processing import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestAddDemoAccount(TestAddTradingAccount):

    def __init__(self, browser):
        TestAddTradingAccount.__init__(self, browser)

    def add_demo_account(self, currency):
        self.get_add_new_demo_account_tab().click()
        self.get_currency_initial().click()
        self.get_currency_choice(currency)
        self.get_create_account_button().click()

    def create_demo_account(self):
        pass
