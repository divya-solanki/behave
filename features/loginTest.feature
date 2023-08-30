Feature:View Dashboard

  Scenario: Test login to OrangeHRM with valid credentials
    Given I launch Chrome Browser
    When I open orangeHRM Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then I am on Dashbord page


  Scenario Outline: Test login to OrangeHRM with mixed credentials
    Given I launch Chrome Browser
    When I open orangeHRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then I am on Dashbord page


    Examples:
    | username | password |
    | Admin | admin123 |
    | Admin | admin1234 |
    | admin36 | admin123 |
    | adnim | dfjdshf |