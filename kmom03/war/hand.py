#!/usr/bin/env python3
"""
Represents a player
"""
class Hand():
    """
    Hand class
    """

    def __init__(self, name, cards):
        """
        Inits a hand object
        """
        self.name = name
        self.cards = cards
        self.score = 0
