# Created by thesu at 4/11/2024
Feature: Target sign in

  Scenario: Verify that logged out user can navigate to sign in
    Given Open the web page https://www.target.com/
    When Click sign in
    When From navigation menu, click sign in
    Then Verify sign in opened
