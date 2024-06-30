from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json
from cryptography.fernet import Fernet
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

# ---------------------------- ENCRYPTION SETUP ------------------------------- #

def generate_key():
    return Fernet.generate_key()

def load_key():
    return open("secret.key", "rb").read()

def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Generate and save key if it doesn't exist
try:
    key = load_key()
except FileNotFoundError:
    key = generate_key()
    save_key(key)

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
        encrypted_data = all_data[website]
        decrypted_data = json.loads(decrypt_data(encrypted_data, key))
        return decrypted_data
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
    password_import_text.insert(END, string=new_password)
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
        data = json.load(read_file())
        data.update(new_data)
        json.dump(data, write_file(), indent=4)
    except FileNotFoundError:
        json.dump(new_data, write_file(), indent=4)

def save_data_to_file():
    website = website_import_text.get().capitalize()
    email_username = email_username_import_text.get()
    password = password_import_text.get()
    new_data = {
        website: encrypt_data(json.dumps({
            "email": email_username,
            "password": password,
        }), key).decode()
    }
    if (is_a_field_blank(website, email_username, password) == True):
        return
    if (confirmation_message_box(website=website, email=email_username, password=password) == True):
        write_to_file_new_data(new_data=new_data)
        empty_fields()
        print(f"{website} | {email_username} | {password}")

# ---------------------------- MENU BAR ------------------------------- #

def copy_password(password):
    pyperclip.copy(password)

def add_new_components(data, saved_password_window, row_for_labels):
    for website in data:
        website_name_label = Label(
            saved_password_window, text=website, fg="blue")
        website_name_label.grid(
            row=row_for_labels, column=0, sticky="EW")
        email_username_name_label = Label(
            saved_password_window, text=data[website]["email"], fg="blue")
        email_username_name_label.grid(
            row=row_for_labels, column=2, sticky="EW")
        password_button = Button(
            saved_password_window, text=data[website]["password"])
        password_button.config(command=lambda password_args=password_button: copy_password(
            (password_args.cget('text'))))
        password_button.grid(row=row_for_labels, column=4, sticky="EW")
        print(data[website])
        row_for_labels = row_for_labels + 1

def create_menu(saved_password_window):
    row_for_labels = 2
    try:
        with open("data.json") as saved_passwords_file:
            data = json.load(saved_passwords_file)
    except json.decoder.JSONDecodeError or FileNotFoundError:
        no_file_found_label = Label(
            saved_password_window, text="No saved data for now !", fg="red")
        no_file_found_label.grid(row=2, column=2, sticky="EW")
    else:
        add_new_components(data, saved_password_window, row_for_labels