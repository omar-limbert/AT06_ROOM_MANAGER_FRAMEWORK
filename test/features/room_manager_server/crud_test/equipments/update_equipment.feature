@CRUD @equipment @room_manager_server
Feature: PUT/equipments/{equipmentId}

  Background: Create a equipment with Administrator credentials
    Given I POST to /equipments
    When I prepare following table
      | name      | displayName | icon    |
      | HeadSet 1 | Headset     | hs_icon |
    And I send the request
    And I keep the "id" as "$item_id" from JSON response

  Scenario: Update an existent equipment by id
    When I PUT to /equipments
    Then I should get response with status code 200
    And I should validate schema received with  equipment schema on equipments folder
    And I should validate the response contains the body json sent
    And I send the request
