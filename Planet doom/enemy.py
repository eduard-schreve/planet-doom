import pygame

pygame.init()

class enemy():
    def __init__(self):
        self.image = pygame.image.load('D:\Eduard Programmering\Planet doom/natives.png').convert_alpha()
        self.y = 0
        self.x = 0

    def render(self, X, Y, screen):
        self.y = Y
        self.x = X
        screen.blit(self.image, (self.x, self.y))
        
    def qualities(self):
        return self.image