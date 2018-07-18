@CRUD @meetings @exchange_server
Feature: PUT /meetings/{meetingId}

  Background: Create a meeting
    Given I POST to /meetings
    When I prepare following body
        """
          {
            "subject": "Scrum Today",
            "body": "Scrum of Room Manager",
            "start": "2019-01-25T16:00:00.00Z",
            "end": "2019-01-25T17:00:00.00Z",
            "location": "Sacaba",
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
    When I send create request
    Then I keep the "id" as "$id_meeting" from the previous step

  Scenario: Updating an existing meeting

    When I PUT to /meetings
    And I prepare following body
         """
          {
            "subject": "Scrum Tomorrow",
            "body": "Scrum of Room Manager 2",
            "start": "2019-01-26T16:00:00.00Z",
            "end": "2019-01-26T17:00:00.00Z",
            "location": "Sacaba",
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
    And I send update request
    And I construct a expected response
    Then I should get response with status code 200
    And the built expected response should be equal to the obtained response