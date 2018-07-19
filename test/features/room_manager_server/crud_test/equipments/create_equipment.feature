@CRUD @equipment @room_manager_server
Feature: POST /meetings CRUD

  Scenario: Create meeting with Administrator credentials

    Given I POST to /equipments
    When I prepare following table
      | name        | displayName | icon    |
      | DataDisplay | Data        | dt_icon |
     And I send the request
    Then I should get response with status code 201
     And I should validate schema received with  equipment schema on equipments folder
     And I should validate the response contains the body json sent
