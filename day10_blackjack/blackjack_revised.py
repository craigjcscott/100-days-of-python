import os
import random
import art

def deal_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21:
        for card in hand:
            if card == 11:
                hand.remove(card)
                hand.append(1)
    return sum(score)

def compare(player, dealer):
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)
    
    if dealer_score == 0:
        game_running = False
        print("Dealer has BlackJack! You lose")
    elif player_score == 0:
        game_running = False
        print("Player has BlackJack! You win")
    elif player_score > 21:
        game_running = False
        print("Player went bust! You Lose")


start_game = input("Do you want to play a game of blackjack? Enter 'y' for yes, or 'n' for no. ")
if start_game.lower() == 'y':
    game_running = True

# def blackjack():
    
#     os.system('clear')

#     print(art.logo)

while game_running:

    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deal_card)
        dealer_hand.append(deal_card)










#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

