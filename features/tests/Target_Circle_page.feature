# Created by thesu at 4/22/2024
Feature: Target Circle Page

  Feature: Target sign in

  Scenario: Verify that logged out user can navigate to sign in
    Given Open the web page https://www.target.com/circle
    Then Verify there are 10 benefit cells