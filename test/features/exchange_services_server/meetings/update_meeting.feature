@CRUD @meetings_exchange @exchange_server
Feature: PUT/meetings/{meetingId}

  Background: Create a meeting with Administrator credentials
    Given I POST to /meetings
    When I prepare following body
        """
          {
            "subject": "Scrum tomorrow",
            "body": "Scrum of Room Manager 3",
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

  Scenario: Update an existent meeting by id
    Given I PUT to /meetings
    When I prepare following body
        """
          {
            "subject": "Scrum today",
            "body": "Scrum of Room Manager 3",
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
    Then I should get response with status code 200
    And I should validate schema received with  meeting_exchange schema on meeting_exchange folder
    And I should validate the response contains the body json sent

