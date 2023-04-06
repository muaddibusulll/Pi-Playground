# Pong Game 🏓

![alt text](/Pi-Playground/PongGame/Screenshot%20from%202023-04-06%2022-30-21.png)

This is a classic Pong Game

## Tools 🪛

I used a build in Python library **Turtle** for my graphics.

## How to run it ⚙️

It's very simple

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.
  - Now go to the **/PongGame** directory and open your terminal.
    - From your terminal type, `python3 main.py`

## The structure of the project 📚

    ├── ball.py
    ├── main.py
    ├── paddle.py
    ├── __pycache__
    │   ├── ball.cpython-310.pyc
    │   ├── paddle.cpython-310.pyc
    │   └── scoreboard.cpython-310.pyc
    ├── README.md
    ├── scoreboard.py

## Class Explanation 📖

Each of these files are our **pong game** classes.

- paddle.py
  - Is our class where the paddles creating and take their traits. Additionally we have two functions so to move up and down the paddles.
- ball.py
  - Is our class where the ball is created, move and interact with the screen walls and the paddles.
- scoreboard.py
  - Is our class where the scoreboard is created, and keep track the players score.
- main.py
  - Is our as you can understand from the name our main class where all other classes and methods are leave and interact with each other. Is the class witch connect all the other classes and methods. Our _while_ loop is let's say the brain of our game.
