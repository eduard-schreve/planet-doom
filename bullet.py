import pygame

pygame.init()

class bullet():
    def __init__(self):
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.imageFlip = pygame.transform.rotate(self.image, 90)

    def render(self, X, Y, screen, side):
        self.x = X
        self.y = Y
        screen.blit(self.image, (self.x, self.y))