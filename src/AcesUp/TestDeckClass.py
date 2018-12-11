##
#
##

import unittest
from Card import Card
from Suits import Suits
from Deck import Deck

class TestDeckClass(unittest.TestCase):

    def test_buildFullDeck(self):
        deck = Deck()
        deck.buildFullDeck()
        self.assertTrue(deck.cardsRemaining() == 52)


    def test_getCardAt(self):
        deck = Deck()
        deck.buildFullDeck()

        card = Card(Suits.HEART, 1)
        self.assertTrue(deck.getCardAt(0) == card)

        card = Card(Suits.HEART, 2)
        self.assertTrue(deck.getCardAt(1) == card)

        card = Card(Suits.DIAMOND, 1)
        self.assertTrue(deck.getCardAt(13) == card)


    def test_getFacingCard(self):
        deck = Deck()
        deck.buildFullDeck()
        card = Card(Suits.CLUB, 13)
        self.assertTrue(deck.getFacingCard() == card)


    def test_dominatesCard(self):
        deck = Deck()
        deck.buildFullDeck()
        card = Card(Suits.HEART, 5)

        self.assertFalse(deck.dominatesCard(card))

    def test_popCard(self):
        deck = Deck()
        deck.buildFullDeck()
        card = Card(Suits.CLUB, 13)
        self.assertTrue(deck.popCard() == card)

        card = Card(Suits.CLUB, 12)
        self.assertTrue(deck.popCard() == card)

        card = Card(Suits.CLUB, 11)
        self.assertTrue(deck.popCard() == card)

    
    def test_pushCard(self):
        deck = Deck()
        deck.buildFullDeck()
        card = Card(Suits.DIAMOND, 9)
        deck.popCard()
        deck.pushCard(card)
        self.assertTrue(deck.getCardAt(51) == card)

        card = Card(Suits.HEART, 3)
        deck.popCard()
        deck.pushCard(card)
        self.assertTrue(deck.getCardAt(51) == card)




def main():
    unittest.main()

if __name__ == '__main__':
    main()
