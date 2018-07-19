@smoke @exchange_accounts @exchange_server
Feature: GET /exchange_accounts Smoke
  Scenario: Get exchange account with name
    Given I GET to /exchangeAccounts
    When I prepare following table
      | displayName      | userPrincipalName      |
      | __DISPLAY_NAME   | __USER1_EMAIL       |
    And I send the request
    Then I should get response with status code 200

