@CRUD @equipment @room_manager_server
Feature: DELETE /meetings/{meetingId}

  Background: Create meeting with Administrator credentials
    Given I POST to /equipments
    When I prepare following table
      | name        | displayName | icon    |
      | DataDisplay | Data        | dt_icon |
    And I send the request
    And I keep the "id" as "$item_id" from JSON response

  Scenario: Delete an existing equipment by id

    When I DELETE to /equipments
    And I send the request
    Then I should get response with status code 204
    And I should validate schema received with  equipment schema on equipments folder
    And I should validate the response contains the body json sent