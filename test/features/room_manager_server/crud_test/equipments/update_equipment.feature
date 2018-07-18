@CRUD @equipment @room_manager_server
Feature: PUT/equipments/{equipmentId}

  @create_equipment
  Scenario: Update an existent equipment by id
    When I PUT to /equipments
    When I prepare following table
      | name      | displayName | icon    |
      | HeadSet 1 | Headset     | hs_icon |
    And I send the request
    Then I should get response with status code 200
    And I should validate schema received with  equipment schema on equipments folder
    And I should validate the response contains the body json sent

