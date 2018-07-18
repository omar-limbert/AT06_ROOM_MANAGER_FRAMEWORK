@CRUD @meetings
Feature: GET /meetings CRUD

  Scenario: Get meetings with Administrator credentials

    Given I GET to /meetings
    When I set the following parameters for a meeting
      | owner                       | start                    |
      | __ADMINISTRATOR_CREDENTIALS | 2018-08-12T12:00:00.000Z |
    And I prepare following header
      | Credentials |
    And I send the request
    Then I should get response with status code 200
