****Objective:****

Develop a text-based Blackjack game that allows a player to play multiple rounds against a computer-controlled dealer. The game should follow standard Blackjack rules, with the player attempting to get a hand value as close to 21 as possible without going over.

**Features:**

**User Initialization:**

The game starts by requesting the user's name.

**Welcome Message:**

Display a stylish welcome message using the PyFiglet library.

**Game Loop:**

The game consists of a loop that allows the user to play multiple rounds until they choose to exit.

**Deal Cards:**

At the beginning of each round, two cards are dealt to the player and the dealer.

**Hand Value Calculation:**

Calculate the total value of a hand, considering Ace cards that can be 1 or 11.

**Player's Turn:**

The player can choose to "hit" (draw another card) or "stand" (keep their current hand).
If the player's hand value reaches 21, they win the round (Blackjack).
If the player's hand value exceeds 21, they lose the round (Bust).

**Dealer's Turn:**

The dealer follows a rule to "hit" until their hand value is 17 or higher.
Outcome Determination:

**Determine the outcome of the round:**

If the dealer busts (exceeds 21), the player wins.
If the player has a higher hand value than the dealer and is not over 21, the player wins.
If the dealer has a higher hand value than the player, the dealer wins.
In case of a tie, the dealer wins.

**Play Again:**

After each round, ask the player if they want to play another round.
The game continues until the player chooses to exit.
Dependencies:

**Run the Python script.**

1.Enter your name when prompted.

2.Play rounds of Blackjack by choosing "hit" or "stand" until you decide to exit.

**Assumptions:**

1.The player follows standard Blackjack rules.

2.The game simulates a single player against a computer-controlled dealer.

**Check blow link for more details about Python Concepts**
https://www.cloudtechtwitter.com/2023/10/understanding-control-flow-in-python.html

