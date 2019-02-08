from features.lib.source.pageObject.pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from features.helpers.processing import *
from features.logger import *

logger = set_logger()


class SignUp(Base):

    FIRST_NAME_TEXT_INPUT_FIELD_BY_ID = "form-first_name"
    LAST_NAME_TEXT_INPUT_FIELD_BY_ID = "form-last_name"
    EMAIL_TEXT_INPUT_FIELD_BY_ID = "form-email"
    PASSWORD_TEXT_INPUT_FIELD_BY_ID = "form-password"
    PHONE_COUNTY_FLAG = "country-name"
    PHONE_TEXT_INPUT_FIELD_BY_ID = "form-telephone"
    DATE_OF_BIRTH_TEXT_INPUT_FIELD_BY_ID = "form-date_of_birth"
    COUNTRY_DROPDOWN_BY_ID = "form___fieldId___chosen"
    POSTCODE_TEXT_INPUT_FIELD_BY_ID = "form-addr_zip"
    ADDRESS_1_TEXT_INPUT_FIELD_BY_ID = "form-addr_street"
    ADDRESS_2_TEXT_INPUT_FIELD_BY_ID = "form-addr_line_2"
    CITY_OR_TOWN_TEXT_INPUT_FIELD_BY_ID = "form-addr_city"
    NEXT_BUTTON_BUTTON_BY_ID = "button-step"
    PAGE_TITLE = "TradeCore - Step 1 | Registration"

    def __init__(self, browser):
        Base.__init__(self, browser)
        try:
            self.__first_name = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, f"{SignUp.FIRST_NAME_TEXT_INPUT_FIELD_BY_ID}"))
            )
            self.__last_name = self.browser.find_element(By.ID, f"{SignUp.LAST_NAME_TEXT_INPUT_FIELD_BY_ID}")
            self.__email = self.browser.find_element(By.ID, f"{SignUp.EMAIL_TEXT_INPUT_FIELD_BY_ID}")
            self.__password = self.browser.find_element(By.ID, f"{SignUp.PASSWORD_TEXT_INPUT_FIELD_BY_ID}")
            self.__phone = self.browser.find_element(By.ID, f"{SignUp.PHONE_TEXT_INPUT_FIELD_BY_ID}")
            self.__date_of_birth = self.browser.find_element(By.ID, f"{SignUp.DATE_OF_BIRTH_TEXT_INPUT_FIELD_BY_ID}")
            self.__country = self.browser.find_element(By.ID, f"{SignUp.COUNTRY_DROPDOWN_BY_ID}")
            self.__postcode = self.browser.find_element(By.ID, f"{SignUp.POSTCODE_TEXT_INPUT_FIELD_BY_ID}")
            self.__address_1 = self.browser.find_element(By.ID, f"{SignUp.ADDRESS_1_TEXT_INPUT_FIELD_BY_ID}")
            self.__city_or_town = self.browser.find_element(By.ID, f"{SignUp.CITY_OR_TOWN_TEXT_INPUT_FIELD_BY_ID}")
            self.__next_button = self.browser.find_element(By.ID, f"{SignUp.NEXT_BUTTON_BUTTON_BY_ID}")
            self.__country_choice = None
            self.__page_title = SignUp.PAGE_TITLE
        except (ElementNotVisibleException, TimeoutException) as e:
            logger.debug("Some element is not visible!")

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_phone(self):
        return self.__phone

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_country(self):
        return self.__country

    def get_country_click(self, country):
        self.__country_choice = self.browser.find_element(By.XPATH, f"//*[@class=\"active-result\" and contains(.,'{country}')]")
        return self.__country_choice

    def choose_country(self, country):
        self.get_country().click()
        self.get_country_click(country).click()

    def get_postcode(self):
        return self.__postcode

    def get_address1(self):
        return self.__address_1

    def set_address1(self, address1):
        self.get_address1().clear()
        self.get_address1().send_keys(address1)

    def get_city(self):
        return self.__city_or_town

    def set_city(self, city):
        self.get_city().clear()
        self.get_city().send_keys(city)

    def get_next(self):
        return self.__next_button

    def click_next(self):
        self.get_next().click()
        time.sleep(2)

    def scroll_page(self):
        self.browser.execute_script("window.scrollTo(0, 1080)")

    def set_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)

    def set_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)

    def set_phone(self, phone):
        self.get_phone().clear()
        self.get_phone().send_keys(phone)

    def set_postcode(self, postcode):
        self.get_postcode().clear()
        self.get_postcode().send_keys(postcode)

    def get_page_title(self):
        return self.__page_title

    def populate_personal_info(self, first_name, last_name, email, password):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.get_email().clear()
        email = create_email_variant(email)
        self.get_email().send_keys(email)
        self.get_password().clear()
        self.get_password().send_keys(password)

    def populate_personal_details(self, date_of_birth, country, postcode, address_line_1, city_or_town):
        self.get_date_of_birth().clear()
        self.get_date_of_birth().send_keys(date_of_birth)
        self.choose_country(country)
        self.set_postcode(postcode)
        self.set_address1(address_line_1)
        self.set_city(city_or_town)
