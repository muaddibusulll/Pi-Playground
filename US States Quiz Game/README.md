# US States Quiz Game ⛳

This is a quiz game where the user needs to think and answer all the US States so to unlock them in the map.

## Tools 🪛

For this project I used - The **Turtle** class for my graphics (image and windows) - The **Pandas** library so to manipulate my data from my **csv** file where I have all the data for the US states, (Name, x, y)

### Very interested code process 🚩

While I was building this project I came along with one issues:

🤔 How to take the position fo each state in the map?_(The map is the turtle with a shape of the map)_

And while I was searching I found this stackoverflow frame:

- [Get mouse click coordinates in Python turtle](https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle)

Where I found this answer:

```python
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
```

This code is not in my actual code but it helped to find the x and y coordinates for each state so to add them into my **csv** file. C

## How to run it ⚙️

It's very simple

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.

  - Now go to the **/US States Quiz Game** directory and open your terminal.
    - From your terminal type, `python3 main.py`

* Make sure the the file **50_states.csv** is in the same directory with the **main.py**

## The structure of the project 📚

    ├── 50_states.csv
    ├── states_img.gif
    ├── state.py
    ├── main.py
    ├── __pycache__
    │   ├── country.cpython-310.pyc
    │   └── questionboard.cpython-310.pyc
    └── README.md

## Class Explanation 📖

- state.py
  - Is our class where we create each time our new state name object and mote it to the correct position on the map. This object it _Turtle_ type object.
- 50_states.csv
  - Is our database table where we have saved all the states with their respective coordinates on the map (as accurate as possible). The _csv_ file contains three columns namely:
    - state
    - x
    - y
- missing_states.csv
  - Is our **csv** file that we are creating just for the user to take a look and see again what are the missing states. I think this a good extra to this game.
- main.py
  - Is our main class where we create our map with the states and we read the corresponding _csv_ file so to have access to the data we need. We have a method called **play_game** which is our main method where the game logic is.
