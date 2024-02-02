from logo_art import logo

# Create Dictionary
current_bids = {}

# Global
other_users = "y"

# Show the Logo
print(logo)


def add_bid():
    # Ask for the name
    name = input("What is your name?/n")

    # Ask for bid price
    bid = float(input("What is your bid price?\n"))

    # Add name and bid to the dictionary
    current_bids[name] = bid

while other_users == "y":
    add_bid()
    other_users = input("Would anyone else like to bid?\nY for yes or N for no\n")
    other_users = other_users.lower()

max = 0.0
winner = ""
for key in current_bids:
    if current_bids[key] > max:
        max = current_bids[key]
        winner = key

print(f"The winner is {winner} with a bid of {current_bids[winner]}")






