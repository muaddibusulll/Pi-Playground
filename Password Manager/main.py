import tkinter
from tkinter import ttk

# Constants
WEBSITE_LABEL_TEXT = "Website:"
EMAIL_USERNAME_TEXT = "Email/Username:"
PASSWORD_TEXT = "Password:"
GENERATE_PASSWORD_BUTTON_TEXT = "Generate Password"
ADD_BUTTON_TEXT = "Add"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO: Create a function that will create a new file
# If it doesn't exist or will open it.
# Pass this file name to an other function
# LINK: https://www.w3schools.com/python/python_file_write.asp

# Or combine them into one function... 🤔

# TODO: Create a function that will take all the fields
# from the program and will save them into the provided file.
# Into this function the fields will be cleared up after
# each time the function is called.
# def save_password():
# LINK: https://tkdocs.com/tutorial/widgets.html#entry


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

website_label = tkinter.Label(text=WEBSITE_LABEL_TEXT, font=FONT)
website_label.grid(row=1, column=0)

website_import_text = tkinter.Entry(width=35)
website_import_text.focus()
website_import_text.grid(row=1, column=1, columnspan=2, sticky="EW")


# -------------------- Email/Username import area -------------------- #

email_username_label = tkinter.Label(text=EMAIL_USERNAME_TEXT, font=FONT)
email_username_label.grid(row=2, column=0)


email_username_import_text = tkinter.Entry(width=35)
email_username_import_text.insert(0, "randomMail@gmail.com")
email_username_import_text.grid(row=2, column=1, columnspan=2, sticky="EW")

# -------------------- Password import area -------------------- #

password_label = tkinter.Label(text=PASSWORD_TEXT, font=FONT)
password_label.grid(row=3, column=0)

password_import_text = tkinter.Entry(width=21)
password_import_text.grid(row=3, column=1, sticky="EW")

generate_password_button = tkinter.Button(
    text=GENERATE_PASSWORD_BUTTON_TEXT)
generate_password_button.grid(row=3, column=2, sticky="EW")

# -------------------- Add Button import area -------------------- #

add_button = tkinter.Button(text=ADD_BUTTON_TEXT, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

width = window.mainloop()
