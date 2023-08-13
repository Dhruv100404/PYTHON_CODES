import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def checker(n, a, lives):
    if n > a:
        print("The number is high")
        return lives - 1
    elif n < a:
        print("The number is low")
        return lives - 1
    else:
        print("You guessed it right")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the guessing game!")
    print("I am guessing a number between 0 to 100")
    a = random.randint(0, 100)
    n = 0
    lives = set_difficulty()

    while n != a:
        print(f"You have this many turns  {lives}")
        n = int(input("what do you think the number is?"))
        lives = int(checker(n, a, lives))

        if lives == 0:
            print("You lose")
            print(a)
            return
        else:
            print("guess again")


game()
