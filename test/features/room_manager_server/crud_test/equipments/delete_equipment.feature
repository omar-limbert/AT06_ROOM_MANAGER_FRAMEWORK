@CRUD @meetings @delete
Feature: DELETE /meetings/{meetingId}

  Background: Create meeting with Administrator credentials
    Given I POST to /equipments
    When I prepare following table
      | name           | displayName | icon    |
      | DataDisplay12341 | Data2112    | dt_icon |
    And I send create request

  Scenario: Delete an existing equipment by id

    When I DELETE to /meetings
    And I send delete request
    Then I should get response with status code 204
    And I should validate the meeting schema received
    And I should validate the response contains the body json sent