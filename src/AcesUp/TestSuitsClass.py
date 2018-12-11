##
#
##

import unittest
from Suits import Suits


class TestSuitsClass(unittest.TestCase):
    
    def test_HEART(self):
        HEART = Suits.HEART
        self.assertTrue(HEART.value == u"\u2665")

    def test_DIAMOND(self):
        DIAMOND = Suits.DIAMOND
        self.assertTrue(DIAMOND.value == u"\u2666")

    def test_SPADE(self):
        SPADE = Suits.SPADE
        self.assertTrue(SPADE.value == u"\u2660")

    def test_CLUB(self):
        CLUB = Suits.CLUB
        self.assertTrue(CLUB.value == u"\u2663")




def main():
    unittest.main()

if __name__ == '__main__':
    main()
