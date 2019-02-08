Feature: Upload documents
  User can upload personal documents as a proof

  Scenario Outline: uploading the documents
    Given that user is logged in with personal information's <email> <password>
    And user should be successfully logged in and redirected to his account page with title <page_title> <first_name> <last_name>
    When user clicks on upload documents tab
    And performs drag&drop of the documents
    Examples:
      | email | password | page_title | first_name | last_name |
      |john.doe@gmail.com|Password1|TradeCore*-*Account|John|Doe|