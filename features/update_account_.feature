Feature: Update account details
    As a customer
    I want to update my account status

    Scenario: Close an account
        Given I am a registered customer with ID "585858"
        When I create an account with customer ID "585858"
        And I close the account
        And I get the account details
        Then I should see an "closed" account with customer id "585858"
