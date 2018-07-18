@smoke @exchange_server
Feature: Smoke test to validate if ldap Account service is available

  Scenario: Get data from /ldapAccount
    Given I GET to /ldapAccount
    When I prepare following header
      | Exchange-Credentials        |
      | __ADMINISTRATOR_CREDENTIALS |
    And I prepare following table
      | hostname     |
      | manual.local |
    And I send the request
    Then I should get response with status code 200