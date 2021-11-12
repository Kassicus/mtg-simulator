import pygame

class Card():
    def __init__(self, name, img_path):
        self.name = name
        self.img_path = img_path

        self.x = 10
        self.y = 10

        self.spotlight = False

        self.pos = (self.x, self.y)

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

        if self.x <= mouse_pos[0] <= self.x + (self.board_image.get_width()):
            if self.y <= mouse_pos[1] <= self.y + (self.board_image.get_height()):
                self.spotlight = True
            else:
                self.spotlight = False
        else:
            self.spotlight = False

    def print_name(self):
        print(self.name)