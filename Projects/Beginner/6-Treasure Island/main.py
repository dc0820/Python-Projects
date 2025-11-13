print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if first == "left":
    second = input("You come to a shore of a lake. What do you do? Type \"swim\" or \"wait\"\n").lower()
    if second == 'wait':
        third = input("A boat is there to pick you up. Among from there there you are taken to the Treasure Island. There you"
              " see that there are three mysterious doors, a \"red\", \"blue\" and a \"green\" door, what do you choose?\n").lower()
        if third == "red":
            print("You are engulfed in fire, Game Over!")
        elif third == "blue":
            print("You are eaten by a pack of wolves, Game Over!")
        elif third == "green":
            print("You have found the treasure of Tressure Island, Congrats!\nYou Win!")
        else:
            print("You turn around, maybe a wise decision, you may have became rich or have died, who knows...")
    else:
        print("A shark has eaten you. Game Over")
else:
    print("You fell into a hole. Game Over")
