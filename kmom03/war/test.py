#!/usr/bin/env python3
"""
Module for unittests
"""

import unittest
from deck import Deck

class TestDeck(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """
        self.deck = Deck()

    def tearDown(self):
        """ Remove dependencies after test """
        self.deck = None

    def test_deck_length(self):
        """Test if deck consists of 52 cards"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_shuffle_deck(self):
        """Test if shuffle method works"""
        first_card = self.deck.cards[0]
        self.deck.shuffle()
        first_card_after_shuffle = self.deck.cards[0]
        self.assertNotEqual(first_card, first_card_after_shuffle)


if __name__ == '__main__':
    unittest.main(verbosity=3)
