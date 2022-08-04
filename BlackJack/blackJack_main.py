'''
Main method
'''

### -------- Imports --------
import os
import blackjack_objects


### -------- Global Variables --------
FLOP_VALUE = 21
PLAYER_MONEY = 1000
ROUND_COUNTER = 0
ROUND_OUTCOME = ''
GAME_ON = True
BET = 1

### -------- Main --------


# Intro and get name
os.system("cls")
print("Welcome to BlackJack!")
print("\n")
firstname = blackjack_objects.get_player_name()
print("\n")
print(f"Let's start playing {firstname}!")
print("\n")


# Main game loop, can play multiple rounds
while GAME_ON:

    # Round intro, can quit game here
    if ROUND_COUNTER == 0: print(f"{firstname}, you have {PLAYER_MONEY} in cash.")
    print("\n")
    play = blackjack_objects.get_keep_playing()
    print("\n")
    if play == 'quit':
        print("Goodbye.")
        GAME_ON = False
        break
    if PLAYER_MONEY <= 0:
        print("You are out of money and cannot play anymore.")
        print("Goodbye.")
        GAME_ON = False
        break
    ROUND_COUNTER += 1
    BET = blackjack_objects.get_player_bet(PLAYER_MONEY)
    print("\n")
    print(f"Round {ROUND_COUNTER} begins!  The bet is {BET} cash.")
    print("\n")

    # create objects for this round
    player = blackjack_objects.Player()
    dealer = blackjack_objects.Dealer()
    deck = blackjack_objects.Deck(1) # 1 creates a full deck
    deck.shuffle_deck()

    # starting hands
    player.deck.add_card(deck.draw_card())
    dealer.deck.add_card(deck.draw_card())
    player_card = player.deck.deck[-1].get_card_name()
    dealer_card = dealer.deck.deck[-1].get_card_name()
    print(f"{firstname} drew the {player_card}.")
    print(f"Dealer drew the {dealer_card}.")

    # all other plays with decision making
    KEEP_DRAWING = True
    while KEEP_DRAWING:

        # player hits or stays
        print('\n')
        player_choice = blackjack_objects.get_player_choice()
        print('\n')
        if player_choice == 'hit':
            player.status = 'hit'
            player.deck.add_card(deck.draw_card())
            player_card = player.deck.deck[-1].get_card_name()
            print(f"{firstname} drew the {player_card}.")
        elif player_choice == 'stay':
            player.status = 'stay'
            print(f"{firstname} chose to stay.")

        #dealer decides to hit or stay
        dealer.dealer_play(player.deck.get_deck_value())
        if dealer.status == 'hit':
            dealer.deck.add_card(deck.draw_card())
            dealer_card = dealer.deck.deck[-1].get_card_name()
            print(f"Dealer drew the {dealer_card}.")
            dealer.status = ''
        elif dealer.status == 'stay':
            print("Dealer chose to stay.")
        # determine if to continue or end round
        pvalue = player.deck.get_deck_value()
        dvalue = dealer.deck.get_deck_value()

        if pvalue > 21 or dvalue > 21:
            KEEP_DRAWING = False
            break
        elif player.status == 'stay' and dealer.status == 'stay':
            KEEP_DRAWING = False
            break
        else:
            continue

    # Determine win or draw
    pvalue = player.deck.get_deck_value()
    dvalue = dealer.deck.get_deck_value()
    print('\n')
    if pvalue > 21 and dvalue > 21:
        ROUND_OUTCOME = 'draw'
        print(f'Both {firstname} and dealer busted!')
    elif pvalue > 21 and dvalue <=21:
        ROUND_OUTCOME = 'won'
        print(f'{firstname} busted, dealer wins!')
        dealer.status = 'won'
    elif dvalue > 21 and pvalue <= 21:
        ROUND_OUTCOME = 'won'
        print(f'Dealer busted. {firstname} wins!')
        player.status = 'won'
    elif dvalue >= pvalue:
        ROUND_OUTCOME = 'won'
        dealer.status = 'won'
        print('Dealer wins!')
    elif pvalue > dvalue:
        ROUND_OUTCOME = 'won'
        player.status = 'won'
        print(f"{firstname} wins!")
    else:
        raise Exception("Unable to determine win or loss.")

    if ROUND_OUTCOME == 'draw':
        print("The round was a draw, no one wins the bet.")
    elif ROUND_OUTCOME == 'won':
        if dealer.status == 'won':
            print(f"The dealer wins the bet of {BET} cash.")
            PLAYER_MONEY = PLAYER_MONEY - BET
        elif player.status == 'won':
            print(f"{firstname} wins the bet of {BET} cash.")
            PLAYER_MONEY = PLAYER_MONEY + BET
        print(f"{firstname} now has {PLAYER_MONEY} in cash.")

    ROUND_OUTCOME = ''
    player.status = ''
    dealer.status = ''
