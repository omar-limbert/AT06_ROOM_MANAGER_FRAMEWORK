@Smoke @equipments @room_manager_server
Feature: Smoke GET /meetings CRUD

  Scenario: Get equipments with Administrator credentials

    Given I GET to /equipments
    And I send the request
    Then I should get response with status code 200
