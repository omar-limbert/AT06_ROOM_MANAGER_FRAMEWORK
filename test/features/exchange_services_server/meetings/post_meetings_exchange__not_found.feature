@functional @negative @meetings @exchange_server
Feature: POST /meetings Functional
  Scenario Outline: POST meetings with Administrator credentials and invalid Id meeting
    Given I POST to /meetings
     When I prepare following header
      | Credentials                 |
      | <ADMINISTRATOR_CREDENTIALS> |
    And I prepare following table
      | meetingId                |
      | <ID_MEETING>             |
    And I send the request
    Then I should get response with status code 404

    Examples: Not Found
      | ADMINISTRATOR_CREDENTIALS                     | ID_MEETING                 |
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba82"|
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "0b4fbe6f224a0b3bda04bb82"|
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "999999999999999999999999"|
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "eeeeeeeeeeeeeeeeeeeeeeee"|

