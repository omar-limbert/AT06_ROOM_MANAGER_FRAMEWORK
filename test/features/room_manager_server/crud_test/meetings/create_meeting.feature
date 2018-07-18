@CRUD @meetings @room_manager_server
Feature: POST /meetings

  Scenario: Create meeting with Administrator credentials

    Given I POST to /meetings
    When I prepare following body
        """
          {
            "organizer": "__ADMINISTRATOR_EMAIL",
            "subject": "Subject test",
            "body": "Body test",
            "start": "2018-08-01T20:00:00.000Z",
            "end": "2018-08-01T20:30:00.000Z",
            "rooms": [
              "__ROOM1",
              "__ROOM2"
            ],
            "attendees": ["__USER1_EMAIL", "__USER2_EMAIL"],
            "optionalAttendees": []
          }
        """
    And I prepare following header
      | Credentials                 |
      | __ADMINISTRATOR_CREDENTIALS |
    And I send the request
    And I keep the "id" as "$item_id" from JSON response
    Then I should get response with status code 201
    And I should validate schema received with  meeting schema on meetings folder
    And I should validate the response contains the body json sent
