#number_guessing_game.py

"""
This is a fun little game where the computer picks 
a number between 1 and 100, and you gotta guess what it is. 
After each guess, it tells you if you’re too high or too low 
until you get it right. It also counts how many tries it 
took you—so try to beat your score!
"""

import random

number = random.randint(1, 100)
attempts = 0

while True:
  try: 
    guess = int(input("Guess a number between 1-100: "))
    attempts += 1
  except ValueError as e:
    print(f"Please try again. {e}")
    continue

  if guess > number:
    print("Too high! Guess again: ")
  elif guess < number:
    print("Too low! Guess again: ")
  else: 
    print(f"Congrats, you guessed the right number in {attempts} tries!\n\
It was {number}.")
    break