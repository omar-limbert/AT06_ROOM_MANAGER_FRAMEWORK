@CRUD @negative @subscriptions @exchange_server
Feature: POST /subscriptions with invalid values

  Scenario: Create subscription with parameters missing
    Given I POST to /subscriptions
    And I prepare following body
        """
          {
          "host": "localhost",
          "port": 7070,
          "notificationUrl": "/api/v1/notifications"
        }
        """
    When I send the request
    And I should get response with status code 409
    Then The response should display service "ConflictValue"