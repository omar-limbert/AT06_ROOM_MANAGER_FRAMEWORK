@CRUD @services @room_manager_server
Feature: POST /services CRUD

  @delete_service
  Scenario: Create services with Administrator credentials

    Given I POST to /services
    When I prepare following body
        """
          {
            "type": "ExchangeServer",
            "hostname": "am-agent-1-cons.manual.local",
            "username": "manual\\Administrator",
            "password": "Control1234!",
            "deleteLockTime": 10
          }
        """
    And I send the request
    Then I should get response with status code 200
#    And I should validate schema received with  services schema on services folder
    And I should validate the response contains the body json sent
