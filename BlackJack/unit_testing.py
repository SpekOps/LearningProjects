'''
Unit Testing
'''
import os
import unittest
import Blackjack_Objects

os.system("cls")

class Test_Blackjack_Objects(unittest.TestCase):
    '''
    Test the Blackjack_Objects objects and functions.
    '''


    def test_card_creation(self):
        '''
        Test card creation and card values
        '''
        testobject = Blackjack_Objects.Card('Spades','Two')
        card_name = testobject.name
        card_value = testobject.value
        self.assertEqual(card_name,'Two of Spades')
        self.assertEqual(card_value,2)


    def test_deck_creation(self):
        '''
        Test deck creation, 2nd card, count count
        '''
        testobject = Blackjack_Objects.Deck(1)
        card_count = len(testobject.deck)
        card_type_check = type(testobject.deck[0])
        self.assertEqual(card_count,52)
        self.assertEqual(card_type_check,Blackjack_Objects.Card)
        testobject.shuffle_deck()
        card_after_shuffle = testobject.deck[0].name
        self.assertNotEqual(card_after_shuffle,'Two of Spades')


    def test_deck_movement(self):
        '''
        Tests adding and removing a card from a deck
        '''
        testdeck = Blackjack_Objects.Deck()

        # test initial zero size deck
        start_cards = len(testdeck.deck)
        self.assertEqual(start_cards,0)

        # test deck after adding two cards
        card1 = Blackjack_Objects.Card('Spades','Three')
        card2 = Blackjack_Objects.Card('Hearts','Four')
        testdeck.add_card(card1)
        testdeck.add_card(card2)
        card_count = len(testdeck.deck)
        self.assertEqual(card_count,2)

        # test deck after removing a card
        # verifies top card removed
        testdeck.draw_card()
        card_count = len(testdeck.deck)
        remaining_card = testdeck.deck[-1].name
        self.assertEqual(card_count,1)
        self.assertEqual(remaining_card,'Three of Spades')


    def test_deck_value(self):
        '''
        Tests calculating deck values per Blackjack rules
        '''
        testdeck = Blackjack_Objects.Deck()
        deck_value_start = testdeck.get_deck_value()
        card1 = Blackjack_Objects.Card('Spades','Three')
        card2 = Blackjack_Objects.Card('Hearts','Four')
        card3 = Blackjack_Objects.Card('Clubs','King')
        testdeck.add_card(card1)
        testdeck.add_card(card2)
        testdeck.add_card(card3)
        deck_value_final = testdeck.get_deck_value()
        self.assertEqual(deck_value_start,0)
        self.assertEqual(deck_value_final,17)       


    def test_player(self):
        '''
        Tests player creation and player deck
        '''        

        # create cards and player
        player = Blackjack_Objects.Player()
        card1 = Blackjack_Objects.Card('Spades','Three')
        card2 = Blackjack_Objects.Card('Hearts','Four')
        card3 = Blackjack_Objects.Card('Clubs','King')

        # give player cards, set status
        player.deck.add_card(card1)
        player.deck.add_card(card2)
        player.deck.add_card(card3)
        player_deck_value = player.deck.get_deck_value()
        player.status = 'won'

        # test
        self.assertEqual(player_deck_value,17)
        self.assertEqual(player.status,'won')   

        
    def test_dealer_logic(self):
        '''
        Tests dealer decisions to hit or stay
        '''
        dealer = Blackjack_Objects.Dealer()
        dealer.dealer_play(25,22)
        test1 = dealer.status
        dealer.dealer_play(25,0)
        test2 = dealer.status
        dealer.dealer_play(15,16)
        test3 = dealer.status
        dealer.dealer_play(15,15)
        test4 = dealer.status
        dealer.dealer_play(21,20)
        test5 = dealer.status
        dealer.dealer_play(16,7)
        test6 = dealer.status
        dealer.dealer_play(22,21)        
        test7 = dealer.status
        self.assertEqual(test1,'stay')
        self.assertEqual(test2,'stay')
        self.assertEqual(test3,'stay')
        self.assertEqual(test4,'stay')
        self.assertEqual(test5,'hit')
        self.assertEqual(test6,'hit')
        self.assertEqual(test7,'stay')


    def test_name_check(self):
        '''
        Tests player name function
        Verifies it can correct input or error out
        '''
        test1 = 'john smith'
        return1 = Blackjack_Objects.name_check(test1)
        self.assertEqual(return1,'John')


if __name__ == '__main__':
    unittest.main()




# d = Blackjack_Objects.Deck(1)

# d.shuffle_deck()

# print(d.deck[0])

# print(len(d))

# drawn_card = d.draw_card()

# print(drawn_card)

# print(len(d))


# counter = 0
# for i in d.deck: 
    # if counter >= 5:
        # break
    # else:
        # print(i)
        # counter += 1
        
# print(d)


