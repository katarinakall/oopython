#!/usr/bin/env python3
"""
A deck class conisting of 52 cards.
"""
from card import Card
from random import shuffle

class Deck():
    """
    Deck class
    """

    def __init__(self):
        """Inits deck object"""
        self.cards = []
        self.create_cards()

    def create_cards(self):
        """Creates a deck of cards"""
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Knight', 'Queen', 'King', 'Ace']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle_deck(self):
        """Shuffles deck of cards"""
        shuffle(self.cards)
        return self.cards