import pygame
import color
import card

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

        self.test = card.Card("Triskaidekaphile", "cards/blue/Triskaidekaphile.png")

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

        self.test.draw(self.screen)

    def update(self):
        self.test.update(self.events)

        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()