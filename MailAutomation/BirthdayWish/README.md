# Birthday Wish Automated mail

This a program so to automated send mails to people so to wish them happy birthday :partying_face:


---

## Tools 🪛

For this project used smtp technology so to send mails. And to use it in **Python** I used import **smtplib** library of Python.

>NOTE: **smtplib** is a pre-build library in **Python**.

Additionally I used **pandas** witch is a **Python** library witch helps us to take information from *csv* files and manipulate them. In this particular program I have a *scv* file naming (birthdays.csv) where I have the information for each person which I want to send e-mails so to wish them.

---

## How to run it ⚙️

### Very important 

You need first go to **main.py** and make some changes in the **mail** and **password**. There are instructions in the code.

First run this command:
`cd Pi-Playground/MailAutomation/BirthdayWish/`

And then open the **main.py** in your editor of your preference. And as I mentioned just change the rows that includes:

```python
MY_EMAIL = "your-mail"
MY_PASSWORD = "your-password"
```

After that just open the **birthdays.csv** file and add your wanted information.

And you are good to go. :blush:

### After configuration

- First you need to to have **Python 3** installed. (You probably have it).
- Then you need to _clone_ my repository.
  - Use `git clone <the name of the repo>`

* Now you should have the whole repository in your machine.

  - Now go to the **/MailAutomation/BirthdayWish** directory and open your terminal.
    - From your terminal type, `python3 main.py`

You can also run this command too:
`cd Pi-Playground/MailAutomation/BirthdayWish/ ; python3 main.py`

---

## The structure of the project 📚

    ├── birthdays.csv
    ├── letter_templates
    │   ├── letter_1.txt
    │   ├── letter_2.txt
    │   └── letter_3.txt
    ├── main.py
    ├── README.md
    └── wish_letter.txt

---

### Class Explanation 📖

In this project we have one class where the whole job done the **main**.

In **main** there are four functions.

- **pick_random_letter_copy_letter()**
  This function pick a random mail template from the *letters_templates* directory and copy it in the **main.py** directory.
- **rewrite_letter(birthday_name)**
  In this function just change the *[NAME]* hard-coded line in the txt files and add the correct name.
- **send_mail(name, content, to_address)**
  This function actually takes the **name** of the current person, the **random letter** with the correct name and the address witch the letter must be send to. And sends the wish letter.
- **check_day()**
  Last but not least this function check if the current day is correct birthday day for each of our people in our csv and if the day is correct then calls the **send_mail** function so to send the mail.