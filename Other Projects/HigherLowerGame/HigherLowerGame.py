import random
from game_data import data
from art import logo, vs
from replit import clear


def userChoice():
    """This function let the user to choose what dose thinks has the most followers.
    And returns the answer of the user"""

    UserChoice = input("Who has more followers? Type 'A' or 'B': ")

    while (UserChoice != 'A') and (UserChoice != 'B'):
        UserChoice = input("Who has more followers? Type 'A' or 'B': ")

    return UserChoice


def comparison(firstContestant, secondContestant, UserChoice):
    """A function witch takes the two random Contestants as dictionary
    and the users choice. And it depends what user choose returns True or False"""

    if UserChoice == 'A':
        # Check if the user choose A if the first contestant has actually more followers if yes return true
        if firstContestant['follower_count'] > secondContestant['follower_count']:
            return True
        else:
            return False
    else:
        if secondContestant['follower_count'] > firstContestant['follower_count']:
            return True
        else:
            return False


firstContestant = {}
secondContestant = {}
contestants = data
userScore = 0
GameEnds = False
firstContestant = random.choice(contestants)
print(logo)
while GameEnds == False:
    # Choose two random contestant from the list data

    secondContestant = random.choice(contestants)

    while (firstContestant == secondContestant):
        secondContestant = random.choice(contestants)

    print(
        f"Cont1: {firstContestant['follower_count']}\nCont2: {secondContestant['follower_count']}")

    print(
        f"Compare A: {firstContestant['name']}, a  {firstContestant['description']}, from {firstContestant['country']}")
    print(vs)
    print(
        f"Compare B: {secondContestant['name']}, a  {secondContestant['description']}, from {secondContestant['country']}")

    if (comparison(firstContestant, secondContestant, userChoice()) == True):
        clear()
        print(logo)
        userScore += 1
        print(f"You\'r right! Current score: {userScore}")
        firstContestant = secondContestant
    else:
        clear()
        print(logo)
        print(f"Sorry, that\'s wrong. Final score: {userScore}")
        GameEnds = True
