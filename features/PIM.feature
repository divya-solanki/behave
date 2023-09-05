Feature: Employee Creation in Orange HM application

  Background: common steps for login
    Given I open orangeHRM Homepage
    When Enter username "Admin" and password "admin123"
    And Click on login button
    Then verify navigation to Dashboard page is successful

#  Scenario Outline: Add an employee details in Employee section of PIM module and Verify creation is successful
#    Given I navigate to  PIM module and click on Add Employee
#    When enter "<FirstName>" and "<LastName>" and click on save button
#    Then verify Employee name is displayed in Personal Details page
#    Examples:
#      | FirstName | LastName |
#      | Dave      | Smith    |


  Scenario Outline: Fill in Personal Details on Personal Details page
    Given I navigate to  PIM module and click on Add Employee
    When enter "<FirstName>" and "<LastName>" and click on save button
    Then verify Employee name is displayed in Personal Details page
    Then Enter "<SSN>" and "<DOB>"
    Then select Nationality
    Then Select Marital Status and Gender
    Then click save button

    Examples:
      | FirstName | LastName | SSN          | DOB        |
      | Dave      | Smith    | 123554242 | 2000-01-01 |