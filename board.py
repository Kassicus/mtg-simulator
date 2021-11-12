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
    def __init__(self, surface):
        self.cards = []
        self.draw_y = 650
        self.draw_x = 10
        self.x_step = 140

        self.render_surface = surface

        self.old_card_len = len(self.cards)

        self.render_cards()

    def render_cards(self):
        for card in self.cards:
            card.x = self.draw_x
            card.y = self.draw_y
            self.draw_x += self.x_step

    def update_cards(self, events):
        """if len(self.cards) != self.old_card_len:
            self.render_cards()

        self.old_card_len = len(self.cards)"""

        for card in self.cards:
            card.update(events)
            card.draw(self.render_surface)

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