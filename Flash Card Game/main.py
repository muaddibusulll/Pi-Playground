from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

from_language = "English"
to_language = "Greek"

words_data = pandas.read_csv("data/Often_Used_Words_En_Gr_De.csv")

# ---------------------------- MENU BAR ------------------------------- #

def create_menu():
    languages = words_data.to_dict(orient="split")["columns"]
    options_window = Tk()
    options_window.title("Language Settings")
    options_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    # ---------------------- From language ---------------------- #
    from_language_label = Label(
        options_window, text="From Language", pady=15, bg=BACKGROUND_COLOR)
    from_language_label.grid(row=0, column=0, sticky="EW")

    # Radio button
    language_0 = Radiobutton(options_window,
                             text=languages[0],
                             variable=StringVar(options_window, languages[0]),
                             command=lambda: print(
                                 StringVar(options_window, languages[0]).get()),
                             value=languages[0])
    language_1 = Radiobutton(options_window,
                             text=languages[1],
                             variable=StringVar(
                                 options_window, languages[1]),
                             command=lambda: print(
                                 StringVar(options_window, languages[1]).get()),
                             value=languages[1])
    language_2 = Radiobutton(options_window,
                             text=languages[2],
                             variable=StringVar(options_window, languages[2]),
                             command=lambda: print(
                                 StringVar(options_window, languages[2]).get()),
                             value=languages[2])
    language_0.grid(row=1, column=0, sticky="EW")
    language_1.grid(row=2, column=0, sticky="EW")
    language_2.grid(row=3, column=0, sticky="EW")
    # # ---------------------- To language ---------------------- #
    to_language_label = Label(
        options_window, text="To Language", pady=15, bg=BACKGROUND_COLOR)
    to_language_label.grid(row=0, column=3, sticky="EW")

    # Radio button

    # Apply Button
    apply_changes_button = Button(options_window, text="Apply Changes")
    apply_changes_button.grid(row=4, column=0, columnspan=4, sticky="EW")

    options_window.mainloop()


# ---------------------------- LOGIN UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
flash_card_canvas = Canvas(window, width=800, height=526)
flash_card_front_image = PhotoImage(file="images/card_front.png")
flash_card_canvas.create_image(400, 263, image=flash_card_front_image)

flash_card_canvas.create_text(400, 150, text="title", font=LANGUAGE_FONT)
flash_card_canvas.create_text(400, 263, text="word", font=WORD_FONT)

flash_card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_word_button = Button(image=wrong_image)
wrong_word_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_word_button = Button(image=right_image)
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
