@functional @negative @meetings @exchange_server
Feature: POST /meetings Functional
  Scenario Outline: POST meetings with Administrator credentials and invalid Id meetings
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
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6f224a0b3bda04ba8"  |
      | "bWludWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzEh"| "5b4fbe6f224a0b3bda04ba822"|
      | "F0b3I6Q29udHJvbDEyN0cmF0b3I6Q29udHJvbDEyMzQh"| "5b4fbe6"                  |
      | "AW0PFuFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "aaaaaaaaaaaaaaaaaaaaaaaaA"|
      | "bWFudWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "/////////////////////////"|
      | "857qdWFsXGFkbWluaXN0cmF0b3I6Q29udHJvbDEyMzQh"| "2018-06-29T15:51:44.368Z" |
      | "3I6Q29udHJbWlubdHJvbDb3IF0b3IF0bdHJvbDEyMzQh"| "TTTTTTTTTTTTTTTTTTTTTTTT" |
