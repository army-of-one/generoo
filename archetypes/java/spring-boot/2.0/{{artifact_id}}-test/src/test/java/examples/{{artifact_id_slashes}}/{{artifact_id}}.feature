Feature: {{artifact_id_capitalized_with_spaces}} API

Background:
* url 'http://localhost:54321/{{group_id_dashes}}'

Scenario: Create {{artifact_id_lowerl}}

    * def user =
    """
    {
      "name": "CreateTest",
    }
    """

    Given path '{{artifact_id}}s'
    And request user
    When method post
    Then status 201
    And match response.id != null

Scenario: Create {{artifact_id_lowerl}} and get by ID after
    * def user =
    """
    {
      "name": "GetByIDTest",
    }
    """

    Given path '{{artifact_id}}s'
    And request user
    When method post
    Then status 201
    And match response.id != null
    Given def id = response.id
    And path '{{artifact_id}}s', id
    When method get
    Then status 200
    And match response.name == user.name
    And print 'got {{artifact_id_lower}} response for id: ' + id
