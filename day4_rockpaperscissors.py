import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

graphics = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0,2)

print('1... 2.... 3.... Go!')
print('Player chooses....')
print(graphics[player_choice])
print('Computer chooses...')
print(graphics[computer_choice])


# if computer_choice == player_choice:
# 	pring('It\'s a draw! Please play again')
	
if computer_choice == 0:
  if player_choice == 0:
    print('Draw! Please play again.')
  elif player_choice == 1:
    print('Player wins!')
  else:
    print('Computer wins!')

if computer_choice == 1:
  if player_choice == 0:
    print('Computer wins!')
  elif player_choice == 1:
   print('Draw! Please play again.')
  else:
    print('Player wins!')

if computer_choice == 2:
  if player_choice == 0:
    print('Player wins!')
  elif player_choice == 1:
   print('Computer wins!')
  else:
    print('Draw! Please play again.')

