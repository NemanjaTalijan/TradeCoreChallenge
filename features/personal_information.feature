Feature: User personal information's
  User can see can see personal information's

  Scenario Outline: User can see personal information's on portal
    Given that user is logged in with personal information's <email> <password>
    And user should be successfully logged in and redirected to his account page with title <page_title> <first_name> <last_name>
    When user clicks on Personal information tab
    Then user should see his personal information's like <first_name> <last_name> <email> <password> <date_of_birth> <country> <postcode> <address_line_1> <city_or_town> <phone>
    Examples:
      |email| password|page_title|first_name|last_name|date_of_birth|country|postcode|address_line_1|city_or_town|phone|
      |john.doe@gmail.com|Password1|TradeCore*-*Account|John|Doe|01/01/2001|United*States|postcode|address1|city|3*816*611-1111|
