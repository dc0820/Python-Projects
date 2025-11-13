print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (10%, 12%, 15%) "))
people = int(input("How many people to split the bill? "))

total_bill = bill / people * (1 + tip / 100)

print(f"If each person split per meal and added a {tip}% to it, it will be ${total_bill:.2f}")

