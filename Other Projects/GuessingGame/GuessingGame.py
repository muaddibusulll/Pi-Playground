from replit import clear
from logo import logo
import random

# Start of function section


def userLevelChoice():
    """A function witch returns the users level choice"""
    UserLevelChoice = ""
    UserLevelChoice = input(
        "Choose a difficulty level. Type 'easy' or 'hard' ")

    while (UserLevelChoice != "easy") and (UserLevelChoice != "hard"):
        UserLevelChoice = input(
            "Choose a difficulty level. Type 'easy' or 'hard' ")

    return (UserLevelChoice)


def playerPlayAgain():
    """A function witch asks the user if wants to continue the game
    and returns True or False depending on users answer"""
    UserPlayAgain = ""
    UserPlayAgain = input("Do you want to play again? Type 'yes' or 'no' ")

    while (UserPlayAgain != "yes") and (UserPlayAgain != "no"):
        UserPlayAgain = input("Do you want to play again? Type 'yes' or 'no' ")

    if (UserPlayAgain == "yes"):
        clear()
        return False
    else:
        clear()
        print("See you !! 👋")
        return True


def userGuess():
    """A function which check if the input of the user is
    a valid integer number, and if it is valid it returns 
    that number"""
    UserGuessNumber = input("Make a guess: ")

    while not UserGuessNumber.isdigit():
        UserGuessNumber = input("Make a guess: ")

    return UserGuessNumber


def guessingTheNumber(NumberOfAttempts, MagicNumber):
    """A function where the game takes place and prints
    if the user won or lost"""

    while NumberOfAttempts != 0:
        print(
            f"You have {NumberOfAttempts} attempts remaining to guess the number")
        UserGuessNumber = int(userGuess())
        if (UserGuessNumber > MagicNumber):
            print("Too high.")
            NumberOfAttempts -= 1
        elif (UserGuessNumber < MagicNumber):
            print("Too low.")
            NumberOfAttempts -= 1
        else:
            print("You won ! 🥳")
            return playerPlayAgain()

        if (NumberOfAttempts == 0):
            print("You lost 😞")
            return playerPlayAgain()

# End of function section


NumberOfAttempts = 0
GameEnds = False


while not GameEnds:
    MagicNumber = random.randint(1, 100)
    # Testing
    print(MagicNumber)
    print(logo)
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100")

    UserLevelChoice = userLevelChoice()
    if UserLevelChoice == "easy":
        NumberOfAttempts = 10
        GameEnds = guessingTheNumber(NumberOfAttempts, MagicNumber)
    else:
        NumberOfAttempts = 5
        GameEnds = guessingTheNumber(NumberOfAttempts, MagicNumber)
