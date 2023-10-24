import pyfiglet

def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders:
        name, bid = bidder
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name
    return highest_bidder, highest_bid

def display_welcome_message():
    # Generate the welcome message using pyfiglet
    welcome_message = pyfiglet.figlet_format("Auction Time!")
    print(welcome_message)

def main():
    bidders = []

    display_welcome_message()

    while True:
        name = input("Enter your name: ")
        bid = float(input("Enter your bid: $"))

        bidders.append((name, bid))

        another_bidder = input("Are there any other bidders? (yes/no): ").lower()
        if another_bidder != 'yes':
            break

    highest_bidder, highest_bid = find_highest_bidder(bidders)

    print(f"The highest bid is ${highest_bid} by {highest_bidder}.")

if __name__ == "__main__":
    main()
