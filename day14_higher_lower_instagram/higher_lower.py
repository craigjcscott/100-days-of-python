import os
import random
import art
import game_data

def random_profile():
	return random.choice(game_data.data)

def higher_lower():
	game_over = False

	correct_guesses = 0
	previous_profile = ''

	while not game_over:
		if previous_profile == '':
			profile_1 = random_profile()
		else:
			profile_1 = previous_profile
		profile_2 = random_profile()

		os.system('clear')
		print(art.logo)

		print(f"Compare A: {profile_1['name']}, a {profile_1['description']}, from {profile_1['country']}.")
		print(art.vs)
		print(f"Against B: {profile_2['name']}, a {profile_2['description']}, from {profile_2['country']}.")

		guess = input("Who has more followers? Type 'A' or 'B': ")
		if (guess == 'A' and profile_1['follower_count'] > profile_2['follower_count']) or (guess == 'B' and profile_2['follower_count'] > profile_1['follower_count']):
			previous_profile = profile_2
			correct_guesses += 1
		else:
			game_over = True
			print(f"Sorry, that's wrong. Final score: {correct_guesses}.")


higher_lower()
