Feature: Smoke test to validate if server is running

  Scenario: Get information from Room Manager server
    Given I have room manager server running
    When I GET to /info
    And I send the request
    And I prepare following table
     | organizer | subject                            | body | start                    | end                      | rooms       | attendees | optionalAttendees |
      | __USER1   | Create meeting to Test room status | Test | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | __USER_ROOM | __USER1   | __USER2           |

    Then I should get response with status code 200
    And I should validate the server schema received