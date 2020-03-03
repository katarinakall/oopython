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

    def get_value(self):
        """
        Returns the value of a card.
        """
        if self._value == 'Knight':
            return 11
        elif self._value == 'Queen':
            return 12
        elif self._value == 'King':
            return 13
        elif self._value == 'Ace':
            return 14
        else: 
            return self._value 

    def get_suit(self):
        """
        Returns the suit of a card
        """
        return self._suit

    def __repr__(self):
        """
        Returns the suit and value of a card.
        """
        return "{v} of {s}".format(v=self._value, s=self._suit)