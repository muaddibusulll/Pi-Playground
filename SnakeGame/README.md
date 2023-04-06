# Snake Game 🐍

This is a classic snake game.

## Tools 🪛

I used a build in Python library **Turtle** for my graphics.

## How to run it

It's very simple

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.
  - Now go to the /SnakeGame directory and open your terminal.
    - From your terminal type, `python3 main.py`

## The structure of the project

    ├── main.py
    ├── __pycache__
    │   └── snake.cpython-310.pyc
    ├── README.md
    └── snake.py
    └── snakeFood.py
    └── scoreboard.py

## Class Explanation

Each of these lives are our **snake game** classes.

- snake.py
  - Is our let's say main class where the snake creates, move, and extends it self.
- scoreboard.py
  - Is our class witch is in charge to keep track of the players score write this score on the creen and when the player lose the game report that to the player.
- snakeFood.py
  - Is our class where the food of the snake creates and print it self to our screen in a random position
- main.py
  - Is out main class where all the functionality of the game is calling the methods from our classes so to make the game alive. This class is where we use our methods from the other three classes so to make them actual do what mend to do.
