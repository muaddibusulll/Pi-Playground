import tkinter


def convert_miles_to_kilometers():
    miles = float(miles_entry.get())
    kilometers = str(round(miles / 0.62137))
    kilometers_output.config(text=kilometers)


LABELS_FONT = ("Arial", 15)

# Window configuration
window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

# Label
my_label = tkinter.Label(text="is equal to",
                         font=LABELS_FONT)
my_label.grid(column=0, row=1)

# Column 1

# Entry
miles_entry = tkinter.Entry(width=10)
miles_entry.insert(tkinter.END, string="0")
miles_entry.grid(column=1, row=0)

# Label for the convert
kilometers_output = tkinter.Label(text="0", font=LABELS_FONT)
kilometers_output.grid(column=1, row=1)

# Button
convert_button = tkinter.Button(
    text="Convert", command=convert_miles_to_kilometers)
convert_button.grid(column=1, row=2)

# Column 2

# Label for miles
miles = tkinter.Label(text="Miles", font=LABELS_FONT)
miles.grid(column=2, row=0)

# Label for kilometers
kilometers = tkinter.Label(text="Km", font=LABELS_FONT)
kilometers.grid(column=2, row=1)


window.mainloop()
