##
#
##

import unittest
from Card import Card
from Suits import Suits

class TestCardClass(unittest.TestCase):
    def test_cards_are_equal(self):
        card1 = Card(Suits.HEART, 2)
        card2 = Card(Suits.HEART, 2)
        self.assertTrue(card1 == card2)

        card1 = Card(Suits.HEART, 5)
        card2 = Card(Suits.HEART, 5)
        self.assertTrue(card1 == card2)

        card1 = Card(Suits.CLUB, 5)
        card2 = Card(Suits.CLUB, 5)
        self.assertTrue(card1 == card2)


    def test_cards_with_different_positions_are_not_equal(self):
        card1 = Card(Suits.HEART, 2)
        card2 = Card(Suits.HEART, 3)
        self.assertFalse(card1 == card2)


    def test_cards_with_different_suits_are_not_equal(self):
        card1 = Card(Suits.HEART, 2)
        card2 = Card(Suits.SPADE, 2)
        self.assertFalse(card1 == card2)


        card1 = Card(Suits.CLUB, 2)
        card2 = Card(Suits.SPADE, 2)
        self.assertFalse(card1 == card2)


    def test_cards_with_different_suits_and_positions_are_not_equal(self):
        card1 = Card(Suits.HEART, 2)
        card2 = Card(Suits.SPADE, 3)
        self.assertFalse(card1 == card2)


    def test_getSuit(self):
        card = Card(Suits.HEART, 1)
        self.assertTrue(card.getSuit() == u"\u2665")

        card = Card(Suits.DIAMOND, 1)
        self.assertTrue(card.getSuit() == u"\u2666")

        card = Card(Suits.SPADE, 1)
        self.assertTrue(card.getSuit() == u"\u2660")

        card = Card(Suits.CLUB, 1)
        self.assertTrue(card.getSuit() == u"\u2663")
        

    def test_getPosition(self):
        card = Card(Suits.HEART, 1)
        self.assertTrue(card.getPosition() == 1)

        card = Card(Suits.HEART, 2)
        self.assertTrue(card.getPosition() == 2)

        card = Card(Suits.HEART, 11)
        self.assertTrue(card.getPosition() == 11)

        card = Card(Suits.SPADE, 1)
        self.assertTrue(card.getPosition() == 1)



    

def main():
    unittest.main()

if __name__ == '__main__':
    main()
