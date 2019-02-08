# Created by nemanja.talijan at 1/26/19
Feature: User signup
  Registration of a new user

  Scenario Outline: User signup with valid data
    Given that user is on Signup page with <page_title_welcome>
    When user enters personal information's like <first_name> <last_name> <email> <password>
    And chooses country flag like <country_flag>
    And enters <phone> number
    And enters personal details like <date_of_birth> <country> <postcode> <address_line_1> <city_or_town>
    And clicks on Next button
    And answer on questions HAVE YOU TRADED IN ANY OF THE FOLLOWING IN THE PAST THREE YEARS? with multiple answers for next tradings <shares> <forex> <cfds> <spread_betting>
    And answer on question OTHER RELEVANT EXPERIENCE? <have_you>
    And answer on question about financier's <trading_platform> <trading_currency> <approximate_annual_income> <employment_status> <approximate_value_of_assets>
    And clicks on Terms & Conditions agreement
    And clicks on Finnish button
    Then user should be successfully signed up and redirected to his account page with title <page_title> <first_name> <last_name>
    Examples:
      |page_title_welcome| page_title | first_name | last_name | email | password | country_flag | phone | date_of_birth | country | postcode | address_line_1 | city_or_town | shares | forex | cfds | spread_betting | have_you | trading_platform | trading_currency | approximate_annual_income | employment_status | approximate_value_of_assets |
      |TradeCore - Step 1 \| Registration| TradeCore - Account | Nemanja | last_name | email@tradecore.com | Password1 | country_flag | 69111111 | 01/01/1990 | Nigeria | postcode | address_line_1 | city_or_town | No | No | No | No | Attended a relevant training course | MT5 | USD | Over $100,000 | Employed | Self Employed |