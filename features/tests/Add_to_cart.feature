# Created by thesu at 4/22/2024
Feature: Add item to cart

  Scenario: Add item and check if its in the cart
    Given Open the web page https://www.target.com
    When Search for ps5
    When Add item to cart
    Then Verify item was added to cart successfully