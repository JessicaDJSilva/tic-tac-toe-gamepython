
## Tic-Tac-Toe 
The tic-tac-toe game is a python terminal game, the aim of the game is to place three marks "X" or "O" in a "horizontal, vertical, or diagonal row.
You can play the game [here](https://tic-tac-toe-pp3.herokuapp.com/)
<img src= images/I-am-resposive.jpg>
## Features

#### How to play
Before starting the game, the user has a welcome message and clear instructions on how the game works and what is needed to do to win.
The user can see an example of the playboard before the game starts.
The game starts after the player choose between heads or tails.
<img src= images/welcome-message.jpg>
####  Start of the game
The user has a 50% chance to start the game by choosing heads or tails.
if the computer wins on the flip coin it uptade with the first move on the board.
<img src= images/start-of-the-game.jpg>
####  Invalid data
If the user enters invalid data or in this case try place to move in the same place the computer will repeat the choose you move question until valid data is received. 
<img src= images/choose-used-postion.jpg>
####  Game Results
The user will receive a different message depending on how the game finishes.
<img src= images/win.jpg>

## Testing
I have manually tested the project by doing.
 - Pass the code on PEP8 and confirm that was no error.
 <img src= images/pep8-valitadion.jpg>
 - The website works in the 3 main browsers: Chrome, Edge, Firefox.

## Bugs

 - The game was running too fast, so I import the time library and added sleep time into the functions to give it more time to run.
 - Some of the lines was too long considering the 80 characters maximum, I fixed instaling black to handle the formation.

## Deployment
To deploy my game on Heroku I follow the steps.
 - Added my requirements on requirements.txt on gitpod
 - Create a new app on the initial page of Heroku and connected it with Github.
 - Search for my tic-tac-toe on the repositories.
 - After liking my repositories, clicked on settings and added Config Vars key PORT and value 8000.
 - Also added python and nodejs in Buildpacks.
 - On the Deployment tab the option Automatic deploys were selected giving me the [link](https://tic-tac-toe-pp3.herokuapp.com/) when fished.


## Unfixed bugs
No unfixed bugs to report.

## Credit
Code institute template was used.
code institute for deployment terminal