Feature:View Dashboard

  Scenario: Test login to OrangeHRM with valid credentials
    Given I open orangeHRM Homepage
    When Enter username "Admin" and password "admin123"
    And Click on login button
    Then verify navigation to Dashboard page is successful


#  Scenario Outline: Test login to OrangeHRM with mixed credentials
#    Given I launch Chrome Browser
#    When I open orangeHRM Homepage
#    And Enter username "<username>" and password "<password>"
#    And Click on login button
#    Then verify navigation to Dashboard page is successful
#
#
#    Examples:
#    | username | password |
#    | Admin | admin123 |
#    | Admin | admin1234 |
#    | admin36 | admin123 |
#    | adnim | dfjdshf |