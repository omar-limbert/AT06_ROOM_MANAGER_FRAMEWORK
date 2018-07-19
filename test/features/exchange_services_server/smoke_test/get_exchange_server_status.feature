@smoke @exchange_server
Feature: Smoke test to validate if exchange server is running

  Scenario: Get information from Exchange server
    Given I have Exchange Server running
    When I GET to /info
    And I send the request
    Then I should get response with status code 200