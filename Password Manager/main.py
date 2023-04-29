import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import string
import random
import pyperclip
import json
import login

# Constants
WEBSITE_LABEL_TEXT = "Website:"
EMAIL_USERNAME_TEXT = "Email/Username:"
PASSWORD_TEXT = "Password:"
GENERATE_PASSWORD_BUTTON_TEXT = "Generate Password"
ADD_BUTTON_TEXT = "Add"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 12)
SEARCH_TEXT = "Search"

login_window = login.LogIn()

# ---------------------------- DATA SEARCH ------------------------------- #


def is_website_filed_empty(website):

    if (website == ""):
        messagebox.showwarning(
            title="Warning", message="Please enter a website")
        return True
    else:
        return False


def find_data(website):

    try:
        all_data = json.load(read_file())
        return all_data[website]
    except KeyError:
        messagebox.showerror(
            title=website, message=f"{website} is not available")


def output_data(website, data_dictionary):

    email = data_dictionary['email']
    password = data_dictionary['password']
    messagebox.showinfo(
        title=website, message=f"Email: {email}\nPassword: {password}")


def search_for_data():

    website = website_import_text.get().capitalize()

    if is_website_filed_empty(website) == True:
        return

    output_data(website, find_data(website))


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_characters_lists():

    password_letters_list = [(random.choice(string.ascii_letters))
                             for letter in range(random.randint(2, 4))]
    password_digits_list = [(random.choice(string.digits))
                            for digit in range(random.randint(2, 4))]
    password_symbols_list = [(random.choice(string.punctuation))
                             for punctuation in range(random.randint(2, 4))]

    return password_letters_list, password_digits_list, password_symbols_list


def manipulate_password_characters():

    password_letters_list = password_characters_lists()[0]
    password_digits_list = password_characters_lists()[1]
    password_symbols_list = password_characters_lists()[2]

    password_list = password_letters_list + \
        password_digits_list + password_symbols_list

    random.shuffle(password_list)

    return password_list


def password_creation():

    password_shuffled_list = manipulate_password_characters()

    new_password = ''.join(password_shuffled_list)

    password_import_text.insert(tkinter.END, string=new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def is_a_field_blank(*data):

    if (data[0] == ""):
        messagebox.showwarning(
            title="Warning", message="Please enter a website")
        return True
    elif (data[1] == ""):
        messagebox.showwarning(
            title="Warning", message="Please enter a password")
        return True
    elif (data[2] == ""):
        messagebox.showwarning(
            title="Warning", message="Please enter an email address")
        return True
    else:
        return False


def empty_fields():
    website_import_text.delete(0, "end")
    password_import_text.delete(0, "end")


def confirmation_message_box(website, email, password):

    return messagebox.askokcancel(
        title="Confirm", message=f"These details are correct?\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?")


def read_file():
    return open("data.json", "r")


def write_file():
    return open("data.json", "w")


def open_file():
    return open("data.json")


def write_to_file_new_data(new_data):
    try:
        # Read old data
        data = json.load(read_file())
        # Update the old data
        data.update(new_data)
        # Save the old data to file
        json.dump(data, write_file(), indent=4)
    except FileNotFoundError:
        # Create a new file
        json.dump(new_data, write_file(), indent=4)


# LINK: https://tkdocs.com/tutorial/widgets.html#entry

def save_data_to_file():

    website = website_import_text.get().capitalize()
    email_username = email_username_import_text.get()
    password = password_import_text.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }}

    if (is_a_field_blank(website, email_username, password) == True):
        return

    if (confirmation_message_box(website=website, email=email_username, password=password) == True):

        write_to_file_new_data(new_data=new_data)

        empty_fields()

        print(f"{website} | {email_username} | {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

# Create our canvas window
canvas = tkinter.Canvas(width=200, height=200)
# Import our image
password_logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo_image)
canvas.grid(row=0, column=1)

# -------------------- Website import area -------------------- #

# Label
website_label = tkinter.Label(text=WEBSITE_LABEL_TEXT, font=FONT)
website_label.grid(row=1, column=0)

# Entry
website_import_text = tkinter.Entry(width=35)
website_import_text.focus()
website_import_text.grid(row=1, column=1, sticky="EW")

# Button
search_data_through_website = tkinter.Button(
    text=SEARCH_TEXT, command=search_for_data)
search_data_through_website.grid(row=1, column=2, sticky="EW")

# -------------------- Email/Username import area -------------------- #

# Label
email_username_label = tkinter.Label(text=EMAIL_USERNAME_TEXT, font=FONT)
email_username_label.grid(row=2, column=0)

# Entry
email_username_import_text = tkinter.Entry(width=35)
email_username_import_text.insert(0, "randomMail@gmail.com")
email_username_import_text.grid(row=2, column=1, columnspan=2, sticky="EW")

# -------------------- Password import area -------------------- #

# Label
password_label = tkinter.Label(text=PASSWORD_TEXT, font=FONT)
password_label.grid(row=3, column=0)

# Entry
password_import_text = tkinter.Entry(width=21)
password_import_text.grid(row=3, column=1, sticky="EW")

# Button
generate_password_button = tkinter.Button(
    text=GENERATE_PASSWORD_BUTTON_TEXT, command=password_creation)
generate_password_button.grid(row=3, column=2, sticky="EW")

# -------------------- Add Button import area -------------------- #

# Button
add_button = tkinter.Button(
    text=ADD_BUTTON_TEXT, width=36, command=save_data_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

# -------------------- Menu Bar import area -------------------- #
menu_bar = Menu(window)
options = Menu(menu_bar, tearoff=0)
options.add_command(label="Saved Passwords")
options.add_command(label="Back")

options.add_separator()

options.add_command(label="Exit", command=window.quit)

menu_bar.add_cascade(label="Options", menu=options)
window.config(menu=menu_bar)

width = window.mainloop()
