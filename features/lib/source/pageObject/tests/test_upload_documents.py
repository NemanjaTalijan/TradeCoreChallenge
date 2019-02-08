from features.lib.source.pageObject.pages.portal_page import PortalBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import time


class UploadDocuments(PortalBasePage):

    PAGE_PRESENTS = "//section/div[3]/div[1]/h3"
    PAGE_PRESENTS_TEXT = "//section/div[3]/div[1]/h3"
    ID_PROOF = "/html/body/ui-view/section/div/div/div/div/section/div/div/div/ui-view/section/div[3]/div[1]/div/div[1]/form"
    ID_PROOF_FILE_PATH = "features/test_files/test_file.pdf"
    ID_PROOF_BACK = "//section/div[3]/div[2]/div/div[1]/form"
    ID_PROOF_BACK_FILE_PATH = "features/test_files/test_file.pdf"
    ADDRESS_PROOF = "//section/div[3]/div[3]/div/div[1]/form"
    ADDRESS_PROFF_FILE_PATH = "features/test_files/test_file.pdf"
    ADDITIONAL_CUSTOMER_DOCUMENTS = "//section/div[3]/div[4]/div/div[1]/form"
    ADDITIONAL_CUSTOMER_DOCUMENTS_FILE_PATH = "features/test_files/test_file.pdf"

    def __init__(self, browser):
        PortalBasePage.__init__(self, browser)

        try:
            self.__page_presents = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"{UploadDocuments.PAGE_PRESENTS}"))
            )
            self.check_page_presents()
            # self.__id_proof = WebDriverWait(self.browser, 10).until(lambda driver:
            #      EC.visibility_of_element_located((By.XPATH, f"{UploadDocuments.ID_PROOF}"))
            # )
            self.__id_proof = WebDriverWait(self.browser, 100).until(
                lambda driver: driver.find_element_by_xpath(f"{UploadDocuments.ID_PROOF}"))
            self.__id_prof_back = WebDriverWait(self.browser, 10).until(
                 EC.element_to_be_clickable((By.XPATH, f"{UploadDocuments.ID_PROOF_BACK}"))
            )
            self.__address_proof = WebDriverWait(self.browser, 10).until(
                 EC.element_to_be_clickable((By.XPATH, f"{UploadDocuments.ADDRESS_PROOF}"))
            )
            self.__additional_customer_documents = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"{UploadDocuments.ADDITIONAL_CUSTOMER_DOCUMENTS}"))
            )

        except TimeoutException:
            print("Some of the elements are not visible on page  - Upload documents!")

    def get_page_presents(self):
        return self.__page_presents

    def get_id_proof(self):
        return self.__id_proof

    def send_file_id_proof(self):
        ActionChains(self.browser).send_keys_to_element(self.get_id_proof(), f"{UploadDocuments.ID_PROOF_FILE_PATH}").perform()
        # self.get_id_proof().send_keys(f"{UploadDocuments.ID_PROOF_FILE_PATH}")
        # self.get_id_proof().click()

    def get_id_proof_back(self):
        return self.__id_prof_back

    def send_file_id_prof_back(self):
        self.get_id_proof_back().send_keys(f"{UploadDocuments.ID_PROOF_BACK_FILE_PATH}")

    def get_address_proof(self):
        return self.__address_proof

    def send_file_address_proof(self):
        self.get_address_proof().send_keys(f"{UploadDocuments.ADDRESS_PROFF_FILE_PATH}")

    def get_additional_customer_documents(self):
        return self.__additional_customer_documents

    def send_file_additional_customer_documents(self):
        self.get_additional_customer_documents().send_keys(f"{UploadDocuments.ADDITIONAL_CUSTOMER_DOCUMENTS_FILE_PATH}")

    def check_page_presents(self):

        while self.get_page_presents().text != 'ID Proof':
            time.sleep(0.1)

    def drop_files(self):
        self.send_file_id_proof()
        self.scroll_page(200)
        self.send_file_id_prof_back()
        self.scroll_page(200)
        self.send_file_address_proof()
        self.scroll_page(200)
        self.send_file_additional_customer_documents()
