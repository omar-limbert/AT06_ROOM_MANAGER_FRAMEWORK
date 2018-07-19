@smoke @meetings @exchange_server
Feature: GET /meetings Smoke

  Scenario: Get meetings with Administrator credentials
    Given I GET to /meetings
    When I prepare following header
      | Credentials                 | Calendar            |
      | __ADMINISTRATOR_CREDENTIALS | lab1@manual.local   |
     And I prepare following table
      | start                    | end	                    |
      | 2018-05-22T00:00:00.000Z | 2018-09-22T00:00:00.000Z |
    And I send the request
    Then I should get response with status code 200

