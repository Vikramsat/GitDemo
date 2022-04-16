*** Settings ***
Documentation   To validate the login form
Library     SeleniumLibrary
Library     Collections
Library     ../customLibraries/Shop.py
Test Setup       open the browser with the Mortgage payment url
#Test Teardown       Close Browser
Resource            resource.robot

*** Variables ***
${Error_Message_Login}      css:.alert-danger
${Shop_Page_Load}           css:.nav-link
${products_List}        Nokia Edge      Blackberry

*** Test Cases ***
#Validate UnSuccessful Login
#    Fill the login form     ${user_name}      ${invalid_password}
#    wait until element is located in the page       ${Error_Message_Login}
#    verify error message is correct

Validate cards display in the shopping page
    Fill the login form     ${user_name}     ${valid_password}
    wait until element is located in the page       ${Shop_Page_Load}
    Verify card titles in the shop page
    hello world
    #Select the card     Blackberry
    add items to cart and checkout      ${products_List}

Select the form and navigate to child window
    Fill the login details and login form

*** Keywords ***
open the browser with the Mortgage payment url
    create webdriver    Chrome  executable_path=E:/Udemy/chromedriver.exe
    go to   ${url}

Fill the login form
    [arguments]     ${username}        ${password}
    input text      id:username     ${username}
    input password      id:password     ${password}
    click button    signInBtn

wait until element is located in the page
    [arguments]     ${element}
    wait until element is visible       ${element}

verify error message is correct
    ${result}=     get text    ${Error_Message_Login}
    Should Be Equal As Strings      ${result}   Incorrect username/password.
    #above line can also be written as below line
    #element text should be      ${Error_Message_Login}      Incorrect username/password.


Verify card titles in the shop page
    @{expected_list}=   Create List    iphone X    Samsung Note 8      Nokia Edge      Blackberry
    @{actual_list}=     Create List

    ${elements}=    Get webelements     css:.card-body h4

    FOR     ${element}  IN  @{elements}
        Log     ${element.text}
        Append To List      ${actual_list}      ${element.text}
    END

    Lists Should Be Equal    ${expected_list}    ${actual_list}


Select the card
        [arguments]     ${cardname}
        ${elements}=    Get webelements     css:.card-body h4
        ${index}=   Set Variable    1
        FOR     ${element}  IN   @{elements}
            Exit For Loop if    '${cardname}' == '${element.text}'
            ${index}=   Evaluate    ${index} + 1
        END
        click button    (//div[@class='card-footer'])[${index}]/button

Fill the login details and login form
    input text      id:username     rahulshettyacademy
    input password      id:password     learning
    click element       css:input[value='user']
    wait until element is visible       css:.modal-body
    click button    okayBtn
    wait until element is not visible     css:.modal-body
    select from list by value       css:select.form-control     teach
    select checkbox     terms
    checkbox should be selected     terms