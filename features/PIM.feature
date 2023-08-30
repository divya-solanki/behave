Feature: PIM Module

  Background: common steps for login
    Given I launch Chrome Browser
    When I open orangeHRM Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then I am on Dashbord page

  Scenario: Add Employee
    Given I click on PIM module
    When I click on Add Employee
    And I enter First Name
    And I enter Last name
    And I click on save button