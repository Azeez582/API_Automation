Feature: login API
#Field Service Engineer
Scenario: Login as FSE
    When I call login API with FSE user
    Then token should be returned
    Then token should be present
    
