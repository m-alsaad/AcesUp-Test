##
#
##

import unittest
from Card import Card
from Suits import Suits
from Deck import Deck
from Player import Player
import copy

class TestPlayerClass(unittest.TestCase):
    
    def test_defaultOptions(self):
        p = Player("1")
        d = {'undo': True, 'confirmQuit': True}
        self.assertTrue(p.defaultOptions() == d)


    def test_get(self):
        p = Player("1")
        self.assertTrue(p.get('name') == '1')

        p = Player("a")
        self.assertTrue(p.get('name') == 'a')

        p = Player("John.Doe")
        self.assertTrue(p.get('name') == 'John.Doe')

        p = Player("John Doe")
        self.assertTrue(p.get('name') == 'John Doe')

        p = Player("John Doe$")
        self.assertTrue(p.get('name') == 'John Doe$')

        p = Player("( ͡° ͜ʖ ͡°)")
        self.assertTrue(p.get('name') == '( ͡° ͜ʖ ͡°)')

        p = Player("🤡")
        self.assertTrue(p.get('name') == '🤡')


    #I don't know what getDeep does
    def test_getDeep(self):
        p = Player("1")
        self.assertTrue(p.getDeep('name') == '1')

        p = Player("a")
        self.assertTrue(p.getDeep('name') == 'a')

        p = Player("John.Doe")
        self.assertTrue(p.getDeep('name') == 'John.Doe')

        p = Player("John Doe")
        self.assertTrue(p.getDeep('name') == 'John Doe')

        p = Player("John Doe$")
        self.assertTrue(p.getDeep('name') == 'John Doe$')

        p = Player("( ͡° ͜ʖ ͡°)")
        self.assertTrue(p.getDeep('name') == '( ͡° ͜ʖ ͡°)')

        p = Player("🤡")
        self.assertTrue(p.getDeep('name') == '🤡')
        

    def test_set(self):
        p = Player("1")

        p.set('name', "2")
        self.assertTrue(p.get('name') == '2')

        p.set('name', "John")
        self.assertTrue(p.get('name') == 'John')

        p.set('name', "$")
        self.assertTrue(p.get('name') == '$')

        p.set('name', "$")
        self.assertTrue(p.get('name') == '$')

        p.set('score', 1)
        self.assertTrue(p.get('score') == 1)

        p.set('score', 'hi')
        self.assertTrue(p.get('score') == 'hi')



    def test_addTo(self):
        p = Player("1")

        p.addTo("name", "2")
        self.assertTrue(p.get('name') == '12')

        p.addTo("name", "James")
        self.assertFalse(p.get('name') == '1James')

        p.addTo("name", "$")
        self.assertTrue(p.get('name') == '1$')

        p.addTo("name", ".")
        self.assertTrue(p.get('name') == '1.')


    #No idea how to test this one
    def test_getAllStats(self):
        pass


    #No idea what this function does
    def test_setDictProp(self):
        pass


    def test_resetStats(self):
        p = Player('1')
        p.resetStats()
        self.assertTrue(p.get('name') == '1')

        p.addTo('score', 5)
        p.resetStats()
        self.assertTrue(p.get('score') == 0)






    

def main():
    unittest.main()

if __name__ == '__main__':
    main()
