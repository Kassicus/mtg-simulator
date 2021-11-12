import pygame

class Deck():
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def remove_top_card(self):
        self.cards.remove(self.cards[0])

class Battlefield():
    def __init__(self):
        pass

class Hand():
    def __init__(self):
        self.cards = []

    def draw_card(self, deck):
        self.cards.append(deck.cards[0])
        deck.remove_top_card()

    def draw_hand(self, deck):
        for x in range(7):
            self.draw_card(deck)

    def print_hand(self):
        for card in self.cards:
            card.print_name()

class Graveyard():
    def __init__(self):
        pass

class Exile():
    def __init__(self):
        pass