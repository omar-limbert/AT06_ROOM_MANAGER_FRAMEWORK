@CRUD @meetings @exchange_server
Feature: POST /meetings

  Scenario: Create meeting with Administrator credentials

    Given I POST to /meetings
    When I prepare following body
        """
          {
            "subject": "Scrum",
            "body": "Scrum of Room Manager",
            "start": "2019-01-25T16:00:00.00Z",
            "end": "2019-01-25T17:00:00.00Z",
            "location": "Cochabamba",
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
      | __ADMINISTRATOR_CREDENTIALS | __ROOM1              |
    When I send create request
    Then I should get response with status code 200
    And I should validate the meeting_exchange schema received
    And I should validate the response contains the body json sent
