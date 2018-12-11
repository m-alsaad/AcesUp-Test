##
#
##

import unittest
from Card import Card
from Suits import Suits
from Deck import Deck
from Player import Player
from Menu import Menu

class TestMenuClass(unittest.TestCase):

    def test_setCurrentMenu(self):
        m = Menu()
        m.setCurrentMenu(m)
        self.assertTrue(m.getCurrentMenu() == m)

    def test_printMenu(self):
        pass

    def test_getInput(self):
        pass

    def test_hasMenu(self):
        m = Menu()
        m.setCurrentMenu(m)

        self.assertTrue(m.hasMenu())

    def test_getFormattedTableObj(self):
        m = Menu()
        m.setCurrentMenu(m)
        d = {'table': 'Data', 'colWidth': 1}
        self.assertTrue(m.getFormattedTableObj('Data', 1) == d)

        d = {'table': 1, 'colWidth': 'Data'}
        self.assertTrue(m.getFormattedTableObj(1, 'Data') == d)

        d = {'table': '$', 'colWidth': 1.1}
        self.assertTrue(m.getFormattedTableObj('$', 1.1) == d)


    def test_gameMenu(self):
        pass

        

    

    
    
    





    

def main():
    unittest.main()

if __name__ == '__main__':
    main()
