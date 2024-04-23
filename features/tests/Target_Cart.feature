# Created by thesu at 4/10/2024
Feature: Target Cart

  Scenario: open target cart
    Given Open the web page https://www.target.com
    When Click on cart
    Then Verify “Your cart is empty” message is shown


