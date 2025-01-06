Feature: Task 3 - User Registration

  Scenario: Verify frontend validation message on registration page
    Given I navigate to the user registration page
    When I trigger validation messages by clicking on all fields
    Then I should see the validation message for all required input fields


   Scenario: Verify the content of password advice section on registration page
    Given I navigate to the user registration page
    When I toggle the available control to show password advice
    Then I should be able to see correct information in show password advice section


   Scenario: Verify successful user registration with valid inputs
    Given I navigate to the user registration page
    When I fill in the registration form with self-generated information
    And I hit the register button
    Then I should see a successful registration message
    And I should navigate to login page

  Scenario: Verify login with newly registered user's credentials
    Given I navigate to the user registration page
    When I fill in the registration form with self-generated information
    And I hit the register button
    Then I should see a successful registration message
    And I should navigate to login page
    When I log in using the same information
    Then I should be logged in successfully


  Scenario: Verify task 3 E2E scenario
    Given I navigate to the user registration page
    When I trigger validation messages by clicking on all fields
    Then I should see the validation message for all required input fields
    When I toggle the available control to show password advice
    Then I should be able to see correct information in show password advice section
    When I fill in the registration form with self-generated information
    And I hit the register button
    Then I should see a successful registration message
    And I should navigate to login page
    When I log in using the same information
    Then I should be logged in successfully