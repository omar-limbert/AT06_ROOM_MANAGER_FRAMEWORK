@CRUD @meetings_exchange @exchange_server
Feature: POST /meetings

  Scenario: Create meeting with Administrator credentials

    Given I POST to /meetings
    When I prepare following body
        """
          {
            "to": [
              "candace.flynn@server.lab"
            ],
            "cc": [
              "candace.flynn@server.lab"
            ],
            "bcc": [
              "candace.flynn@server.lab"
            ],
            "subject": "Scrum",
            "body": "Scrum of Room Manager"
          }
        """
    And I prepare following header
      | Exchange-Credentials        | Exchange-Calendar |
      | __ADMINISTRATOR_CREDENTIALS | __ROOM1           |
    And I send the request
    And I keep the "id" as "$item_id" from JSON response
    Then I should get response with status code 201
    And I should validate schema received with  meeting_exchange schema on meetings_exchange folder
    And I should validate the response contains the body json sent