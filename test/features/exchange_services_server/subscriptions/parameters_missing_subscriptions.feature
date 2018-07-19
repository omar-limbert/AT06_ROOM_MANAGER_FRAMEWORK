@CRUD @negative @subscriptions @exchange_server
Feature: POST /subscriptions with invalid values

  Scenario: Create subscription with parameters missing
    Given I POST to /subscriptions
    When I prepare following body
        """
          {
            "host": "manual.local",
            "notificationUrl": "/api/v1/notifications"
          }
        """
    And I send the request
    Then I should get response with status code 400
    And I should validate schema received with  negative schema on negative folder
    And The response should display service "SchemaValidationError"