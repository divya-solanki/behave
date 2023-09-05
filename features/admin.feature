Feature: Admin functionality verification in Orange HM application

  Background: common steps for login
    Given I open orangeHRM Homepage
    When Enter username "Admin" and password "admin123"
    And Click on login button
    Then verify navigation to Dashboard page is successful


  Scenario Outline: Verify Search functionality for admin
    Given I am on Dashboard page
    When navigate to Admin page
    And enter "<username>" to search
    And click on search button
    Then search result with "<username>" is shown in bottom pane.
    Examples:
    | username |
    | Admin    |
