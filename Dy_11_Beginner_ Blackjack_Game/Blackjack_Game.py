import random
import pyfiglet

# Function to deal a random card
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Function to calculate the total value of a hand, considering Aces
def calculate_hand_value(hand):
    value, aces = 0, hand.count('A')
    for card in hand:
        if card in '2 3 4 5 6 7 8 9 10'.split():
            value += int(card)
        elif card in 'J Q K'.split():
            value += 10
        elif card == 'A':
            value += 11
    while aces > 0 and value > 21:
        value -= 10
        aces -= 1
    return value

# Function to display the welcome message using pyfiglet
def display_welcome_message():
    print(pyfiglet.figlet_format("Blackjack"))

# Main Blackjack game function
def blackjack():
    user_name = input("Enter your name: ")
    display_welcome_message()

    while True:
        # Initialize player and dealer hands with two cards each
        player_hand, dealer_hand = [deal_card(), deal_card()], [deal_card(), deal_card()]

        outcome = None  # Initialize outcome here

        print(f"Your hand: {', '.join(player_hand)}")
        print(f"Dealer's face-up card: {dealer_hand[0]}")

        while True:
            player_value = calculate_hand_value(player_hand)
            if player_value == 21:
                outcome = f"Blackjack! You win, {user_name}!"
            elif player_value > 21:
                outcome = f"Bust! You lose, {user_name}."
            else:
                action = input("Do you want to hit or stand? ").lower()
                if action == 'hit':
                    player_hand.append(deal_card())
                    print(f"Your hand: {', '.join(player_hand)}")
                elif action == 'stand':
                    while calculate_hand_value(dealer_hand) < 17:
                        dealer_hand.append(deal_card())
                    dealer_value = calculate_hand_value(dealer_hand)
                    if dealer_value > 21:
                        outcome = f"Dealer busts! You win, {user_name}!"
                    elif dealer_value >= player_value:
                        outcome = f"Dealer wins, {user_name}!"
                    else:
                        outcome = f"You win, {user_name}!"

            if outcome:
                print(f"Your hand: {', '.join(player_hand)}")
                print(f"Dealer's hand: {', '.join(dealer_hand)}")
                print(pyfiglet.figlet_format(outcome))
                break

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    blackjack()
