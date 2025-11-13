import random
import art
import time

# def compare(choice, correct_number):
#     if choice > correct_number:
#         return "Too high.\nGuess again."
#     elif choice < correct_number:
#         return "Too low.\nGuess again."
#     else:
#         return f"You got it! The answer was {correct_number}"

# def play_game():
#     print(art.logo)
#     print("Welcome to the Number Guessing Game")
#     print("I'm thinking of a number between 1 and 100.")
#
#
#     chosen_number = random.randint(1,100)
#     #print(chosen_number)
#     easy_attempts = 10
#     hard_attempts = 5
#     continue_guessing = True
#
#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#
#     if difficulty == 'easy':
#         attempts = easy_attempts
#     else:
#         attempts = hard_attempts
#
#     while continue_guessing:
#             guess = int(input("Make a guess: "))
#             time.sleep(1)
#             print(compare(guess, chosen_number))
#             if guess == chosen_number:
#                 continue_guessing = False
#             else:
#                 attempts -= 1
#                 if attempts == 0:
#                     print(f"You've run out of guesses")
#                     continue_guessing = False
#                 else:
#                     print(f"You have {attempts} attempts remaining to guess the number")
#
# while input("Do you want to play the Number Guessing Game, type 'y' or 'n': ").lower() == 'y':
#     play_game()

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return 10
    else:
        return 5

def make_guess():
    u_guess = int(input("Make a guess: "))
    return u_guess

def compare(choice, correct_number):
    if choice > correct_number:
        return "Too high.\nGuess again."
    elif choice < correct_number:
        return "Too low.\nGuess again."
    else:
        return f"You got it! The answer was {correct_number}"

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    attempts = set_difficulty()
    while attempts > 0:
        guess = make_guess()
        print(compare(guess, number))
        time.sleep(1)
        if guess == number:
            return
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    print("You have no attempts left")

while input("Do you want to play the Number Guessing Game, type 'y' or 'n': ").lower() == 'y':
    play_game()