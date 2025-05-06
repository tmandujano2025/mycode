#!/usr/bin/env python3
"""Number Guessing Game | Step 1"""

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user for their guess
guess = int(input("Guess the number between 1 and 10: "))

# Check if the guess is correct
if guess < 1 or guess > 10:
    print ("Invalid guess. Please enter a number between 1 and 10.")

elif guess == secret_number:
    print("You guessed it! Great job!")
elif guess > secret_number:
    print("Too High!")
elif guess < secret_number:
    print("Too Low!")

