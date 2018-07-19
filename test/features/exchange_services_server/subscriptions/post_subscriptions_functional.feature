@functional @negative @subscriptions @exchange_server
Feature: POST /subscriptions Functional
  Scenario: POST subscriptions with name
    Given I POST to /subscriptions
    When I prepare following body
        """
          {

          }
        """
    And I send the request
    Then I should get response with status code 400

