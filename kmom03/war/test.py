#!/usr/bin/env python3
"""
Module for unittests
"""

import unittest
from deck import Deck
from war import War

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
        self.deck.shuffle_deck()
        first_card_after_shuffle = self.deck.cards[0]
        self.assertNotEqual(first_card, first_card_after_shuffle)


class TestWar(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """
        self.war = War()

    def tearDown(self):
        """ Remove dependencies after test """
        self.war = None

    def test_generate_players(self):
        """Test if function generate players work"""
        self.assertEqual(len(self.war.players), 2)

    def test_draw_cards(self):
        """Test if function draw cards works"""
        self.war.draw_cards()
        self.assertEqual(len(self.war.players[0].cards), 25)

    def test_append_cards(self):
        """Test function append cards"""
        self.war.draw_cards()
        self.war.append_cards(0)
        self.assertEqual(len(self.war.players[0].cards), 27)



if __name__ == '__main__':
    unittest.main(verbosity=3)