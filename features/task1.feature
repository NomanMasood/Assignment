Feature: Task1 - Products page Items

  Scenario: Verify all items are displayed on the products page
    Given I navigate to the Juice Shop application
    When I scroll to the bottom of the page
    And I change items per page to the maximum
    Then I should see all items displayed on the products page