@smoke @exchange_server
Feature: Smoke test to validate if Exchange Accounts service is available

  Scenario: Get data from /exchangeAccounts
    Given I GET to /exchangeAccounts
    And I send the request
    Then I should get response with status code 200