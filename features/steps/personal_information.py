from features.lib.source.pageObject.pages.login import LoginPage
from features.lib.source.pageObject.tests.test_verify_user_account_page import TestVerifyUserSignupAccountMainPage
from features.lib.source.pageObject.tests.test_see_personal_information import TestSeePersonalInformation
from features.helpers.processing import *
from behave import *

use_step_matcher("re")


@given("that user is logged in with personal information's (?P<email>.+) (?P<password>.+)")
def step_impl(context, email, password):
    login_page = LoginPage(context.browser)
    login_page.login_user(email, password)



@step("user should be successfully logged in and redirected to his account page with title (?P<page_title>.+) (?P<first_name>.+) (?P<last_name>.+)")
def step_impl(context, page_title, first_name, last_name):
    user_verification = TestVerifyUserSignupAccountMainPage(context.browser)
    try:
        assert user_verification.get_page_title() == f'{convert_star_to_blk_space(page_title)}'
        assert user_verification.get_user_first_last_name_text() == f'{first_name} {last_name}[Logout]'
    except AssertionError:
        print(f'One of the assertions failed on user account page - conformation - page title or user onscreen name!')


@when("user clicks on Personal information tab")
def step_impl(context):
    personal_information = TestSeePersonalInformation(context.browser)
    personal_information.get_personal_information_tab().click()


@then("user should see his personal information's like (?P<first_name>.+) (?P<last_name>.+) (?P<email>.+) (?P<password>.+) (?P<date_of_birth>.+) (?P<country>.+) (?P<postcode>.+) (?P<address_line_1>.+) (?P<city_or_town>.+) (?P<phone>.+)")
def step_impl(context, first_name, last_name, email, password, date_of_birth, country, postcode, address_line_1, city_or_town, phone):
    personal_information = TestSeePersonalInformation(context.browser)
    personal_information.check_personal_information(first_name, last_name, email, phone, country, postcode, address_line_1, date_of_birth)
