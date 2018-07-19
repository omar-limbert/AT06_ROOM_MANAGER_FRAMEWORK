@negative @meetings @room_manager_server
Feature: /meetings Functional

  @delete_meeting
  Scenario Outline: Create meetings with Administrator credentials and sent different data.
    Given I POST to /meetings
    When I prepare following body
        """
          {
            "organizer": <ORGANIZER>,
            "subject": "Subject test",
            "body": "Body test",
            "start": <START>,
            "end": <END>,
            "rooms": [
              <ROOM_1>
            ],
            "attendees": ["__USER1_EMAIL", "__USER2_EMAIL"],
            "optionalAttendees": []
          }
        """
    And I prepare following header
      | Credentials                 | ServiceName    |
      | __ADMINISTRATOR_CREDENTIALS | ExchangeServer |
    And I send the request
    And I keep the "id" as "$item_id" from JSON response
    Then I should get response with status code 201

    And I should validate the response contains the body json sent

    Examples:
      | ORGANIZER               | START                      | END                        | ROOM_1    | ROOM_1    |
      | "__ADMINISTRATOR_EMAIL" | "2018-08-01T20:00:00.000Z" | "2018-08-01T20:30:00.000Z" | "__ROOM2" | "__ROOM2" |
      | "__ADMINISTRATOR_EMAIL" | "2018-08-01T20:00:00.000Z" | "2018-08-01T20:30:00.000Z" | "__ROOM1" | "__ROOM1" |
      | "__ADMINISTRATOR_EMAIL" | "2018-08-01T20:00:00.000Z" | "2018-08-01T20:30:00.000Z" | "__ROOM1" | "__ROOM2" |
      | "__ADMINISTRATOR_EMAIL" | "2018-08-01T20:00:00.000Z" | "2018-08-01T20:30:00.000Z" | "__ROOM2" | "__ROOM1" |
