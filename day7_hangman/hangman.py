import random
import os
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_finished = False
player_wins = False
player_loses = False
lives = 6
wrong_guesses = []
correct_guesses = []

display = []

for _ in range(word_length):
	display += "_"

print(hangman_art.logo)

input('Press Enter to begin')
os.system('clear')

while game_finished == False:
  

	print(hangman_art.stages[lives])
	print(F"Wrong guesses: {wrong_guesses} \n")
	print(f"{' '.join(display)}")

	guess = input("\n Guess a letter: ").lower()

	if (guess in wrong_guesses or guess in correct_guesses):
		print("You already guessed this letter, please try again")
	elif guess in chosen_word:
		for position in range(word_length):
			letter = chosen_word[position]
			if letter == guess:
				display[position] = letter
				correct_guesses.append(guess)
	else:
		lives -= 1
		wrong_guesses.append(guess)
		wrong_guesses.sort()
		print(F"Wrong guesses: {wrong_guesses}")

	if lives == 0:
		game_finished = True
		player_loses = True
		print(F"Oh no! You lose. The correct answer was {chosen_word}")
	else:
		os.system('clear')
  
	if not '_' in display:
		game_finished = True
		player_wins = True
  
if game_finished == True:
	if player_wins == True:
		print(hangman_art.stages[lives])
		print(f"{' '.join(display)}")
		print("Congratulations! You win!")
    