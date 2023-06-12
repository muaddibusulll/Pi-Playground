from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

#from_language = "Greek"
#to_language = "English"

from_language = "English"
to_language = "Greek"

words_data = pandas.read_csv("data/Often_Used_Words_En_Gr_De.csv")
word_records_dictionary = words_data.to_dict("records")

    
# ---------------------------- MENU BAR ------------------------------- #

def create_menu():
    languages = words_data.to_dict(orient="split")["columns"]
    options_window = Tk()
    options_window.title("Language Settings")
    options_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    # ---------------------- From language ---------------------- #
    def from_language_list_box_used(event):
        '''A function where we change the language in order to give the user more options 
        in what language to learn. In this function we just change the value of the global
        variable from_language from the selected item from the list.'''
        global from_language
        from_language=from_language_listbox.get(from_language_listbox.curselection())
        flash_card_canvas.itemconfig(initial_text, text="")
        flash_card_canvas.itemconfig(initial_text, text=from_language)
        
    from_language_label = Label(options_window, text="From Language", pady=15, bg=BACKGROUND_COLOR)
    from_language_label.grid(row=0, column=0, sticky="EW")
    
    from_language_listbox = Listbox(options_window, height=4)
    for language in languages:
        from_language_listbox.insert(languages.index(language), language)
    from_language_listbox.bind("<<ListboxSelect>>", from_language_list_box_used)
    from_language_listbox.grid(row=2, column=0, sticky="EW")
        
    # # ---------------------- To language ---------------------- #
    to_language_label = Label(options_window, text="To Language", pady=15, bg=BACKGROUND_COLOR)
    to_language_label.grid(row=0, column=3, sticky="EW")

    def to_language_list_box_used(event):
        # TODO: Need to change the actual languages
        print("To the first list: ", to_language_listbox.get(to_language_listbox.curselection()))
        
    to_language_listbox = Listbox(options_window, height=4)
    for language in languages:
        to_language_listbox.insert(languages.index(language), language)
    to_language_listbox.bind("<<ListboxSelect>>", to_language_list_box_used)
    to_language_listbox.grid(row=2, column=3, sticky="EW")
    
    options_window.mainloop()

# ---------------------------- Random Word Function ------------------------------- #

def pick_random_word():
    if from_language == "Greek":
        pick_random_word = random.choice(word_records_dictionary)["Greek"]
        flash_card_canvas.itemconfig(word_text, text=pick_random_word)
        return pick_random_word
    elif from_language == "English":
        pick_random_word = random.choice(word_records_dictionary)["English"]
        flash_card_canvas.itemconfig(word_text, text=pick_random_word)
        return random.choice(word_records_dictionary)["English"]
    else:
        pick_random_word = random.choice(word_records_dictionary)["German"]
        flash_card_canvas.itemconfig(word_text, text=pick_random_word)
        return random.choice(word_records_dictionary)["German"]

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
flash_card_canvas = Canvas(window, width=800, height=526)
flash_card_front_image = PhotoImage(file="images/card_front.png")
flash_card_canvas.create_image(400, 263, image=flash_card_front_image)

initial_text = flash_card_canvas.create_text(400, 150, text=from_language, font=LANGUAGE_FONT)
word_text = flash_card_canvas.create_text(400, 263, text=random.choice(word_records_dictionary)[from_language], font=WORD_FONT)

flash_card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_word_button = Button(image=wrong_image, command=pick_random_word)
wrong_word_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_word_button = Button(image=right_image, command=pick_random_word)
right_word_button.grid(row=1, column=1)

# -------------------- Menu Bar import area -------------------- #
menubar = Menu(window)
options = Menu(menubar, tearoff=0)

options.add_command(label="Flash Card Options", command=create_menu)
options.add_command(label="Back")

options.add_separator()

options.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="Options", menu=options)

window.config(menu=menubar)


window.mainloop()
