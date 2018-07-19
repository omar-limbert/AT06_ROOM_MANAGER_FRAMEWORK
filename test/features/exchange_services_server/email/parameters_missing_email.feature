@CRUD @negative @email @exchange_server
Feature: POST /email with parameters missing

  Scenario: Create email with body parameter "to" missing
    Given I POST to /email
    When I prepare following body
        """
          {
            "cc": [
              "lab1@manual.local"
            ],
            "bcc": [
              "lab1@manual.local"
            ],
            "subject": "Scrum Cancelled",
            "body": "Scrum of Room Manager Cancelled"
          }
        """
    And I prepare following header
      | Exchange-Credentials        | Exchange-Calendar |
      | __ADMINISTRATOR_CREDENTIALS | __ROOM1           |
    And I send the request
    Then I should get response with status code 400
    And The response should display service "ServiceNotFoundError"