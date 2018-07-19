@CRUD @meetings @exchange_server
Feature: POST /meetings

  Scenario: Create meeting with Administrator credentials

    Given I POST to /meetings
    When I prepare following body
        """
          {
            "subject": "Scrum",
            "body": "Scrum of Room Manager",
            "start": "2017-01-25T16:00:00.00Z",
            "end": "2017-01-25T17:00:00.00Z",
            "location": "Arani",
            "attendees": [
              "candace.flynn@server.lab"
            ],
            "optionalAttendees": [
              "stacy.hirano@server.lab"
            ]
          }
        """
    And I prepare following header
      | Exchange-Credentials        | Exchange-Calendar |
      | __ADMINISTRATOR_CREDENTIALS | __ROOM1           |
    And I send the request
    And I keep the "id" as "$item_id" from JSON response
    Then I should get response with status code 201
    And I should validate schema received with  meeting schema on meetings_exchange folder
    And I should validate the response contains the body json sent