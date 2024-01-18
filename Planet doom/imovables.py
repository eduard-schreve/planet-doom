import pygame 

pygame.init()

class wall():
    def __init__(self):
        self.image = pygame.image.load("Muur.png").convert_alpha()
        self.x = 0
        self.y = 0

    def render(self, X, Y, screen):
        self.x = X
        self.y = Y
        screen.blit(self.image, (self.x, self.y))