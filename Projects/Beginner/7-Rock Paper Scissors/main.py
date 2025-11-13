import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player >= 3 or player < 0:
    print("Not a valid response.")
else:
    print(f"\nYou chose:\n{choices[player]}")

    computer = random.randint(0, 2)
    print(f"Computer chose:\n{choices[computer]}")

    if player == computer:
        print("It's a tie!")
    elif (player - computer) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")

#player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#choices = [rock, paper, scissors]

#computer = random.choice(choices)
'''
if player == 0:
    print("You chose rock.")
    print(choices[0])
    if computer == choices[0]:
        print("Computer chose rock.")
        print(choices[0])
        print("It is a tie.")
    elif computer == choices[1]:
        print("Computer chose paper.")
        print(choices[1])
        print("You lose.")
    else:
        print("Computer chose scissors.")
        print(choices[2])
        print("You Win.")
elif player == 1:
    print("You chose paper.")
    print(choices[1])
    if computer == choices[1]:
        print("Computer chose paper.")
        print(choices[1])
        print("It is a tie.")
    elif computer == choices[2]:
        print("Computer chose scissors.")
        print(choices[2])
        print("You lose.")
    else:
        print("Computer chose rock.")
        print(choices[0])
        print("You Win.")

elif player == 2:
    print("You chose scissors.")
    print(choices[2])
    if computer == choices[2]:
        print("Computer chose scissors.")
        print(choices[2])
        print("It is a tie.")
    elif computer == choices[0]:
        print("Computer chose rock.")
        print(choices[0])
        print("You lose.")
    else:
        print("Computer chose paper.")
        print(choices[1])
        print("You Win.")
else:
    print("Not a valid response")
'''