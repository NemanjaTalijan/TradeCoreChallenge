from features.lib.source.pageObject.pages.portal_page import PortalBasePage
from features.helpers.processing import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.logger import *

logger = set_logger()


class TestSeePersonalInformation(PortalBasePage):

    FIRST_NAME_FIELD = "//form/div[1]/div[1]/div[1]/p"
    LAST_NAME_FIELD = "//form/div[1]/div[2]/div[1]/p"
    EMAIL_FIELD = "//form/div[2]/div[1]/div[1]/p"
    PHONE_FIELD = "//form/div[2]/div[2]/div[1]/p"
    COUNTRY_FIELD = "//form/div[3]/div[1]/div/p"
    POSTCODE_FIELD = "//form/div[3]/div[2]/div[1]/p"
    ADDRESS_LINE_1_FIELD = "//form/div[4]/div[1]/div[1]/p"
    DATE_OF_BIRTH_FIELD = "//form/div[6]/div[1]/div[1]/p"
    LANGUAGE_FIELD = "//form/div[6]/div[2]/div[1]/p"

    def __init__(self, browser):
        PortalBasePage.__init__(self, browser)

        try:
            self.__first_name = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.FIRST_NAME_FIELD}"))
            )
            self.__last_name = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.LAST_NAME_FIELD}"))
            )
            self.__email = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.EMAIL_FIELD}"))
            )
            self.__phone = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.PHONE_FIELD}"))
            )
            self.__country = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.COUNTRY_FIELD}"))
            )
            self.__postcode = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.POSTCODE_FIELD}"))
            )
            self.__address_line_1 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.ADDRESS_LINE_1_FIELD}"))
            )
            self.__date_of_birth = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.DATE_OF_BIRTH_FIELD}"))
            )
            self.__language = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestSeePersonalInformation.LANGUAGE_FIELD}"))
            )
        except TimeoutException as e:
            logger.debug("Some of the elements are not found on page  - personal information's")

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_country(self):
        return self.__country

    def get_postcode(self):
        return self.__postcode

    def get_address_line_1(self):
        return self.__address_line_1

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_language(self):
        return self.__language

    def check_personal_information(self, first_name, last_name, email, phone, country, postcode, address_line1, date_of_birth, language = None):

        try:
            assert self.get_first_name().__getattribute__("text") == first_name
            assert self.get_last_name().__getattribute__("text") == last_name
            assert self.get_email().__getattribute__("text") == email
            assert self.get_phone().__getattribute__("text") == convert_star_to_blk_space(phone)
            assert self.get_country().__getattribute__("text") == convert_star_to_blk_space(country)
            assert self.get_postcode().__getattribute__("text") == postcode
            assert self.get_address_line_1().__getattribute__("text") == address_line1
            assert self.get_date_of_birth().__getattribute__("text") == date_of_birth
        except AssertionError as ae:
            print(f"Assertion error accured! {ae}")
