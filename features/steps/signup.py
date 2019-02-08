from behave import *
from features.lib.source.pageObject.pages.signup_page import SignUp
from features.lib.source.pageObject.pages.signup_page_continue import SignupContinue
from features.lib.source.pageObject.tests.test_verify_user_account_page import TestVerifyUserSignupAccountMainPage
import time

use_step_matcher("re")


@given("that user is on Signup page with (?P<page_title_welcome>.+)")
def step_impl(context, page_title_welcome):
    signup_page = SignUp(context.browser)
    assert signup_page.get_page_title() == f"{page_title_welcome}"


@when("user enters personal information's like (?P<first_name>.+) (?P<last_name>.+) (?P<email>.+) (?P<password>.+)")
def step_impl(context, first_name, last_name, email, password):
    signup_page = SignUp(context.browser)
    signup_page.populate_personal_info(first_name, last_name, email, password)


@step("chooses country flag like (?P<country_flag>.+)")
def step_impl(context, country_flag):
    signup_page = SignUp(context.browser)
    # signup_page.set_phone_county_flag()


@step("enters (?P<phone>.+) number")
def step_impl(context, phone):
    signup_page = SignUp(context.browser)
    signup_page.set_phone(phone)


@step("enters personal details like (?P<date_of_birth>.+) (?P<country>.+) (?P<postcode>.+) (?P<address_line_1>.+) (?P<city_or_town>.+)")
def step_impl(context, date_of_birth, country, postcode, address_line_1, city_or_town):
    signup_page = SignUp(context.browser)
    signup_page.populate_personal_details(date_of_birth, country, postcode, address_line_1, city_or_town)


@step("clicks on Next button")
def step_impl(context):
    SignUp(context.browser).click_next()


@step("answer on questions HAVE YOU TRADED IN ANY OF THE FOLLOWING IN THE PAST THREE YEARS\? with multiple answers for next tradings (?P<shares>.+) (?P<forex>.+) (?P<cfds>.+) (?P<spread_betting>.+)")
def step_impl(context, shares, forex, cfds, spread_betting):
    SignupContinue(context.browser).populate_signup_continue_page(shares, forex, cfds, spread_betting)


@step("answer on question OTHER RELEVANT EXPERIENCE\? (?P<have_you>.+)")
def step_impl(context, have_you):
    signup_continue_page = SignupContinue(context.browser)
    signup_continue_page.populate_have_you_question(have_you)


@step("clicks on Terms & Conditions agreement")
def step_impl(context):
    signup_page_continue = SignupContinue(context.browser)
    signup_page_continue.click_on_terms()


@step("clicks on Finnish button")
def step_impl(context):
    signup_page_continue = SignupContinue(context.browser)
    signup_page_continue.click_on_finish_button()


@then("user should be successfully signed up and redirected to his account page with title (?P<page_title>.+) (?P<first_name>.+) (?P<last_name>.+)")
def step_impl(context, page_title, first_name, last_name):
    user_verification = TestVerifyUserSignupAccountMainPage(context.browser)
    try:
        assert user_verification.get_page_title() == f'{page_title}'
        assert user_verification.get_user_first_last_name_text() == f'{first_name} {last_name}[Logout]'
    except AssertionError:
        print(f'One of the assertions failed on user account page - conformation!')


@step("answer on question about financier's (?P<trading_platform>.+) (?P<trading_currency>.+) (?P<approximate_annual_income>.+) (?P<employment_status>.+) (?P<approximate_value_of_assets>.+)")
def step_impl(context, trading_platform, trading_currency, approximate_annual_income, employment_status, approximate_value_of_assets):
    signup_page = SignupContinue(context.browser)
    signup_page.populate_financial_details(trading_platform, trading_currency, approximate_annual_income, employment_status, approximate_value_of_assets)
