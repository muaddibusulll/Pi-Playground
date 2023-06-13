# Flash Card Game 🪪

### Front Card

![alter text](https://github.com/sifisKoen/Pi-Playground/blob/main/ReadMe%20images/Flash_card_front.png)


### Back Card

![alter text](https://github.com/sifisKoen/Pi-Playground/blob/main/ReadMe%20images/Flash_card_back.png)

This is a Flash Card Game for learning new words from other languages. Currently there are only three languages.

- English
- Greek
- German

This program builded so to help learn a new language. It works very simple, it just show to user a word and it will wait for some time until 
show the translation of the word.

---

## Tools 🪛

For my word list I used:

- Wiktionary
  For my English words. I used this because I needed to find the most common words for English.

Then I used Google Sheets, where I put all the words that I wanted and clean up some of the useless data. Then for the other two languages I just used a Sheet macro just to translate the words.

The macro I used is: `=GOOGLETRANSLATE(A2, "en", "el")` you can change the languages according to your preferences.
More information you can find here: [Translation Tool][Language Support Link]

[Language Support Link]: https://cloud.google.com/translate/docs/languages

For my UI I used:

- tkinter
  Tkinter is a python library witch is use to create UIs in Python. 

---

## How to run it ⚙️

It's very simple

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.

  - Now go to the **/Flash Card Game** directory and open your terminal.
    - From your terminal type, `python3 main.py`

You also can just copy and paste this command in your command line, and the program should run.
`cd Pi-Playground/Flash\ Card\ Game/ ; python3 main.py`

---

## The structure of the project 📚

    ├── data
    │   └── Often_Used_Words_En_Gr_De.csv
    ├── images
    │   ├── card_back.png
    │   ├── card_front.png
    │   ├── right.png
    │   └── wrong.png
    ├── main.py
    └── README.md


### Class Explanation 📖

We have one class the main where all the program runs. There are several **functions** in main witch are worth to mention.

- **create_menu()**
  - This function is responsible to create the menu where we have the functionality to change the languages of preference, for example if we want to have a word from English to German we can go there and choose to change the language **to_language** to German.
- **pick_random_word()**
  - This function helps to pick a random dictionary from our csv and the correct word from it, that user wonts to learn it.
- **flip_card()**
  - This function is using to "flip" the card and reveal to the user the word in translation, depending in witch language the user wants to translate to.
