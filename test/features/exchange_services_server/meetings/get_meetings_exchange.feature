@functional @meetings @exchange_server
Feature: GET /meetings Smoke

  Scenario: Get meetings with Administrator credentials
    Given I GET to /meetings
    When I prepare following table
        | Credentials                 | Calendar            | start                    | end	                    |
        | __ADMINISTRATOR_CREDENTIALS | lab1@manual.local   | 2018-05-22T00:00:00.000Z | 2018-09-22T00:00:00.000Z |
    And I send the request
    Then I should get response with status code 401

