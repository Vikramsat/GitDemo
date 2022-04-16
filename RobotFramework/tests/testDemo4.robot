*** Settings ***
Documentation   To validate the login form
Library     SeleniumLibrary
Test Teardown       Close Browser
Test Template       Validate Unsuccessful Login

*** Variables ***
${Error_Message_Login}      css:.alert-danger

*** Test Cases ***      username    password
Invalid username        abcd        learning
Invalid password        rahulshetty     abcd
Special chacters        @#$         learning

*** Keywords ***
Validate UnSuccessful Login
    [Arguments]     ${username}    ${password}
    open the browser with the Mortgage payment url
    Fill the login form     ${username}     ${password}
    wait until it checks and displays error message
    verify error message is correct

open the browser with the Mortgage payment url
    create webdriver    Chrome  executable_path=E:/Udemy/chromedriver.exe
    go to   https://www.rahulshettyacademy.com/loginpagePractise/

Fill the login form
    [arguments]     ${username}     ${password}
    input text      id:username     ${username}
    input password      id:password     ${password}
    click button    signInBtn

wait until it checks and displays error message
    wait until element is visible   ${Error_Message_Login}

verify error message is correct
    ${result}=     get text    ${Error_Message_Login}
    Should Be Equal As Strings      ${result}   Incorrect username/password.
    #above line can also be written as below line
    #element text should be      ${Error_Message_Login}      Incorrect username/password.