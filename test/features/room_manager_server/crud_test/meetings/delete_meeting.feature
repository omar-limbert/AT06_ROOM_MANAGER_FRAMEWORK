@CRUD @meetings @room_manager_server
Feature: DELETE /meetings/{meetingId}

  @create_meeting
  Scenario: Delete an existing meeting by id

    When I DELETE to /meetings
    And I prepare following header
      | Credentials                 | ServiceName    |
      | __ADMINISTRATOR_CREDENTIALS | ExchangeServer |
    And I prepare meeting_id saved before in create meeting hook
    And I send the request
    Then I should get response with status code 204
    And I should validate schema received with  meeting schema on meetings folder
    And I should validate the response contains the body json sent