*** Settings ***
Documentation   To validate the login form
Library     SeleniumLibrary
Library     String
Library     Collections
Test Setup       open the browser with the Mortgage payment url
#Test Teardown       Close Browser
Resource    resource.robot

*** Variables ***
${Error_Message_Login}      css:.alert-danger

*** Test Cases ***
#Validate UnSuccessful Login
#    open the browser with the Mortgage payment url
#    Fill the login form
#    wait until it checks and displays error message
#    verify error message is correct

Validate Child Window Functionality
    Select the link of the child window
    Verify the user is switched to child window
    Grab the email id in the child window
    Switch to parent window and enter the email


*** Keywords ***
Select the link of the child window
    click element       css:.blinkingText
    Sleep       5

Verify the user is switched to child window
    switch window       NEW
    element text should be      css:h1      DOCUMENTS REQUEST

Grab the email id in the child window
    ${text}=    Get text    css:.red
    @{words}=    Split String    ${text}     at

    ${text_split}=   Get From List       ${words}    1
    @{words_2}=     Split string        ${text_split}    with
    ${email}=       Get From List      ${words_2}      0
    Set Global Variable     ${email}

Switch to parent window and enter the email
    switch window   MAIN
#    title should be
    input text      id:username     ${email}


