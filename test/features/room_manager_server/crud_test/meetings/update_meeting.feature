@CRUD @meetings @room_manager_server
Feature: PUT /meetings CRUD

  Background: Create meeting with Administrator credentials
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
            "attendees": ["daniel@manual.local"],
            "optionalAttendees": []
          }
        """
    And I prepare following header
      | Credentials                 |
      | __ADMINISTRATOR_CREDENTIALS |
    And I send create request


  Scenario: Create meeting with Administrator credentials
    Given I PUT to /meetings
    When I prepare following body
        """
          {
            "organizer": "lab1@manual.local",
            "subject": "Scrum Test PUT",
            "body": "Test meeting PUT",
            "start": "2018-07-12",
            "end": "2018-07-12T21:07:19.472Z",
            "rooms": [
              "lab1@manual.local"
            ],
            "attendees": [
              "jin@manual.local"
            ],
            "optionalAttendees": [

            ]
          }
        """
    And I prepare following header
      | Credentials                 |
      | __ADMINISTRATOR_CREDENTIALS |
    And I send update request
    Then I should get response with status code 200
    And I should validate the meeting schema received
    And I should validate the response contains the body json sent
