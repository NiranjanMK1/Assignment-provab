Feature: Login to Hubbler

  Scenario: Login with OTP
    Given User on the Hubbler login page
    When User click on login with OTP
    Then User enter valid login details from excel
    And User click on the Next button
    And User Go to email in a new tab in chrome
    #Then User Search  OTP sent by 'hubblermail'        step is passed as i dont have the credentials to log into
    And User copy the OTP
    And User Return to enter the OTP screen for hubbler
    And User paste the OTP
    Then User should see the My day landing page
    #And I track the total time taken to login
