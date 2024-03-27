# LOVE-ROCK-PAPER-SCISSORS

## Welcome to my version of rock-paper-scissors. It is played in the tradiitonal way except it is a human against a  computer. I had much fun learning to do this and despite some setbacks, i hope you enjoy the program. 

## PREREQUISITES
To be able to run the program, the user is required to have the Heroku App as it runs from a terminal in the application.

### How to install Heroku:
* Open your browser and type in Heroku.
* Follow the prompts to set up your account.
* Once your account is set up, you can open the deployment link and as Heroku is now installed in your compuetr, the program will run.

## GAMEPLAY

Love-Rock-Paper-Scissors is a game commonly played by 2 people. It can be played as in this case, by a person and a computer as random input is what is required. 

### The game is played as follows: 
* The user selects rock, paper or scissors as an option when prompted and the computer will also randomly select one of the three choices.
* If the user input is invalid, the user will be prompted to enter valid input. 
* Once a valid selection is made, the rules are as follows:
* If the computer and user chose the same option, then it is a tie.
* Rock smashes scissors; scissors cuts apper, paper covers rock.
* The winner is chosen as per the above rules.
* A score is shown at the end of each round: the winner receives 1 point, the loser receives no points for the round and if it is a tie then both the user and the computer do not receive any points.
* The winner of the series is whoever wins 3 rounds first. At the end of the series, the winner is displayed.
* The user is then prompted to choose wether they will continue the game or not. 
* If the user input is invalid, the user will be prompted to enter valid input.
* Once a valid selection is made, if the user chooses no, the game ends and a thank you message is displayed.
* If the user chooses to continue playing, the game prompts the user to re-start by inputing a selection of either rock, paper or scissors, and the game continues as at the start.

The image below is what the game looks like in the terminal.

![love rock paper scissors heroku terminal screenshot](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/d842a326-b495-448c-a91a-4c70606d92cf)


## FLOWCHART
The image below is a flowchart that displays the basic functionality of the gqme. The flowchart was created first and was the basis for the project and was built on and expanded to create the project as it currently is.

![Screenshot 2024-03-26 230746](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/0e107e3e-cb27-4182-ab70-349fe7d0441f)


### GAME AREA PAGE

* The game area page displays a welcome message the instructions on how to play as discussed above. The user can then type in their choice and the game begins. 
* The interface uses a variety of colors to make the site appealing as opposed to a black and white treminal. 
* The program also makes use of emojis for a fun experience.

## TECHNOLOGIES
Python is used as the main language for this project. 

## TESTING

### Input validation

* The user is prompted twice: once to enter either rock, paper or scissors and the second time to enter yes or no.
* For both requests, the user is to type their response in lowercase. This is written in the instructions.
* If the user enters any input aside from the provided choices, a loop will run that first notifies the user that invalid input was entered and then requests the user to enter valid input.
* This loop repeats the notification until valid input is entered.

A screenshot below is attached to display this in both instances.

![Screenshot 2024-03-27 071240](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/34f9e7f5-523c-4e57-a211-f53ba5d2f2c5)

![Screenshot 2024-03-27 071327](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/e4d4bc94-5bd0-45ec-b5a0-ecc222ef8d43)

### Code Validation
The code was run through CI Python Linter. There were no errors at the time of deployment.
The image below displays this.

![Screenshot 2024-03-27 034148](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/1b1332f8-7877-445c-8c40-1bce36bbcdca)

![Screenshot 2024-03-27 034159](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/e5e36b03-114e-40e9-b38e-249ae0736b3b)

![Screenshot 2024-03-27 034211](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/1896634f-0fed-4e5d-bda8-a5c5d1f11dfb)

![Screenshot 2024-03-27 034221](https://github.com/TammyGirl2015/love-rock-paper-scissors/assets/148330702/8adc691d-1145-406c-a30e-eb3d8b3cfc1a)

### Functional Testing

* Run program button.
* User input: rock, paper, scissors.
* User input: yes, no.

Description                                                   |Action                                            |Expected Result                                                                                                                                                                                                                                                              |Pass/Fail
--------------------------------------------------------------|--------------------------------------------------|---------------------------------------------------------|----------------------------------
Test the 'run program' button runs the program each time      |Click on 'run program' button                     |Program runs and starts the game                         |Pass
Test the user input for rock, paper and scissors              |User types in rock, paper or scissors in lowercase|If the input is not one of the three option, a loop      |Pass
.                                                             |.                                                 |notifies the user of  the error and asks the user to     |.
.                                                             |.                                                 |enter valid input.  Once the computer chooses it's input |.
.                                                             |.                                                 |the game loop determines a tie, win or loss for the user |. 
.                                                             |.                                                 |and computer and writes the sore for each round.         |. 
Test the user input for yes, no                               |User types in yes or no when prompted in lowercase|If the input is correct, yes continues the game and no   |Pass
.                                                             |.                                                 |ends the game. If the input is incorrcet, the user is    |. 
.                                                             |.                                                 |notified of the error and prompted to enter valid input. |. 
.                                                             |.                                                 |The loop repeats until valid input is entered.           |.

### Unfixed Bugs

There are no unfixed bugs at this time. I will mention the fact that i had to delete my original repository and create a new one due to the fact that all my commits were lost. The second time around, i amde a number  of commits before adding the creds.json file and while i followed the correct steps to hide the sensitive info, my repsoitory would not allow me to commit any changes and thus i had to do a hard reset and a numebr of commits were lost. 
Despite this, everything that has been done in the repository however, has been committed. 

### Version Control

The site was created using the Code Institute, Codeanywhere code editor template and pushed to github to the remote repository ‘love-rock-paper-scissors’.

The following git commands were used throughout development to push code to the remote repo:

```git add .``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Deployment to Heroku App

* The site was deployed to Heroku App.
* Installation for this can be found in the prerequisites section.
* The live link can be found here - https://love-rock-paper-scissors-ca1fc0ed705e.herokuapp.com/

### Clone the Repository Code Locally

Navigate to the GitHub Repository you want to clone to use locally:

* Click on the code drop down button
* Click on HTTPS
* Copy the repository link to the clipboard
* Open your IDE of choice (git must be installed for the next steps)
* Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

## CREDITS

### Page Name

* The page name was initially Trivia Time however at some point during the making of the site, i didn't feel that the questions were trivia but rather more general knowledge based hence the change to: Quizzed.

### Format

* The format of the website is credited to looking at the general layout of several quiz pages online and i had a general idea of the format of the quiz i wanted to create and ultimately went with that.
* The READme is a template from a previous project of mine and adjusted to suit the project.

### Content

* Content is credited to myself for text input with the answers to the 'made up' questions and some of the questions being taken from Google.

### Media

* All images used were taken from <https://pexels.com>
