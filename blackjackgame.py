import random
import clear


def deal_cards():
    """deal_cards() returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """compares users score and computers score"""
    if user_score == computer_score:
        return "Both scores are the same. Game ends in a draw."
    elif computer_score == 0:
        return "You lose. Computer has blackjack."
    elif user_score == 0:
        return "Blackjack! User wins!"
    elif user_score > 21:
        return "You went over 21... You lose."
    elif computer_score > 21:
        return "Computer went over 21... You win!"
    elif user_score > computer_score:
        return "Your score is greater than the computer's score. Player wins!"
    else:
        return "Computer's score is greater. You lose."


def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    while game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your current cards are {user_cards} and your current score is: {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_again = input("Would you like to draw another card? Type 'y' or 'n': ")
        if draw_again == 'y':
            user_cards.append(deal_cards())
            user_score == calculate_score(user_cards)
        else:
            game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
        print(f"Your final hand was {user_cards} and your final score is: {user_score}")
        print(f"Computer's cards are {computer_cards} and computer's score is: {computer_score}")

    print(compare(user_score, computer_score))
    play_another_game = input("Would you like to play another game of Blackjack? Type 'y' or 'n': ")
    if play_another_game == 'y':
        clear
        play_game()
    else:
        print("Good bye!")


play_game()
