@CRUD @meetings @room_manager_server
Feature: PUT /meetings CRUD

  @create_meeting @delete_meeting
  Scenario: Create meeting with Administrator credentials
    Given I PUT to /meetings
    When I prepare following body
        """
          {
            "organizer": "__ADMINISTRATOR_EMAIL",
            "subject": "New Subject",
            "body": "Body test",
            "start": "2018-08-01T20:00:00.000Z",
            "end": "2018-08-01T20:30:00.000Z",
            "rooms": [
              "__ROOM1",
              "__ROOM2"
            ],
            "attendees": ["__USER2_EMAIL"],
            "optionalAttendees": []
          }
        """
    And I prepare following header
      | Credentials                 | ServiceName    |
      | __ADMINISTRATOR_CREDENTIALS | ExchangeServer |
    And I send the request
    Then I should get response with status code 200
    And I should validate schema received with  meeting schema on meetings folder
    And I should validate the response contains the body json sent
