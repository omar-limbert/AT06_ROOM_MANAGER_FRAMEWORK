@CRUD @meetings
Feature: POST /meetings CRUD

  Scenario: Create meeting with Administrator credentials

    Given I POST to /meetings
    When I prepare following body
        """
          {
            "organizer": "__ADMINISTRATOR_EMAIL",
            "subject": "Subject test ",
            "body": "Body test",
            "start": "2018-08-01T20:00:00.000Z",
            "end": "2018-08-01T20:30:00.000Z",
            "rooms": [
              "__ROOM1",
              "__ROOM2"
            ],
            "attendees": [],
            "optionalAttendees": []
          }
        """
    And I prepare following header
      | Credentials                 |
      | __ADMINISTRATOR_CREDENTIALS |
    And I send create request
    Then I should get response with status code 200
    And I should validate the meeting schema received
    And I should validate the response contains the body json sent
