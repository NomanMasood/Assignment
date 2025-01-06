Feature: Task 4 - Login and end to end Product Checkout process

  Scenario: Login and checkout process
    Given I navigate to the Juice Shop login page
    When I login with valid generated credentials
    Then I should be logged in successfully
    When I add the 'Apple Juice (1000ml)' to the basket
    Then I should see the 'Apple Juice (1000ml)' added success message
    When I add the 'Banana Juice' to the basket
    Then I should see the 'Banana Juice (1000ml)' added success message
    When I add the 'Fruit Press' to the basket
    Then I should see the 'Fruit Press' added success message
    When I add the 'Carrot Juice (1000ml)' to the basket
    Then I should see the 'Carrot Juice (1000ml)' added success message
    When I add the 'Lemon Juice (500ml)' to the basket
    Then I should see the 'Lemon Juice (500ml)' added success message
    And The cart number should be updated to "5"
    When I navigate to my basket and increase the quantity of a product
    And I delete the product from the basket
    Then the total price should be updated
    When I click on checkout and add address information
    And I select the address and proceed to checkout
    And I choose the delivery speed and proceed to checkout
    Then I should not have money in wallet balance
    When I add the details of new card and proceed to checkout
    Then I should see the card saved message

