Feature: Task 2 - Product Interaction

  Scenario: Verify product pop-up and expand review
    Given I navigate to the Juice Shop application
    When I click on the first product
    Then I should see the product pop-up
    And the product image should be displayed
    When I expand the review section if available
    Then I should be able to see the expanded review section
    And I close the product pop-up