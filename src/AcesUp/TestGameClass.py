##
#
##

import unittest
from Card import Card
from Suits import Suits
from Deck import Deck
from Player import Player
from Menu import Menu
from Game import Game

class TestGameClass(unittest.TestCase):

    def test_getPlayer(self):
        g = Game()

        self.assertFalser(g.getPlayer())
        

    

    
    
    





    

def main():
    unittest.main()

if __name__ == '__main__':
    main()
