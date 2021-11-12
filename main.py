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

        self.deck = board.Deck("First Deck", [self.test_a, self.test_b])

        self.hand = board.Hand()
        #self.hand.print_hand()
        self.hand.draw_card(self.deck)
        self.hand.draw_card(self.deck)
        self.hand.print_hand()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.BLACK)

        self.test_b.draw(self.screen)

    def update(self):
        self.test_b.update(self.events)

        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()