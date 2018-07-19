@CRUD @services @room_manager_server
Feature: DELETE /services/{meetingId}

  @create_service
  Scenario: Delete an existing service by id

    When I DELETE to /services
    And I prepare service_id saved before in create meeting hook
    And I send the request
    Then I should get response with status code 200
    And I should validate schema received with  services schema on services folder
    And I should validate the response contains the body json sent