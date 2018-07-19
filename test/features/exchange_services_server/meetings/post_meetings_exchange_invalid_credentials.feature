@functional @negative @meetings @exchange_server
Feature: POST /meetings Functional
  Scenario Outline: POST meetings with Administrator invalid credentials and  Id meetings
    Given I POST to /meetings
     When I prepare following header
      | Credentials                 |
      | <ADMINISTRATOR_CREDENTIALS> |
    And I prepare following table
      | meetingId                |
      | <ID_MEETING> |
    And I send the request
    Then I should get response with status code 401

    Examples:
      | ADMINISTRATOR_CREDENTIALS                     | ID_MEETING                 |
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba82"  |
      | "bWludWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzEh"| "5b4fbe6f224a0b3bda04ba82"|
      | "F0b3I6Q29udHJvbDEyN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba85"                  |
      | "AW0PFuFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba82"|
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba82"|
      | "857qdWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba82" |
      | "3I6Q29udHJbWlubdHJvbDb3IF0b3IF0bdHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba82" |
