# Snake Game 🐍

![alt text](https://github.com/sifisKoen/Pi-Playground/blob/main/ReadMe%20images/NewSnakeHighScore.png)

This is a classic snake game with high scoreboard track.
The high score of our game is saved in a file called **game_data.txt**.

## Tools 🪛

I used a build in Python library **Turtle** for my graphics.

## How to run it ⚙️

It's very simple

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.

  - Now go to the **/SnakeGame** directory and open your terminal.
    - From your terminal type, `python3 main.py`

* Make sure the the file **game_data.txt** is 0 if you want to make a new start. If not you can just keep the old score of yours.

## The structure of the project 📚

    ├── main.py
    ├── __pycache__
    │   └── snake.cpython-310.pyc
    ├── README.md
    └── snake.py
    └── snakeFood.py
    └── scoreboard.py
    └── game_data.txt

## Class Explanation 📖

Each of these files are our **snake game** classes.

- snake.py
  - Is our let's say main class where the snake creates, move, and extends it self.
- scoreboard.py
  - Is our class witch is in charge to keep track of the players score write this score on the screen and when the player lose the game report that to the player.
- snakeFood.py
  - Is our class where the food of the snake creates and print it self to our screen in a random position
- main.py
  - Is out main class where all the functionality of the game is calling the methods from our classes so to make the game alive. This class is where we use our methods from the other three classes so to make them actual do what mend to do.
- game_data.txt
  - Is not a class but it is a txt file where we save our game higher score so to keep track our score.

## Changes 🛠️

The changes that I made from the previous version of the game are:

- First I remove the Game Over functionality (I didn't like it)
  - I include instead when the user loses the snake starts again from the initial state of it.
- I include the **High Score** functionality in the **Scoreboard**
- Now the old **hight** score is saving and the user can have their high score and after they close the game.
