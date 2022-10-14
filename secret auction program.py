# Import gavel art file.
import gavel_art
# Print gavel art.
print(gavel_art.logo)
# Variable used as condition to keep while loop running until secret auction end.
auction_ongoing = True
# Highest bid variable set to 0 before bidding starts.
highest_bid = 0
# CLS commands do not work with IDE used to write this program. clear function used as substitute.
def clear():
    print ("\n" * 100)
# While loop runs until all bidders have bid.
while auction_ongoing == True:
# Current bidder information stored in dictionary.
    bidder = {}
# Highest bidder information stored in dictionary.
    highest_bidder = {}
# Ask for name input.
    key = input("What is your name? ")
# Ask for bid amount input.
    value = int(input("What is your bid?: $"))
# Bidder information stored to bidder dictionary.
    bidder[key] = value
# Tests if bidder amount is highest amount.
    if bidder[key] > highest_bid:
# New highest bid amount added.
        highest_bid = bidder[key]
# New key added for highest bidder.
        key2 = key
# New value added for highest bidder.
        value2 = value
# Highest bidder information appended to highest_bidder dictionary.
        highest_bidder[key2] = value2
# Bidder dictionary information reset.
        bidder = {}
    else:
        bidder = {}
# Ask for more bidders input.
    while True:
        auction_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if auction_continue == 'yes':
            clear()
            break
# Output if auction will not continue.
        elif auction_continue == 'no':
            print(f"The winner is {key2} with a bid of ${value2}!")
            auction_ongoing = False
            break
# Will ask for input again if not given 'yes' or 'no'.
        else:
            continue
    
    