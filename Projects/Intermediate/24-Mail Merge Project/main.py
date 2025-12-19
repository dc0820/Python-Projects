PLACEHOLDER = "[name]"


# Read template once
with open("./Input/Letters/starting_letter.txt") as StartingLetter:
    letter_contents = StartingLetter.read()

# Read names and write letters
with open("./Input/Names/invited_names.txt") as InvitedNames:
    for name in InvitedNames:
        stripped_name = name.strip()
        personalized = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as SendLetter:
            SendLetter.write(personalized)
