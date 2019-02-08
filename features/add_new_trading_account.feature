Feature: Creating new trading account
  User can add new trading account by choosing currency and trading platform

  Scenario Outline: User can add trading account
    Given that user is logged in with personal information's <email> <password>
    And user should be successfully logged in and redirected to his account page with title <page_title> <first_name> <last_name>
    When user clicks on add trading account button
    And chooses type of currency
    And clicks on create
    Examples:
      | email | password | page_title | first_name | last_name |
