# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:36:15 2025

@author: adars
"""

from breezypythongui import EasyFrame
import random

class NumberGuessingGame(EasyFrame):
    def __init__(self):
        # Initialize the frame with title and fixed size
        super().__init__(title="Number Guessing Game")
        self.setSize(350, 200)
        self.setResizable(False)

        # Initialize game variables
        self.target_number = random.randint(1, 100)
        self.attempts_count = 0

        # Add GUI components
        self.addLabel("Guess a number between 1 and 100:", row=0, column=0, columnspan=2, sticky="NSEW")
        self.guess_input = self.addIntegerField(value=0, row=1, column=0, sticky="EW")
        self.addButton("Guess", row=1, column=1, command=self.check_guess)
        self.result_message = self.addLabel("", row=2, column=0, columnspan=2, sticky="NSEW")

    def check_guess(self):
        # Increment attempt count
        self.attempts_count += 1
        user_guess = self.guess_input.getNumber()

        # Compare guess with target number and display appropriate message
        if user_guess < self.target_number:
            message = "Try a higher number!"
        elif user_guess > self.target_number:
            message = "Try a lower number!"
        else:
            message = f"Congratulations! You guessed it in {self.attempts_count} attempts!"
            # Reset game after a correct guess
            self.target_number = random.randint(1, 100)
            self.attempts_count = 0

        # Update the result message label
        self.result_message['text'] = message

if __name__ == "__main__":
    NumberGuessingGame().mainloop()
