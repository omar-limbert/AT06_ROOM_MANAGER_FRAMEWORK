@functional @negative @meetings @exchange_server
Feature: POST /meetings Functional
  Scenario Outline: Create a survey invalid inputs
    Given I POST to /meetings
    And I prepare following header
     """
     {
         "_id":"",
         "title":<TITLE>,
         "description":"test",
         "audience":0,
         "settings":{
            "releaseDate":<RELEASE_DATE>,
            "expirationDate":"2018-07-06T15:51:44.366Z",
            "allowedDomains":[],
            "acceptMultipleAnswers":<MULTIPLE_ANSWERS>,
            "allowIncognitoResponses":False,
            "showUsersEmail":False,
            "allowedEmails":[],
            "requiresLogIn":False
         },
         "state":<STATE>,
         "creationDate":"2018-06-29T15:51:44.368Z",
         "responseQuantity":<RESPONSE_QUANTITY>,
         "questions":[
            {
               "_id":"",
               "text":<QUESTION_NAME>,
               "type":<QUESTION_TYPE>,
               "required":False,
               "sequence":0,
               "valid":True,
               "max":0,
               "options":[],
               "wasTyped":True
            }
         ],
         "tags":[ ],
         "shortUrl":"",
         "actionTokensCost":<TOKEN_COST>,
         "fastpass":""
     }
     """
    When I perform a POST  at the service "/surveys"
    And I save the body response as "survey_response"
    Then I expect status code "400"
    And I verify the response "survey_response" with the following body
    """
    {
      "statusCode": 400,
      "details": "Invalid request",
      "payload": None
    }
    """

    Examples: Empty
      | TITLE           | RELEASE_DATE
      | ""              | "2018-06-29T15:51:44.368Z"
      | "Survey Test 1" | ""
      | "Survey Test 2" | "2018-06-29T15:51:44.368Z"
      | "Survey Test 3" | "27187-15-288-:51:44.368Z"
      | ""              | "2018-06-29T15:51:44.368Z"
      | "Survey Test 4" | "2018-06-29T15:51:44.368Z"
      | "Survey Test 5" | "2018-06-29T15:51:44.368Z"

    Examples: Invalid
      | TITLE            | RELEASE_DATE
      | "Survey Test 6"  | "2018-06-29T15:51:44.368Z"
      | "Survey Test 7"  | "2018-06-29T15:51:44.368Z"
      | "Survey Test 8"  | "2018-06-29T15:51:44.368Z"
      | "Survey Test 9"  | "2018-06-29T15:51:44.368Z"
      | "Survey Test 10" | "2018-06-29T15:51:44.368Z"
      | "Survey Test 11" | "2018-06-29T15:51:44.368Z"
      | 12               | "2018-06-29T15:51:44.368Z"
      | True             | "2018-06-29T15:51:44.368Z"
      | "Survey Test 13" | 2018
      | "Survey Test 14" | "2018-06-29T15:51:44.368Z"
      | "Survey Test 14" | "2018-06-29T15:51:44.368Z"

    Examples: Negative Inputs
      | TITLE         | RELEASE_DATE
      |               | "2018-06-29T15:51:44.368Z"
      | "Survey Test" |   ""
      | "Survey Test" | "2018-06-29T15:51:44.368Z"
      | "Survey Test" | "2018-06-29T15:51:44.368Z"
      | "Survey Test" | "2018-06-29T15:51:44.368Z"
      | "Survey Test" | "2018-06-29T15:51:44.368Z"
      | "Survey Test" | "2018-06-29T15:51:44.368Z"
      | "Survey Test" | "2018-06-29T15:51:44.368Z"
