@CRUD @services @room_manager_server
Feature: PUT /services CRUD

  @create_service @delete_service
  Scenario: Update meeting with Administrator credentials
    Given I PUT to /services
    When I prepare following body
        """
          {
          "username": "manual\\Administrator",
          "password": "Control1234!",
          "deleteLockTime": 10
        }
        """
    And I send the request
    Then I should get response with status code 200
    And I should validate schema received with  services schema on services folder
    And I should validate the response contains the body json sent