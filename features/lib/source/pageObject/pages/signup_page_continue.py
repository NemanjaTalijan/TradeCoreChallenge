from features.lib.source.pageObject.pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.helpers.processing import *
import time


class SignupContinue(Base):

    SHARES_BY_XPATH = "//form/div[2]/div/div/div/div/div[1]"
    FOREX_BY_XPATH = "//form/div[3]/div/div/div/div/div[1]"
    CFDS_BY_XPATH = "//form/div[4]/div/div/div/div/div[1]"
    SPREAD_BETTING_BY_XPATH = "//form/div[5]/div/div/div/div/div[1]"
    HAVE_YOU_BY_XPATH = "//form/div[7]/div/div/div/div/div[1]"
    TRADING_PLATFORM_DROPDOWN_BY_XPATH = "//form/div[9]/div/div/div/div/div[1]"
    TRADING_CURRENCY_DROPDOWN_BY_XPATH = "//form/div[10]/div/div/div/div/div[1]"
    APPROXIMATE_ANNUAL_INCOME_BY_XPATH = "//form/div[10]/div/div/div/div/div[1]"
    EMPLOYMENT_STATUS_BY_XPATH = "//form/div[11]/div/div/div/div/div[1]"
    APPROXIMATE_VALUE_OF_ASSETS_BY_XPATH = "//form/div[12]/div/div/div/div/div[1]"
    FORM_READ_CHECK_BOX_BY_ID = "//form/div[15]"
    FINNISH_BUTTON_BY_ID = "button-step"
    ON_CONTINUE_PAGE_TEXT_FIELD = "//div[1]/div/div/div/div/h2[2]"
    TEXT_ON_CONTINUE_PAGE = "HAVE YOU TRADED IN ANY OF THE FOLLOWING IN THE PAST THREE YEARS?"

    def __init__(self, browser):
        Base.__init__(self, browser)

        self.__text = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{SignupContinue.ON_CONTINUE_PAGE_TEXT_FIELD}"))
        )
        self.check_text_on_page()
        self.__shares_initial = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"{SignupContinue.SHARES_BY_XPATH}"))
        )
        self.__shares = None
        self.__forex_initial = self.browser.find_element(By.XPATH, f"{SignupContinue.FOREX_BY_XPATH}")
        self.__forex = None
        self.__cfds_initial = self.browser.find_element(By.XPATH, f"{SignupContinue.CFDS_BY_XPATH}")
        self.__cfds = None
        self.__spread_betting_initial = self.browser.find_element(By.XPATH, f"{SignupContinue.SPREAD_BETTING_BY_XPATH}")
        self.__spread_betting = None
        self.__have_you_initial = None
        self.__have_you = None
        self.__trading_platformes_initial = self.browser.find_element(By.XPATH, f"{SignupContinue.TRADING_PLATFORM_DROPDOWN_BY_XPATH}")
        self.__trading_platformes = None
        self.__trading_currency_initial = None
        self.__trading_currency = None
        self.__approximate_annual_income_initial = self.browser.find_element(By.XPATH, f"{SignupContinue.APPROXIMATE_ANNUAL_INCOME_BY_XPATH}")
        self.__approximate_annual_income = None
        self.__employment_status_initial = self.browser.find_element(By.XPATH, f"{SignupContinue.EMPLOYMENT_STATUS_BY_XPATH}")
        self.__employment_status = None
        self.__approximate_value_of_assets_initial = self.browser.find_element(By.XPATH, f"{SignupContinue.APPROXIMATE_VALUE_OF_ASSETS_BY_XPATH}")
        self.__approximate_value_of_assets = None
        self.__form_read_check_box = None
        self.__finnish_button = None

    def get_text_on_continue_page(self):
        return self.__text

    def check_text_on_page(self):
        while self.get_text_on_continue_page().__getattribute__("text") != f"{SignupContinue.TEXT_ON_CONTINUE_PAGE}":
            time.sleep(0.1)

    def get_shares_initial(self):
        return self.__shares_initial

    def shares_click(self):
        self.get_shares_initial().click()

    def get_share_choose(self, share):
        self.__shares = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@class='{check_answer(share)}' and contains(.,'{share}')]"))
        )
        return self.__shares

    def get_forex_initial(self):
        return self.__forex_initial

    def forex_click(self):
        self.get_forex_initial().click()

    def get_forex_choose(self, forex):
        self.__forex = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[3]/div/div/div/div/div[1]/div/ul/li[{check_answer_other(forex)}]"))
        )
        return self.__forex

    def get_cfds_initial(self):
        return self.__cfds_initial

    def cfds_click(self):
        self.get_cfds_initial().click()

    def get_cfds_choose(self, cfds):
        self.__cfds = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[4]/div/div/div/div/div[1]/div/ul/li[{check_answer_other(cfds)}]"))
        )
        return self.__cfds

    def get_spread_betting_initial(self):
        return self.__spread_betting_initial

    def spread_betting_click(self):
        self.get_spread_betting_initial().click()

    def get_spread_betting_choose(self, spread_betting):
        self.__spread_betting = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[5]/div/div/div/div/div[1]/div/ul/li[{check_answer_other(spread_betting)}]"))
        )
        return self.__spread_betting

    def get_have_you_initial(self):
        self.__have_you_initial = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                        f"{SignupContinue.HAVE_YOU_BY_XPATH}"))
        )
        return self.__have_you_initial

    def have_you_click(self):
        self.get_have_you_initial().click()

    def get_have_you_choose(self, have_you):
        self.__have_you = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[7]/div/div/div/div/div[1]/div/ul/li[{check_have_you(have_you)}]"))
        )
        return self.__have_you

    def get_trading_platformes_initial(self):
        return self.__trading_platformes_initial

    def trading_platformes_click(self):
        self.get_trading_platformes_initial().click()

    def get_trading_platformes_choose(self, trading_platformes):
        self.__trading_platformes = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[9]/div/div/div/div/div[1]/div/ul/li[1]"))
        )
        return self.__trading_platformes

    def get_trading_currency_initial(self):
        self.__trading_currency_initial = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[10]/div/div/div/div/div[1]"))
        )
        return self.__trading_currency_initial

    def trading_currency_click(self):
        self.get_trading_currency_initial().click()

    def get_trading_currency_choose(self, trading_currency):
        self.__trading_currency = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[10]/div/div/div/div/div[1]/div/ul/li[{check_trading_currency(trading_currency)}]"))
        )
        return self.__trading_currency

    def get_approximate_annual_income_initial(self):
        return self.__approximate_annual_income_initial

    def approximate_annual_income_click(self):
        self.get_approximate_annual_income_initial().click()

    def get_approximate_annual_income_choose(self, approximate_annual_income):
        self.__approximate_annual_income = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[11]/div/div/div/div/div[1]/div/ul/li[{check_approximate_annual_income(approximate_annual_income)}]"))
        )
        return self.__approximate_annual_income

    def get_employment_status_initial(self):
        return self.__employment_status_initial

    def employment_status_click(self):
        self.get_employment_status_initial().click()

    def get_employment_status_choose(self, employment_status):
        self.__employment_status = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[12]/div/div/div/div/div[1]/div/ul/li[{check_employment_status(employment_status)}]"))
        )
        return self.__employment_status

    def get_approximate_value_of_assets_initial(self):
        return self.__approximate_value_of_assets_initial

    def approximate_value_of_assets_click(self):
        self.get_approximate_value_of_assets_initial().click()

    def get_approximate_value_of_assets_choose(self, approximate_value_of_assets):
        self.__approximate_value_of_assets = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='steps']/form/div[13]/div/div/div/div/div[1]/div/ul/li[{check_approximate_value_of_assets(approximate_value_of_assets)}]"))
        )
        return self.__approximate_value_of_assets

    def get_form_read_check_box(self):
        self.__form_read_check_box = self.browser.find_element(By.XPATH, f"{SignupContinue.FORM_READ_CHECK_BOX_BY_ID}")
        return self.__form_read_check_box

    def get_finnish_button(self):
        self.__finnish_button = self.browser.find_element(By.ID, f"{SignupContinue.FINNISH_BUTTON_BY_ID}")
        return self.__finnish_button

    def scroll_page(self, how_much):
        self.browser.execute_script(f"window.scrollTo(0, {how_much})")

    def populate_signup_continue_page(self, share, forex, cfds, spread_betting):
        self.shares_click()
        self.get_share_choose(share).click()
        self.forex_click()
        self.get_forex_choose(forex).click()
        self.cfds_click()
        self.get_cfds_choose(cfds).click()
        self.spread_betting_click()
        self.get_spread_betting_choose(spread_betting).click()
        self.browser.save_screenshot(f'features/screenShots/signup_continue - {time.asctime()}.png')

    def populate_have_you_question(self, have_you_answer):
        self.scroll_page(500)
        self.have_you_click()
        self.get_have_you_choose(have_you_answer).click()
        self.browser.save_screenshot(f'features/screenShots/signup_continue - {time.asctime()}.png')

    def populate_financial_details(self, trading_platform, trading_currency, approximate_annual_income, employment_status, approximate_value_of_assets):
        self.scroll_page(1080)
        self.trading_platformes_click()
        self.get_trading_platformes_choose(trading_platform).click()
        self.trading_currency_click()
        self.get_trading_currency_choose(trading_currency).click()
        self.approximate_annual_income_click()
        self.get_approximate_annual_income_choose(approximate_annual_income).click()
        self.employment_status_click()
        self.get_employment_status_choose(employment_status).click()
        self.approximate_value_of_assets_click()
        self.get_approximate_value_of_assets_choose(approximate_value_of_assets).click()

    def click_on_terms(self):
        self.get_form_read_check_box().click()

    def click_on_finish_button(self):
        self.get_finnish_button().click()
