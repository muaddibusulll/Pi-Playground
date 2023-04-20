# Password Creator and Manager 🔐

![alter text](https://github.com/sifisKoen/Pi-Playground/blob/main/ReadMe%20images/PasswordManagerIMG.png)

This is UI Python program witch creates a random password for a web site and save the name of the site as well as the password and the email address of the user into a txt file **locally** to user's computer.

The name of the file is **data.txt** witch very easily can be change from the code.

## Tools 🪛

I used the build in Python library **tkinter** for the graphics (UI).

From **tkinter** I used additionally the **messagebox** module for displaying messages to the user's screen.

Also I used from the **PiPy** library the **pyperclip** witch helps when the user push the button _Generate Password_ and the new password generate to copy this new password to user's clipboard.

## How to run it ⚙️

It's very simple

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.

  - Now go to the **/Password Manager** directory and open your terminal.
    - From your terminal type, `python3 main.py`

* Very important IF you run Linux machine first you need to install: `sudo apt-get install xsel` this is copy paste mechanism witch let the **pyperclip** run correctly. This is only for Linux users for Mac and Windows users works without any installations.

## The structure of the project 📚

    ├── data.txt
    ├── logo.png
    ├── main.py
    └── README.md

## Class Explanation 📖

In this project we have only one class.

- main.py
  - I our main class where all the program runs. In this class we have tree concrete sections.
    - **_PASSWORD GENERATOR_** witch is the section where the password **generates** when the user clicks on the button _Generate Password_. This section is divided into three different functions, `password_characters_lists()`, `manipulate_password_characters()`, and `password_creation()`
    - **_SAVE PASSWORD_** in this section the user's input saved into a txt file if the file is already created but if the file is not there it also creates a file automatically. This section is divided into five different functions, `is_a_field_blank()`, `empty_fields()`, `confirmation_message_box()`, `file()`, `save_data_to_file()`
    - **_UI SETUP_** in this last but very important section lives our UI and all the commands of it. In this section all previous functions get called so to make use of them.
