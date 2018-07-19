@smoke @exchange_accounts @exchange_server
Feature: GET /exchange_accounts Smoke
  Scenario: Get exchange account with name
    Given I GET to /exchangeAccounts
    When I prepare following table
      | displayName      | userPrincipalName      |
      | Jimmy JR. Romero | jin@manual.local       |
    And I send the request
    Then I should get response with status code 200

