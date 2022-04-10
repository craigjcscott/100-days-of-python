import os
import cypher_art 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_encoder = True

def ceasar(text, shift, direction):
		output = ''
		if direction == 'decode':
			shift *= -1
		for letter in text:
			if letter in alphabet:
				current_index = alphabet.index(letter)
				new_index = current_index + shift%26
				output += alphabet[new_index]
			else:
				output += letter
		print(output)

while run_encoder:

	os.system('clear')

	print(cypher_art.logo)

	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
	text = input("Type your message: ").lower()
	shift = int(input("Type the shift number: "))

	ceasar(text, shift, direction)

	run_again = input('Do you want to restart the program? yes/no ')

	if run_again == 'no':
		run_encoder = False