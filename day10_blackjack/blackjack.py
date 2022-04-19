import numpy as np
import os
import art

os.system('clear')
print(art.logo)


cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
fulldeck = np.repeat(cards,4)

hand = np.random.choice(fulldeck, 2, replace=False)
first_card = hand[0]
second_card = hand[1]

print(f'Your first card is {first_card}')
print(f'Your second card is {second_card}')
print(f'Hand sum is {sum(hand)}')

