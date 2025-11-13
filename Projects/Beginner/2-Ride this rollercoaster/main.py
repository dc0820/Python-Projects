print("Welcome to the rollercoaster!")
age = int(input("What is your age? "))

if age >= 18:
    height = int(input("What is your height in cm? "))
    if height >= 120:
        print("You are over the age of 18 and over the height to ride\nYour cost of entry is $12 for adult entry")
    else:
        print("You may be old enough, but you don't meet the height requirements")
elif 12 < age < 18:
    height = int(input("what is your height in cm?"))
    if height >= 120:
        print("You are between 12 and 18 and over the height to ride\nYour cost of entry is $7 for teenager entry")
    else:
        print("You don't meet the height requirements")
elif 7 < age < 12:
    height = int(input("what is your height in cm?"))
    if height >= 120:
        print("You are under 12 and over the height to ride\nYour cost of entry is $5 for child entry")
    else:
        print("You don't meet the height requirements")
else:
    print("Your child can't ride the rides.\nEntry fee is free")
