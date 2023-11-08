import random
import tkinter as tk
from tkinter import simpledialog, messagebox


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        if rank_order.index(self.rank) < rank_order.index(other.rank):
            return True
        elif rank_order.index(self.rank) == rank_order.index(other.rank) and self.suit < other.suit:
            return True
        return False


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num=1):
        if num > len(self.cards):
            num = len(self.cards)
        drawn = self.cards[-num:]
        self.cards = self.cards[:-num]
        return drawn


def play_card_guessing_game():
    deck = Deck()
    deck.shuffle()

    while deck.cards:
        drawn_cards = deck.draw(1)
        if drawn_cards:
            card = drawn_cards[0]

            root = tk.Tk()
            root.withdraw()  # Hide the main window

            guess = simpledialog.askstring("Card Guessing Game", "Guess the card (e.g., 'Queen of Hearts'):")

            if guess is None:
                # User canceled the game
                break

            guess_parts = guess.split(" of ")
            if len(guess_parts) == 2:
                guessed_card = Card(guess_parts[1], guess_parts[0])
                if guessed_card == card:
                    messagebox.showinfo("Card Guessing Game", f"Correct! You guessed: {card}")
                else:
                    messagebox.showinfo("Card Guessing Game", f"Sorry, the card was: {card}")
            else:
                messagebox.showinfo("Card Guessing Game", "Invalid guess format. Use 'Rank of Suit'.")

            root.destroy()

    if not deck.cards:
        messagebox.showinfo("Card Guessing Game", "No cards left in the deck.")


if __name__ == "__main__":
    play_card_guessing_game()
