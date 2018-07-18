@smoke @exchange_server
Feature: Smoke test to validate if Exchange service is available

  Scenario: Get data from /services
    Given I GET to /services
    And I send the request
    Then I should get response with status code 200