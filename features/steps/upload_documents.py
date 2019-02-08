from features.lib.source.pageObject.tests.test_upload_documents import UploadDocuments
from behave import *

use_step_matcher("re")


@when("user clicks on upload documents tab")
def step_impl(context):
    upload_documents_page = UploadDocuments(context.browser)
    upload_documents_page.upload_documents_tab_click()


@step("performs drag&drop of the documents")
def step_impl(context):
    upload_documents_page = UploadDocuments(context.browser)
    upload_documents_page.drop_files()
