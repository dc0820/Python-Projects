from game_data import data
import random
import time
import art

def get_random_account():
    """Returns a random account's display info and follower count."""
    account = random.choice(data)
    user_info = f"{account['name']}, a {account['description']}, from {account['country']}."
    return user_info, account['follower_count']

def check_answer(user_choice, follower_a, follower_b):
    """Returns True if the user's guess is correct, else False."""
    if follower_a > follower_b:
        return user_choice == 'a'
    else:
        return user_choice == 'b'

def higher_lower_game():
    print(art.logo)
    score = 0
    game_continues = True

    # Initialize the first two accounts
    user_info_a, follower_a = get_random_account()
    user_info_b, follower_b = get_random_account()

    while game_continues:
        # Avoid duplicate accounts
        while user_info_a == user_info_b:
            user_info_b, follower_b = get_random_account()

        print(f"\nCompare A: {user_info_a}")
        print(art.vs)
        print(f"Against B: {user_info_b}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(user_choice, follower_a, follower_b)
        time.sleep(.6)

        if is_correct:
            score += 1
            print(f"✅ Correct! Current score: {score}\n")
            # Make B the next A and pick a new B
            user_info_a, follower_a = user_info_b, follower_b
            user_info_b, follower_b = get_random_account()
        else:
            print(f"❌ Sorry, that's wrong. Final score: {score}.")
            game_continues = False

# Start the game
if __name__ == "__main__":
    higher_lower_game()
