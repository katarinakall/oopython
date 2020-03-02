#!/usr/bin/env python3
"""
Module for game functionallity.
"""
from deck import Deck
from hand import Hand

class War():
    """
    Game class
    """

    def __init__(self):
        """
        Inits game object
        """
        self.players = []
        self.generate_players()


    def generate_players(self):
        """
        Creates two players
        """
        deck = Deck()
        deck.shuffle_deck()
        half_deck = len(deck.cards)//2
        player_1 = Hand('You', deck.cards[:half_deck])
        player_2 = Hand('Opponent', deck.cards[half_deck:])
        self.players.append(player_1)
        self.players.append(player_2)

    def play_game(self):
        """
        Game
        """
while True:
       





if __name__ == "__main__": 
    War()

