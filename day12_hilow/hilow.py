import os
import random
import art

os.system('clear')
print(art.logo)

def set_difficulty():
	difficulty = input("Choose difficulty: 'easy' (10 guesses) or 'hard' (5 guesses): ")
	if difficulty == 'hard':
		return 5
	else:
		return 10

def user_guess():
	guess = int(input("What is your guess? "))


remaining_guesses = set_difficulty()
guess_limit = remaining_guesses

secret_number = random.randint(1,100)

game_running = True

while game_running:
	print(f"You have {remaining_guesses} turns remaining")
	guess = int(input("What is your guess? "))
	remaining_guesses -= 1
	if remaining_guesses < 0:
		print("Game over!")
	elif guess == secret_number:
		print(f"You did it! It only took you {guess_limit-remaining_guesses} guesses")
		game_running = False
	elif guess > secret_number:
		print("Too high!")
	else:
		print("Too low!")

