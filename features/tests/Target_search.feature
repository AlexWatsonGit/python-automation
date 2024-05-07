# Created by thesu at 5/5/2024
Feature: Target search

  Scenario: Search for item on target page and verify its there
    Given Open the web page https://www.target.com/
    When Search for lemon ginger tea
    Then Verify item pops up