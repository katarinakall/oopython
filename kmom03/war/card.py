#!/usr/bin/env python3
"""
A single playing card having suit and value.
"""
class Card():
    """
    Playing card class
    """
    def __init__(self, suit, value):
        """
        Inits card object
        """
        self._suit = suit
        self._value = value

    def __repr__(self):
        """
        Returns the suit and value of a card.
        """
        return "{v} of {s}".format(v=self._value, s=self._suit)
