# Larrys LogBook

![Larrys LogBooks mockup image]()

Larrys Logbook is designed to help the user find out their budget for a given time, without having to do any mathematical equations.

Larrys LogBooks works with the simple formula of Available Funds + Income - Expenses, all of which are inside a given timeframe of the user’s choosing.

Visit the deployed application [here]().

## Table of Contents
1. [User Experience (UX)](#user-experience-UX)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Color Scheme](#color-scheme)
    4. [Data Model](#data-model)
    5. [Flowchart](#flowchart)
2. [Features](#features)
    1. [User Information Input](#user-information-input)
    2. [](#)
    3. [](#)
    4. [](#)
    5. [](#)
    6. [](#)
    7. [](#)
    8. [](#)
    9. [](#)
    10. [](#)
    11. [](#)
3. [Technologies Used](#technologies-used)
    1. [Language Used](#language-used)
    2. [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](#manual-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Project Goals

* Display enough information to let the user know what Larrys LogBook does.

* Each question/section that is asked/displayed is given the necessary information to be understood by the user.

* Provides input validation to help the user input the correct data.

* Gives insightful and convenient information to the user when the budget projections are displayed at the end.

### User Stories

* As a user, I want to know what Larrys LogBook is about and what it does.

* As a user, I want to understand each step clearly. 

* As a user, I want to know if the input I put in is correct or not, and receive clear feedback of what needs to be corrected.

* As a user, I want the data I put in to be displayed to me and given the option to correct it if needed.

* As a user, I want the final budget information to be displayed clearly and easy to understand.

### Color Scheme

[Colorama](https://pypi.org/project/colorama/) has been used to apply color to the terminal text. This in order to make the program more intuitive and easier to read. 

Here are the colors being used:

* Inputs/questions are displayed in green.

* The heading and final budget page are displayed in blue.

* Data that has been put in is displayed in yellow.

* Errors are displayed with a red background. 

* General information and other content is displayed in plain white. 

### Data Model

Data asked for like name is used for aesthetic purposes while data asked for as available funds amount, income amount and expense amount are used to calculate the surplus of the budget. What is also done with this data, is the input of naming and adding extra data with the data model being able to add up each available fund, income and expense given, to give a total of each respectively. The naming of each available fund, income and expense is recored for the convenience of the user to not have to add up each amount but just state the amount and let the program add it up for them. 

The timeframe data is used to calculate the daily projections of the budget and be displayed to the user at the final budget page.

Extra calculations are used with the data recieved to calculate the surplus, budget per day and ofcourse the totals of each available fund, income and expense for the results page.

### Flowchart

The following flowchart was designed using []() in order to plan the logic to be implemented in the program.

![Larrys LogBook Flowchart]()

As shown in the flowchart, the original order of some functions has been changed during the development process in to follow a more intuitive logic and sequence of events but the main idea behind the process is still the same.

[Back to top ⇧](#larrys-logbook)

## Features

### User Information Input

Collect the users information in order to use it in the program.

![User Information Input]()


###

![]()

### 

![]()

### 

![]()

### 

![]()

### 

![]()
![]()

### 

![]()

###

![]()

### 



![]()

### 

![]()

###

![]()

### 

[Back to top ⇧](#larrys-logbook)

## Technologies Used

### Language Used

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

* []() was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/) was used to store the project after pushing.

* [Heroku](https://id.heroku.com/) was used to deploy the application.

* [PEP8 online check](http://pep8online.com/) was used to validate the Python code.

* [BeautifulTable]() library was used to present the data in table format.

* [Colorama](https://pypi.org/project/colorama/) library was used to apply color to the terminal text. 

* []() was used to create the program flowchart.

[Back to top ⇧](#larrys-logbook)

## Testing

### Testing User Stories

* 

    - 

    - 

* 

    - 

    - 

* 

    - 

    - 

    - 

* 

    - 

    - 

    - 

* 

    - 

    - 

### Code Validation

The [PEP8 online check](http://pep8online.com/) was used continuosly during the development proces to validate the Python code for PEP8 requirements.

![PEP8 Code Validation](assets/readme-files/pep8-code-validation.png)

### Manual Testing



[Back to top ⇧](#larrys-logbook)

## Deployment

The application has been deployed using [Heroku](https://id.heroku.com/) by following these steps:

[Heroku](https://id.heroku.com/) was used to deploy the application.

1. Create the requirements.txt file and run: `pip3 freeze > requirements.txt` in the console.
2. Commit changes and push them to GitHub.
3. Go to the Heroku's website.
4. From the Heroku dashboard, click on "Create new app".
5. Enter the "App name" and "Choose a region" before clicking on "Create app".
6. Go to "Config Vars" under the "Settings" tab.
7. Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
8. Add the Config Var, KEY: PORT and VALUE: 8000.
9. Go to "Buildpacks" section and click "Add buildpack".
10. Select "python" and click "Save changes"
11. Add "nodejs" buildpack as well using the same process.
12. Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
13. Go to "Connect to GitHub" section and "Search" the repository to be deployed.
14. Click "Connect" next the repository name.
15. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

[Back to top ⇧](#larrys-logbook)

## Credits

### Content

* 

*

### Media
* 

### Code
* 

[Back to top ⇧](#larrys-logbook)

## Acknowledgements

* 

* My tutor, Marcel, for his invaluable feedback and guidance.

* Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.

