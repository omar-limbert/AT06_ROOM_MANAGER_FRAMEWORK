@functional_negative @equipment @room_manager_server
Feature: POST /equipments CRUD

  Scenario Outline: Create equipments with Administrator credentials and different data.

    Given I POST to /equipments
    When I prepare following table
      | name   | displayName    | icon   |
      | <NAME> | <DISPLAY_NAME> | <ICON> |
    And I send the request
    Then I should get response with status code 200
    And I should validate schema received with  equipment schema on equipments folder
    And I should validate the response contains the body json sent
    Examples:
      | NAME          | DISPLAY_NAME         | ICON              |
      | "DataDisplay" | "Data"               | "dt_icon"         |
      | "DataDisplay" | "!@#$%^&"            | "!@#$%^&"         |
      | "DataDisplay" |                      |                   |
      | "!@#$%^&"     |                      |                   |
      | "!@#$%^&"     |                      | "valid_icon"      |
      | "!@#$%^&"     | "valid_display_name" | "!@#$%^&"         |
      |               |                      | "!@#$%^&"         |
      |               | "valid_display_name" |                   |
      |               | "!@#$%^&"            | "valid_icon"      |
      | "Duplicated"  | "Duplicated Data"    | "duplicated_icon" |
      | "Duplicated"  | "Duplicated Data"    | "duplicated_icon" |
      |               |                      |                   |


  @create_equipment
  Scenario Outline: Update an existent equipment by id with Administrator credentials and different data.
    When I PUT to /equipments
    When I prepare following table
      | name   | displayName    | icon   |
      | <NAME> | <DISPLAY_NAME> | <ICON> |
    And I send the request
    Then I should get response with status code 200
    And I should validate schema received with  equipment schema on equipments folder
    And I should validate the response contains the body json sent
    Examples:
      | NAME          | DISPLAY_NAME         | ICON              |
      | "DataDisplay" | "Data"               | "dt_icon"         |
      | "DataDisplay" | "!@#$%^&"            | "!@#$%^&"         |
      | "DataDisplay" |                      |                   |
      | "!@#$%^&"     |                      |                   |
      | "!@#$%^&"     |                      | "valid_icon"      |
      | "!@#$%^&"     | "valid_display_name" | "!@#$%^&"         |
      |               |                      | "!@#$%^&"         |
      |               | "valid_display_name" |                   |
      |               | "!@#$%^&"            | "valid_icon"      |
      | "Duplicated"  | "Duplicated Data"    | "duplicated_icon" |
      | "Duplicated"  | "Duplicated Data"    | "duplicated_icon" |
      |               |                      |                   |