import pygame
import random

class Card():
    def __init__(self, name, img_path):
        self.name = name
        self.img_path = img_path

        self.x = random.randint(0, 1200)
        self.y = random.randint(0, 600)

        self.spotlight = False

        self.pos = (self.x, self.y)

        self.dragging = False

        self.mouse_offset_x = 0
        self.mouse_offset_y = 0

        self.raw_image = pygame.image.load(self.img_path)
        self.raw_width = self.raw_image.get_width()
        self.raw_height = self.raw_image.get_height()

        self.board_image = pygame.transform.scale(self.raw_image, (int(self.raw_width / 2), int(self.raw_height / 2)))

    def draw(self, surface):
        surface.blit(self.board_image, self.pos)

        if self.spotlight:
            surface.blit(self.raw_image, (1235, 0))

    def update(self, events):
        self.pos = (self.x, self.y)

        mouse_pos = pygame.mouse.get_pos()

        if self.dragging:
            self.x = 5 * round((mouse_pos[0] - (self.board_image.get_width() / 2)) / 5)
            self.y = 5 * round((mouse_pos[1] - (self.board_image.get_height() / 2)) / 5)

            self.pos = (self.x, self.y)

        if self.x <= mouse_pos[0] <= self.x + (self.board_image.get_width()):
            if self.y <= mouse_pos[1] <= self.y + (self.board_image.get_height()):
                self.spotlight = True
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.dragging = True
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.dragging = False
            else:
                self.spotlight = False
        else:
            self.spotlight = False

    def print_name(self):
        print(self.name)

    def top_of_deck(self, deck):
        deck.cards.insert(0, self)

    def bottom_of_deck(self, deck):
        deck.cards.append(self)