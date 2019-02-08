import string
import random


def id_generator(size=3, chars=string.ascii_lowercase + string.digits):
    return '+' + ''.join(random.choice(chars) for _ in range(size))


def create_email_variant(original_email):
    email_array = original_email.split('@')
    email_array[0] = email_array[0] + id_generator()
    new_email = email_array[0] + '@' + email_array[1]
    return new_email


def check_answer(answer):
    if answer == 'Frequently':
        class_selector = 'active-result highlighted'
    else:
        class_selector = 'active-result'
    return class_selector


def check_answer_other(answer):
    if answer == 'Frequently':
        selector = '1'
    elif answer == 'Sometimes':
        selector = '2'
    elif answer == 'No':
        selector = '3'
    else:
        selector = 1
    return selector


def check_have_you(answer):
    if answer == 'Attended a relevant training course':
        selector = '1'
    elif answer == 'Had experience of working in the financial sector':
        selector = '2'
    elif answer == 'No other relevant experience':
        selector = '3'
    else:
        selector = 1
    return selector


def check_trading_currency(answer):
    if answer == 'USD':
        selector = '1'
    elif answer == 'EUR':
        selector = '2'
    elif answer == 'GBP':
        selector = '3'
    else:
        selector = 1
    return selector


def check_approximate_annual_income(answer):
    if answer == 'Over $100,000':
        selector = '1'
    elif answer == '$50,000 - $99,999':
        selector = '2'
    elif answer == '$15,000 - $49,999':
        selector = '3'
    elif answer == 'Less than $15,000':
        selector = '4'
    else:
        selector = 1
    return selector


def check_employment_status(answer):
    if answer == 'Employed':
        selector = '1'
    elif answer == 'Self Employed':
        selector = '2'
    elif answer == 'Retired':
        selector = '3'
    elif answer == 'Unemployed':
        selector = '4'
    else:
        selector = 1
    return selector


def check_approximate_value_of_assets(answer):
    if answer == 'Over $100,000':
        selector = '1'
    elif answer == '$50,000 - $99,999':
        selector = '2'
    elif answer == '$5,000 - $49,999':
        selector = '3'
    elif answer == 'Less than $5,000':
        selector = '4'
    else:
        selector = 1
    return selector


def convert_star_to_blk_space(string):
    new_string_list = list(string)
    list_len = len(new_string_list)
    for x in range(0, list_len):
        if new_string_list[x] == '*':
            new_string_list[x] = ' '
    new_string = ''.join(new_string_list)
    return new_string
