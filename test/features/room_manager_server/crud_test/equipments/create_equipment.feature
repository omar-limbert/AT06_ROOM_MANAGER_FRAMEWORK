@CRUD @equipment @room_manager_server
Feature: POST /meetings CRUD

  Scenario: Create meeting with Administrator credentials

    Given I POST to /equipments
    When I prepare following table
      | name        | displayName | icon    |
      | DataDisplay | Data        | dt_icon |
    And I send create request
    Then I should get response with status code 200
    And I should validate the equipment schema received
    And I should validate the response contains the body json sent
