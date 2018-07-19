@CRUD @service @room_manager_server
Feature: GET/services/{equipmentId}

  @create_service @delete_service
  Scenario: Obtain an existent service by id
    When I GET to /services
    Then I should get response with status code 200
    And I should validate schema received with  services schema on services folder
    And I should validate the response contains the body json sent
    And I send the request