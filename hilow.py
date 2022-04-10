import random

secret_number = random.randint(1,100)
guessed_correctly = False
guess_counter = 0

while guessed_correctly == False:
	guess = int(input("What is your guess? "))
	guess_counter += 1
	if guess == secret_number:
		print("You did it!")
		guessed_correctly = True
	elif guess > secret_number:
		print("Too high!")
	else:
		print("Too low!")

print(F"It took you {guess_counter} guesses!")