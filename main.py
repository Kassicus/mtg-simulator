import pygame
import color
import card
import board

pygame.init()

class Game():
    def __init__(self):
        self.WIDTH = 1500
        self.HEIGHT = 900
        self.TITLE = "Magic: The Gathering Simulator"

        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption(self.TITLE)
        
        self.running = True

        self.clock = pygame.time.Clock()

        self.events = pygame.event.get()

        self.test_a = card.Card("Triskaidekaphile", "cards/blue/Triskaidekaphile.png")
        self.test_b = card.Card("Shock", "cards/red/Shock.png")
        self.test_c = card.Card("Ajani, Mentor of Heroes", "cards/green-white/Ajani_Mentor_of_Heroes.png")

        self.deck = board.Deck("First Deck", [self.test_a, self.test_b, self.test_c])

        self.hand = board.Hand(self.screen)

        self.hand.draw_card(self.deck)
        self.hand.draw_card(self.deck)
        self.hand.draw_card(self.deck)

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.BACKGROUND)

    def update(self):
        self.hand.update_cards(self.events)

        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()