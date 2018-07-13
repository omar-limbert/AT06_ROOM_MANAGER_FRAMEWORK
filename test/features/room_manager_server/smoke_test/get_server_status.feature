Feature: Smoke test to validate if server is running

  Scenario: Get information from Room Manager server
    Given I have room manager server running
    When I GET to /info
    And I send the request
    Then I should get response with status code 200