# Cross Game

![alt text](https://github.com/sifisKoen/Pi-Playground/blob/main/ReadMe%20images/CrossImage.png)

This is a cross the road game. Where your objective is to cross the road with your turtle.

## Tools 🪛

I used a build in Python library **Turtle** for my graphics.

## How to run it ⚙️

It's very simple

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.
  - Now go to the **/CrossGame** directory and open your terminal.
    - From your terminal type, `python3 main.py`

## The structure of the project 📚

    ├── car_manager.py
    ├── cars.py
    ├── main.py
    ├── player.py
    ├── __pycache__
    │   ├── car.cpython-310.pyc
    │   ├── car_manager.cpython-310.pyc
    │   ├── cars.cpython-310.pyc
    │   ├── player.cpython-310.pyc
    │   └── scoreboard.cpython-310.pyc
    ├── README.md
    └── scoreboard.py

## Class Explanation 📖

Each of these files are our **cross game** classes.

- cars.py
  - Is our class where we initialize our cars where they start their color and shape.
- car_manager.py
  - Is our class where controls the cars and move them create them and increase their speed when the user pass each level.
- player.py
  - Is our class where we create the player initialize the shape of the player and speed of them. In this class we also have one function witch helps us to move the player.
- main.py
  - Is our main class where we have our while loop in witch happening all our main event of the game. In this while loop we check the collisions of the player with the cars or when the player finishes a level so to move them to the next level.
