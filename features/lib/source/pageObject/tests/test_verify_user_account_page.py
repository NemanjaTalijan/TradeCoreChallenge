from features.lib.source.pageObject.pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time


class TestVerifyUserSignupAccountMainPage(Base):

    USER_FIRST_LAST_NAME_BY_XPATH = "/html/body/section/div[1]/div/div/div[2]/div[2]"
    PAGE_TITLE_BY_XPATH = "/html/head/title"
    PAGE_TITLE = "TradeCore - Account"

    def __init__(self, browser):
        Base.__init__(self, browser)

        try:
            TestVerifyUserSignupAccountMainPage.get_page_title(self)
            self.__page_title = self.browser.title
            self.__user_first_last_name = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{TestVerifyUserSignupAccountMainPage.USER_FIRST_LAST_NAME_BY_XPATH}"))
            )
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Some of the elements are not found on user account main page! Exception: {e}")

    def get_page_title(self):
        while self.browser.title != f"{TestVerifyUserSignupAccountMainPage.PAGE_TITLE}":
            time.sleep(0.1)
        return self.browser.title

    def get_user_first_last_name_text(self):
        while self.__user_first_last_name.__getattribute__("text") == '[Logout]':
            time.sleep(0.1)
        return self.__user_first_last_name.__getattribute__("text")
