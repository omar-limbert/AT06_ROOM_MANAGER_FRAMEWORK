@functional @negative @services @exchange_server
Feature: POST /services Functional
  Scenario: POST services with name
    Given I POST to /services
    When I prepare following body
        """
          {
            "isExchangeOnline": false,
             "hostname": "my.exchange.server",
             "username": "manual\\Administrator",
             "password": "Control1234!"
          }
        """
    And I send the request
    Then I should get response with status code 400

