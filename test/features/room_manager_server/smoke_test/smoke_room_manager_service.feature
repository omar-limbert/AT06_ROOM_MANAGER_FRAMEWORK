@Smoke @services @room_manager_server
Feature: Smoke GET /services CRUD

  Scenario: Get services with Administrator credentials

    Given I GET to /services
    And I send the request
    Then I should get response with status code 200
