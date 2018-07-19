@CRUD @meetings_exchange @exchange_server
Feature: DELETE /meetings/{meetingId}

  @create_meeting_exchange
  Scenario: Delete an existing meeting by id

    When I DELETE to /meetings
    And I prepare following header
      | Exchange-Credentials        | Exchange-Calendar |
      | __ADMINISTRATOR_CREDENTIALS | __ROOM1   |
    And I prepare meeting_id saved before in create meeting hook
    And I send the request
    Then I should get response with status code 204
    And I should validate schema received with  meeting_exchange schema on meeting_exchange folder
    And I should validate the response contains the body json sent