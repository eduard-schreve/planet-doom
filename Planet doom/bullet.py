import pygame

pygame.init()

class bullet():
    def __init__(self):
        self.image = pygame.image.load('D:\Eduard Programmering\Planet doom/bullet.png').convert_alpha()

    def render(self, X, Y, screen):
        self.x = X
        self.y = Y
        screen.blit(self.image, (self.x, self.y))