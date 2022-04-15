# TODO

# restrict guesses to allowed guesses list
# Restart the loop upon a previous guess

# Create a new display variable for each guess, and then show all of them each turn

import random
import os
import time
from termcolor import colored
import wordle_answers
import wordle_guesses

possible_answers = wordle_answers.possible_answers
allowed_guesses = wordle_guesses.allowed_guesses

answer = random.choice(possible_answers)

game_finished = False
player_wins = False
player_loses = False
hard_mode = False
guesses_remaining = 6
previous_guesses = []
dead_letters = []

display = ['_','_','_','_','_']
display_array = [['_','_','_','_','_'],
				 ['_','_','_','_','_'],
				 ['_','_','_','_','_'],
				 ['_','_','_','_','_'],
				 ['_','_','_','_','_'],
				 ['_','_','_','_','_']]

os.system('clear')

for row in display_array:
	print(f"{' '.join(row)} \n")

# For dev use, remove upon completion.
# answer = 'tears'
# print(f'psst, the answer is {answer}')

while game_finished == False:

	guess = input("\n Guess a word: ").lower()
	
	if len(guess) != 5:
		print("Word must be 5 letters, please try again.")
		time.sleep(1)
	elif (guess in previous_guesses):
		print("You've already guessed this word, please try again.")
		time.sleep(1)
	elif guess not in (allowed_guesses + possible_answers):
		print('Not a word, please try again.')
		time.sleep(1)
	elif guess == answer:
		guesses_remaining -= 1
		game_finished = True
		player_wins = True
		print("\n Congratulations! You win!")
	else:
		for position in range(0,5):
			if guess[position].lower() == answer[position].lower():
				display[position] = colored(guess[position].lower(), 'green')
			elif guess[position].lower() in (answer[:position] + answer[position+1:]).lower():
				display[position] = colored(guess[position].lower(), 'yellow')
			else: 
				display[position] = '_'
				dead_letters.append(guess[position])

		display_array[guesses_remaining*-1] = display.copy()
		print(f'Letters not in word: {sorted(set(dead_letters))}')
		for row in display_array:
			print(f"{' '.join(row)} \n")

		guesses_remaining -= 1
		previous_guesses.append(guess)

	if guesses_remaining == 0:
		game_finished = True
		player_loses = True
		print(F"Oh no! You lose. The correct answer was {answer}")
  

	# os.system('clear')
  
		
    