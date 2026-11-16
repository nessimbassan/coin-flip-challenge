# THIS SECTION IMPORTS A FUNCTION FROM OPEN SOURCE LIBRARIES TO GENERATE A RANDOM NUMBER
import random

# THIS SECTION DEFINES THE VARIABLES USED IN THE PROGRAM
flip = 0     # result of the latest coin flip (1 = heads, 2 = tails)
guess = 0    # the player's latest guess
wins = 0     # correct guesses counter
tries = 0    # tries taken counter
goal = 3     # correct guesses needed to win
n = 6        # maximum number of tries allowed

# THIS SECTION CONTAINS THE PROGRAM PROMPTS INTRODUCING THE PROGRAM TO A NEW USER
print("Welcome to the Coin Flip Challenge!")
print("I will flip a coin up to 6 times.")
print("Guess correctly 3 times and you win. Good luck!")

# THIS SECTION CONTAINS THE LOOP THAT LETS THE PLAYER GUESS UP TO 6 TIMES
while wins != goal and tries < n:
    flip = random.randint(1, 2)
    guess = int(input("Enter 1 for heads or 2 for tails: "))
    if guess == flip:
        print("Correct! The coin landed on", flip)
        wins = wins + 1
    else:
        print("Wrong! The coin landed on", flip)
    tries = tries + 1

# THIS SECTION TESTS IF THE PLAYER EXITED THE ABOVE LOOP BY REACHING THE GOAL OR BY BEING OUT OF TRIES
if wins == goal:
    print("You won! You had", wins, "correct guesses in", tries, "tries.")
else:
    print("You lost. You only had", wins, "correct guesses in", tries, "tries.")
