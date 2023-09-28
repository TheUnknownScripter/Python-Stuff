#Made By TheUnknownScripter In Python | This is a simple little mini game for fun that you have to pick the difficulty and guess the number between 1 and x with some simple little hint's have fun

import random

def Randomizer(x):
    Rand = random.randint(1, x)
    CurrentGuess = 0
    print(f"Your guessing is between 1 and {x}")
    while CurrentGuess != Rand:
        try:
            CurrentGuess = int(input(f"Guess a number between 1 and {x} : "))
            if CurrentGuess < Rand:
                print("Yea no that guess was to Low try again")
            elif CurrentGuess > Rand:
                print("Yea no that guess was to High try again")
        except ValueError:
            print("Yea no Invalid Input has to be a number try again")
    print(f"You guessed the right number : {CurrentGuess}")

Difficultys = ["easy", "normal", "hard", "extreme", "godly"]

while True:
    Diff = input("Select a difficulty from : easy | normal | hard | extreme | godly : ")
    if Diff.lower().strip() == Difficultys[0]:
        Randomizer(random.randint(10, 50))
        break
    elif Diff.lower().strip() == Difficultys[1]:
        Randomizer(random.randint(100, 500))
        break
    elif Diff.lower().strip() == Difficultys[2]:
        Randomizer(random.randint(1000, 5000))
        break
    elif Diff.lower().strip() == Difficultys[3]:
        Randomizer(random.randint(5000, 10000))
        break
    elif Diff.lower().strip() == Difficultys[4]:
        Randomizer(random.randint(1000000, 10000000))
        break
    elif not Diff.lower().strip() in Difficultys:
        print("Invalid Response Retry")
