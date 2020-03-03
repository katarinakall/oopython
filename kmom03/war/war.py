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
        self.card_stack = []


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
        while self.players[0].cards and self.players[1].cards:
            input("Press any key to continue...")
            cards = self.draw_cards()
            self.compare_value(cards)
        if len(self.players[0].cards) > len(self.players[0].cards):
            print("Congratulations you won!")
        else:
            print("Unfortunately you did not win. Better luck next time.")
        

        
    def draw_cards(self):
        """
        Draws a card from each player
        """
        card_player1 = self.players[0].cards.pop(0)
        card_player2 = self.players[1].cards.pop(0)
        print("{n} draws {c}".format(n=self.players[0].name, c=card_player1))
        print("{n} draws {c}".format(n=self.players[1].name, c=card_player2))
        self.card_stack.append(card_player1)
        self.card_stack.append(card_player2)
        return (card_player1, card_player2)
    

    def compare_value(self, cards):
        """
        Compares two cards values
        """
        if cards[0].get_suit() == cards[1].get_suit():
            if cards[0].get_value() > cards[1].get_value():
                print("{n} wins the round and picks up all cards.".format(n=self.players[0].name))
                self.append_cards(0)
            else:
                print("{n} wins the round and picks up all cards.".format(n=self.players[1].name))
                self.append_cards(1)
            self.print_score()

    def append_cards(self, player):
        """
        Appends stack of cards from round to players stack of cards.
        """
        for card in self.card_stack:
            self.players[player].cards.append(card)
            self.card_stack = []


    def print_score(self):
        """
        Prints the current score.
        """
        print("Status:\n{p1}: {s1} cards\n{p2}: {s2} cards"\
            .format(p1=self.players[0].name, s1=len(self.players[0].cards),\
                p2=self.players[1].name, s2=len(self.players[1].cards)))



if __name__ == "__main__": 
    War().play_game()

