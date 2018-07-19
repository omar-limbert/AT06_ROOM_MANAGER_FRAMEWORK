@functional @negative @meetings @exchange_server
Feature: PUT /meetings Negative
  Scenario Outline: PUT meetings with invalid Administrator credentials
    Given I PUT to /meetings
     When I prepare following header
      | Credentials                 |
      | <ADMINISTRATOR_CREDENTIALS> |
    And I prepare following body
      """
        {
           "subject": "Scrum Test",
           "body": "Test meeting",
           "start": "2018-07-15T21:07:19.000Z",
           "end": "2018-07-19T21:07:19.000Z",
           "location": "lab1@manual.local,lab2@manual.local",
           "attendees" : [
              "Jin@manual.local",
              "roger@manual.local",
              "lab1@manual.local",
              "lab2@manual.local"
           ],
           "optionalAttendees" : [
              "ivan@manual.local",
              "daniel@manual.local"
           ]
        }
      """
    And I send the request
    Then I should get response with status code 404

    Examples:
      | ADMINISTRATOR_CREDENTIALS                     |
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"|
      | "bWludWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzEh"|
      | "F0b3I6Q29udHJvbDEyN0cmF0b3I6Q29udHJvbDEyMzQh"|
      | "AW0PFuFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"|
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"|
      | "857qdWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"|
      | "3I6Q29udHJbWlubdHJvbDb3IF0b3IF0bdHJvbDEyMzQh"|
