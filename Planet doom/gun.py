import pygame

pygame.init()

class Gun():
    def __init__(self):
        self.image = pygame.image.load("gun.png").convert_alpha()

    def render(self, X, Y, screen):
        self.x = X
        self.y = Y
        screen.blit(self.image, (self.x, self.y))