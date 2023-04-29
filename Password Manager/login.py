import tkinter
from tkinter import messagebox
import json

LOGIN_WINDOW_TITLE = "Login Window"
LOGIN_LOGO_IMAGE_PATH = "logo.png"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 12)
NOTES_FOR_THE_USER_TEXT = "NOTE:\n1) Please remember your Password\n2) Choose a strong Password"


def password_check_interface():
    # Label
    user_password_label = tkinter.Label(
        text="Password", font=FONT)
    user_password_label.grid(row=1, column=0, sticky="EW")

    # Entry
    global user_password
    user_password = tkinter.Entry(width=35)
    user_password.focus()
    user_password.grid(row=1, column=1, columnspan=2, sticky="EW")

    # Button
    login_button = tkinter.Button(text="Login", command=password_check)
    login_button.grid(row=2, column=1, columnspan=2, sticky="EW")


def incorrect_password_messagebox():

    messagebox.showerror(
        title="Error", message="Wrong password")


def is_password_correct(inserted_password):

    # Read password file
    password_data = json.load(open("user_password.json", "r"))

    if inserted_password in password_data["password"]:
        return True


def password_check():

    inserted_password = user_password.get()

    if is_password_correct(inserted_password) != True:
        incorrect_password_messagebox()
        password_check_interface()
    else:
        login_window.quit()


# ---------------------------- NEW USER ------------------------------- #


def create_user_password_interface():
    # Label
    choose_password_label = tkinter.Label(text="Choose Password", font=FONT)
    choose_password_label.grid(row=1, column=0, sticky="EW")

    # Entry
    global user_choose_password
    user_choose_password = tkinter.Entry(width=35)
    user_choose_password.focus()
    user_choose_password.grid(row=1, column=1, columnspan=2, sticky="EW")

    # Button
    save_user_new_password = tkinter.Button(
        text="Save", command=save_the_new_password)
    save_user_new_password.grid(row=2, column=1, columnspan=2, sticky="EW")

    # NOTE: Labels
    password_explain_to_user = tkinter.Label(
        text="This password is required to unlock tha app", fg="red")
    password_explain_to_user.grid(row=3, column=0, columnspan=2, sticky="EW")

    notes_for_the_user = tkinter.Label(text=NOTES_FOR_THE_USER_TEXT, fg="red")
    notes_for_the_user.grid(row=5, column=0, columnspan=2, sticky="EW")


def confirmation_message_box(new_password):
    return messagebox.askokcancel(
        title="Confirm", message=f"Is this password correct?\n{new_password}")


def write_new_password_to_file(new_password):

    json.dump(new_password, open("user_password.json", "w"), indent=4)


def save_the_new_password():

    user_new_password = user_choose_password.get()
    password_data = {
        "password": user_new_password
    }

    if confirmation_message_box(new_password=user_new_password) == True:

        write_new_password_to_file(password_data)


# ---------------------------- LOGIN UI SETUP ------------------------------- #

class LogIn:

    def __init__(self):
        global login_window
        login_window = tkinter.Tk()
        login_window.title(LOGIN_WINDOW_TITLE)
        login_window.config(padx=50, pady=50)

        # Create our canvas window
        login_canvas = tkinter.Canvas(width=200, height=200)
        # Import our image
        login_logo_image = tkinter.PhotoImage(file=LOGIN_LOGO_IMAGE_PATH)
        login_canvas.create_image(100, 100, image=login_logo_image)
        login_canvas.grid(row=0, column=1)

        try:
            with open("user_password.json") as user_password_file:
                password_check_interface()
        except FileNotFoundError:
            create_user_password_interface()

        width = login_window.mainloop()
