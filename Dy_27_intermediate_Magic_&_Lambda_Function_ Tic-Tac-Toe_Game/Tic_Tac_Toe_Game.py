import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = [None] * 9
        self.game_over = False  # Track whether the game is over

        # Increase the frame size by configuring the root window
        self.root.geometry("300x300")

        for i in range(9):
            row, col = divmod(i, 3)
            # Increase button size (width and height) for a larger box
            button = CustomButton(self.root, text="", height=3, width=6)
            button.coords = (row, col)  # Assign coordinates to the button
            button.grid(row=row, column=col)
            button.configure(command=lambda b=button: self.make_move(b))
            self.buttons[i] = button  # Store the button in the list

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game)
        self.play_again_button.grid(row=3, column=0, columnspan=3)
        self.play_again_button.grid_remove()  # Initially hide the "Play Again" button

    def make_move(self, button):
        if not self.game_over:
            # Get the coordinates of the button
            coords = button.coords
            i = coords[0] * 3 + coords[1]

            # Check if the button is available to make a move
            if not self.board[i]:
                self.board[i] = self.current_player
                button["text"] = self.current_player
                self.check_winner()
                # Switch the current player
                self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        # Define win conditions as sets of indices
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            a, b, c = condition
            # Check if any of the win conditions have been met
            if self.board[a] == self.board[b] == self.board[c] and self.board[a]:
                self.game_over = True
                self.disable_buttons()
                self.display_message(f"Player {self.current_player} wins!")
                self.play_again_button.grid()  # Display the "Play Again" button

        if all(self.board) and not self.game_over:
            # If all spaces are filled and no winner, the game is tied
            self.game_over = True
            self.display_message("It's a tie!")
            self.play_again_button.grid()  # Display the "Play Again" button

    def disable_buttons(self):
        for button in self.buttons:
            if button:
                # Disable all buttons to prevent further moves
                button["state"] = tk.DISABLED

    def reset_game(self):
        # Clear the game board and enable buttons
        for i in range(9):
            self.board[i] = ""
            self.buttons[i]["text"] = ""
            self.buttons[i]["state"] = tk.NORMAL
        self.current_player = "X"
        self.game_over = False
        self.play_again_button.grid_remove()  # Hide the "Play Again" button
        self.display_message("")  # Clear the message

    def display_message(self, message):
        # Update the message label to display win/tie messages
        self.message_label.config(text=message)

class CustomButton(tk.Button):
    pass

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    game.message_label = tk.Label(root, text="", font=("Helvetica", 16))
    game.message_label.grid(row=4, column=0, columnspan=3)
    root.mainloop()
