*** Settings ***
Documentation   A resource file with reusable keywords and variables
...
...             The system specific keyword created here from our own
...             domain specific language. They utilize keywords provided
...             by the imported selenium library

Library     SeleniumLibrary


*** Variables ***
${user_name}            rahulshettyacademy
${valid_password}       learning
${invalid_password}     123456
${url}                  https://www.rahulshettyacademy.com/loginpagePractise/


*** Keywords ***
open the browser with the Mortgage payment url
    create webdriver    Chrome  executable_path=E:/Udemy/chromedriver.exe
    go to  ${url}

Close Browser Session
    Close Browser