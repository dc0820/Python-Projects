# TODO-1: Ask the user for input
from art import logo

print(logo)


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with ${highest_bid}")

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
continue_bidding = True
bids = {}

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif other_bidders == "yes":
        print("\n" * 20)

# TODO-4: Compare bids in dictionary
