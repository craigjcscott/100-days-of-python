import os
import random
import art

start_game = input("Do you want to play a game of blackjack? Enter 'y' for yes, or 'n' for no. ")
if start_game.lower() == 'y':
    game_running = True

def draw_card(hand):
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    hand.append(random.choice(cards))
    
def check_if_bust(hand):
    if sum(hand) > 21:
        for card in hand:
            if card == 11:
                card = 1
                
def show_hand(hand):
    print(f'Cards: {hand}, Score: {sum(hand)}')

def blackjack():
    
    os.system('clear')

    print(art.logo)
    
    player_hand = []
    dealer_hand = []

    for i in range(2):
        draw_card(player_hand)
        draw_card(dealer_hand)

    if sum(dealer_hand) == 21:
        print(f'Dealer has BlackJack! You lose. Your final hand: {player_hand}, Your final score: {sum(player_hand)}')
        print(f'Computer final hand: {dealer_hand}, final score: {sum(dealer_hand)}')
        return
    elif sum(player_hand) == 21:
        print(f'You have BlackJack! You win. Your final hand: {player_hand}, Your final score: {sum(player_hand)}')
        print(f'Computer final hand: {dealer_hand}, final score: {sum(dealer_hand)}') 
        return
    else:
        show_hand(player_hand)
        print(f"The dealer's second card is: {dealer_hand[1]}")
        player_turn = True
        
    while player_turn:
        hit_or_stick = input("Type 'y' to get another card, type 'n' to pass. ")
        if hit_or_stick.lower() == 'y':
            draw_card(player_hand)
            check_if_bust(player_hand)
            if sum(player_hand) > 21:
                print(f'You went bust! Your final hand: {player_hand}, Your final score: {sum(player_hand)}')
                print(f'Computer final hand: {dealer_hand}, final score: {sum(dealer_hand)}')      
                player_turn = False
                return
            else:
                show_hand(player_hand)
        else:
            player_turn = False
            dealer_turn = True
            
    while dealer_turn:
        print('Dealers turn now...')
        while sum(dealer_hand) <=16:
            print('Dealer hits')
            draw_card(dealer_hand)
            check_if_bust(dealer_hand)
            show_hand(dealer_hand)
        
        if sum(dealer_hand) > 21:
            print(f'Dealer went bust! Your final hand: {player_hand}, Your final score: {sum(player_hand)}')
            print(f'Computer final hand: {dealer_hand}, final score: {sum(dealer_hand)}')      
            dealer_turn = False
        elif sum(dealer_hand) >= sum(player_hand):
            print(f'Dealer wins! Your final hand: {player_hand}, Your final score: {sum(player_hand)}')
            print(f'Computer final hand: {dealer_hand}, final score: {sum(dealer_hand)}')
        else:
            print(f'You win! Your final hand: {player_hand}, Your final score: {sum(player_hand)}')
            print(f'Computer final hand: {dealer_hand}, final score: {sum(dealer_hand)}')
        dealer_turn = False

        return

while game_running:
    blackjack()
    
    play_again = input("Do you want to play again? Enter 'y' for yes, or 'n' for no. ")
    if play_again.lower() != 'y':
        game_running = False