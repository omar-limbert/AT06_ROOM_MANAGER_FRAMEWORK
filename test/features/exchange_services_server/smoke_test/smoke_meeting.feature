@smoke @exchange_server
Feature: Smoke test to validate if meetings service is available

  Scenario: Get data from /meetings
    Given I GET to /meetings
    And I send the request
    Then I should get response with status code 200