import random

from art import logo

print(logo)

from game_data import data


def checker(guess, A, B):
    if A['follower_count'] >= B['follower_count']:
        return "A"
    else:
        return "B"


choice1 = random.choice(data)
choice2 = random.choice(data)

game_over = True
score = 0

while game_over:
    choice1 = choice2
    choice2 = random.choice(data)

    if choice1 == choice2:
        choice2 = random.choice(data)

    print(f"Comapre A : {choice1['name']} , a {choice1['description']}, from {choice1['country']}")
    from art import vs

    print(vs)
    print(f"Against B : {choice2['name']} , a {choice2['description']}, from {choice2['country']}")

    answer = str(input("Who has more followers : Type 'A' or 'B':"))

    is_correct = checker(answer, choice1, choice2)

    if is_correct == answer:
        score += 1
        print(f"Your current score is {score}")
    else:
        game_over = False
        print(f"That's Wrong Your Final score {score}")




