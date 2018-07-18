@smoke @room_manager_server
Feature: Smoke test to validate if room manager server is running

  Scenario: Get information from Room Manager server
    Given I have Room Manager Server running
    When I GET to /info
    And I send the request
    Then I should get response with status code 200