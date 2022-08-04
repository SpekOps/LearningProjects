'''
Module defining main objects in game.
Cards, decks, players.
'''

import random

SUITS = ('Spades','Hearts','Diamonds','Clubs')
RANKS = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
CARD_VALUES = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,
'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
FLOP_VALUE = 21

class Card:
    '''
    Cards.  Have suit, rank, and value.
    Value based on BlackJack values.
    Requires reference data from a tuple
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = CARD_VALUES[self.rank]
        self.name = self.rank+' of '+self.suit

    def get_card_name(self):
        '''
        method info
        '''
        return self.rank+' of '+self.suit

    def __str__(self):
        return self.name



class Deck:
    '''
    Class represents a deck of cards.
    Can create a new deck of cards with new_deck = 1
    Can start an empty deck with new_deck = 0 (default)
    '''

    def __init__(self,new_deck=0):
        self.deck = []

        if new_deck == 1:
            for suits in SUITS:
                for ranks in RANKS:
                    newcard = Card(suits,ranks)
                    self.deck.append(newcard)

    def shuffle_deck(self):
        '''
        Shuffles the deck
        '''

        random.shuffle(self.deck)

    def draw_card(self):
        '''
        Draws one card from top of this deck.
        Removes drawn card from this deck.
        Use on main deck
        Uses pop(-1), returns a Card object
        '''

        return self.deck.pop(-1)

    def add_card(self,added_card):
        '''
        Adds one card to the top of the deck
        Expects Card object
        '''

        if not isinstance(added_card,Card):
            raise TypeError("Must provide a Card type")
        self.deck.append(added_card)

    def get_deck_value(self):
        '''
        Returns the total value of cards in a deck
        '''
        deck_value = 0
        for i in self.deck:
            deck_value = deck_value + i.value
        return deck_value

    def __str__(self):
        printstr = ''
        for i in self.deck:
            printstr = printstr+i.get_card_name()+'\n'
        return printstr

    def __len__(self):
        return len(self.deck)



class Player:
    '''
    Class that defines human player and actions
    Player starts with an empty Deck object
    Has a pot of money
    '''

    def __init__(self):
        self.deck = Deck()
        self.status = ''



class Dealer():
    '''
    Class that defines the card dealer
    Has hit or stay decision making logic
    '''

    def __init__(self):
        self.deck = Deck()
        self.status = ''

    def dealer_play(self,player_sum,dealer_sum=0):
        '''
        Logic to play a round
        Draw card or pass (hit or stay)
        pass in dealer.deck.get_deck_value() for dealer_sum
        '''
        if dealer_sum==0: # allows unit testing by taking non-zero value
            dealer_sum = self.deck.get_deck_value()
        else:
            pass
        if dealer_sum >= FLOP_VALUE or player_sum > FLOP_VALUE:
            self.status = 'stay'
        elif dealer_sum <= FLOP_VALUE-11:
            self.status = 'hit'
        elif dealer_sum >= player_sum:
            self.status = 'stay'
        elif dealer_sum < player_sum:
            self.status = 'hit'



def name_check(name):
    '''
    Validates and corrects name from input.
    Unit testing point for user name input function
    '''
    name = name.split()
    name = (name[0])[0:25:1]
    name = name.title()
    if name.isalpha() == False:
        raise Exception("No special characters.")
    elif len(name) <1:
        raise Exception('Nothing entered.')
    elif name.lower() == "dealer":
        raise Exception("You can't be the dealer.")
    else:
        return name



def get_player_name():
    '''
    Gets a valid player name from user input.
    First name only, cannot be dealer.
    Function will continue asking for name until valid name is given.
    Depends on name_check() method
    '''
    while True:
        try:
            get_name = input('What is your first name? ')
            name_check(get_name)
        except:
            print("Invalid name, please try again...")
            continue
        else:
            return get_name.title()



def get_player_choice():
    '''
    Gets the players decision to either hit or stay
    Function not unit tested
    '''
    while True:
        try:
            print("Type hit to hit or stay to stay.")
            get_choice = input('What is your play choice? ')
            if get_choice.lower() in ('hit','stay'):
                pass
            else:
                raise Exception("Invalid input")
        except:
            print("Invalid input, try again...")
            continue
        else:
            return get_choice.lower()



def get_keep_playing():
    '''
    Gets input from player on whether to start round or quit game.
    Function not unit tested
    '''
    while True:
        try:
            print("Do you want to play a new round or quit?")
            get_choice = input('Type "play" to play or "quit" to quit. ')
            if get_choice.lower() in ('play','quit'):
                pass
            else:
                raise Exception("Invalid input")
        except:
            print("Invalid input, try again...")
            continue
        else:
            return get_choice.lower()


def get_player_bet(available):
    '''
    Gets input from player on how much to bet
    Can't be more than player has.
    This function is not unit tested.
    '''
    while True:
        try:
            print("How much cash do you want to bet for this round?")
            print("You can only bet what you have in cash, no decimals.")
            get_choice = input('Bet: ')
            if int(get_choice) >= 1 and int(get_choice) <= available:
                pass
            else:
                raise Exception("Invalid input")
        except:
            print("You can't bet that, please try again... ")
            continue
        else:
            return int(get_choice)
