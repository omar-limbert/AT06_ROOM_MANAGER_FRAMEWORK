@CRUD @rooms @room_manager_server
Feature:  GET /rooms CRUD

  Scenario: Get rooms with Administrator credentials

    Given I GET to /rooms
    When I prepare following table
      | owner                       | start                    |
      | __ADMINISTRATOR_CREDENTIALS | 2018-08-12T12:00:00.000Z |
    And I send the request
    Then I should get response with status code 200
