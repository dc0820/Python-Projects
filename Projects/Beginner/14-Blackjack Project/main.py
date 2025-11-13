# Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(u_score, c_score):
    if u_score == c_score:
        return "It's a tie!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif c_score == 0:
        return "Computer wins with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Computer went over. You win 😁"
    elif u_score > c_score:
        return "You win 🎉"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your first cards are: {user_cards} Your score: {user_score}")
        print(f"Computer first cards is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            new_deal = input("Would you like to deal another card, 'y' for cards, 'n' for pass: ").lower()
            if new_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
       #computer turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()

