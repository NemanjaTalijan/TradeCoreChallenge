from features.lib.source.pageObject.pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from features.logger import *

logger = set_logger()


class PortalBasePage(Base):

    PAGE_BASE_URL = "https://demo-biq.dev.tradecore.io/#/portal/"
    USER_FIRST_LAST_NAME_BY_XPATH = "/html/body/section/div[1]/div/div/div[2]/div[2]"
    ACCOUNT_SUMMARY_MENU = "//ul/li[2]"
    ADD_NEW_TRADING_ACCOUNT_MENU = "//ul/li[3]"
    ADD_NEW_DEMO_ACCOUNT_MENU = "//ul/li[4]"
    PERSONAL_INFORMATION_MENU = "//*[@id=\"base.portal.personal\"]"
    UPLOAD_DOCUMENTS_MENU = "//ul/li[7]"
    CHANGE_PASSWORD_MENU = "//ul/li[8]"
    LEGAL_DOCUMENTS_MENU = "//ul/li[9]"
    DEPOSIT_FUNDS_MENU = "//ul/li[11]"
    WITHDRAW_FUNDS_MENU = "//ul/li[12]"
    INTERNAL_TRANSFER_MENU = "//ul/li[13]"
    PAYMENT_HISTORY_MENU = "//ul/li[14]"
    LOGOUT = "//nav/ul/li[15]"
    PAGE_TITLE_BY_XPATH = "/html/head/title"
    PAGE_TITLE = "TradeCore - Account"

    def __init__(self, browser):
        Base.__init__(self, browser)

        try:
            self.__account_summary = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.ACCOUNT_SUMMARY_MENU}'))
            )
            self.__add_new_trading_account = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.ADD_NEW_TRADING_ACCOUNT_MENU}'))
            )
            self.__add_new_demo_account = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.ADD_NEW_DEMO_ACCOUNT_MENU}'))
            )
            self.__personal_information = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.PERSONAL_INFORMATION_MENU}'))
            )
            self.__upload_documents = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.UPLOAD_DOCUMENTS_MENU}'))
            )
            self.__change_password = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.CHANGE_PASSWORD_MENU}'))
            )
            self.__legal_documents = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.LEGAL_DOCUMENTS_MENU}'))
            )
            self.__deposit_funds = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.DEPOSIT_FUNDS_MENU}'))
            )
            self.__withdraw_funds = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.WITHDRAW_FUNDS_MENU}'))
            )
            self.__internal_transfer = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.INTERNAL_TRANSFER_MENU}'))
            )
            self.__payment_history = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.PAYMENT_HISTORY_MENU}'))
            )
            self.__logout = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'{PortalBasePage.LOGOUT}'))
            )
        except (NoSuchElementException, TimeoutException) as e:
            logger.debug("Some of the elements are not found on user account main page or not needed for test!")

    def get_account_summary_tab(self):
        return self.__account_summary

    def get_add_new_trading_account_tab(self):
        return self.__add_new_trading_account

    def get_add_new_demo_account_tab(self):
        return self.__add_new_demo_account

    def get_personal_information_tab(self):
        return self.__personal_information

    def get_upload_documents_tab(self):
        return self.__upload_documents

    def get_change_password_tab(self):
        return self.__change_password

    def get_legal_documents_tab(self):
        return self.__legal_documents

    def get_deposit_funds_tab(self):
        return self.__deposit_funds

    def get_withdraw_funds_tab(self):
        return self.__withdraw_funds

    def get_internal_transfer_tab(self):
        return self.__internal_transfer

    def get_payment_history_tab(self):
        return self.__payment_history

    def get_logout(self):
        return self.__logout

    def account_summary_tab_click(self):
        self.get_account_summary_tab().click()

    def add_new_trading_account_tab_click(self):
        self.get_add_new_trading_account_tab().click()

    def add_new_demo_account_tab_click(self):
        self.get_add_new_demo_account_tab().click()

    def personal_information_tab_click(self):
        self.get_personal_information_tab().click()

    def upload_documents_tab_click(self):
        self.get_upload_documents_tab().click()

    def change_password_tab_click(self):
        self.get_change_password_tab().click()

    def legal_documents_tab_click(self):
        self.get_legal_documents_tab().click()

    def deposit_funds_tab_click(self):
        self.get_deposit_funds_tab().click()

    def withdraw_funds_tab_click(self):
        self.get_withdraw_funds_tab().click()

    def internal_transfer_tab_click(self):
        self.get_internal_transfer_tab().click()

    def get_payment_hystory_tab_click(self):
        self.get_payment_history_tab().click()

    def get_logout_click(self):
        self.get_logout().click()

    def scroll_page(self, how_much):
        self.browser.execute_script(f"window.scrollTo(0, {how_much})")
