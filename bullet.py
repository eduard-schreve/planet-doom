import pygame

pygame.init()

class bullet():
    def __init__(self):
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.imageFlip = pygame.transform.rotate(self.image, 90)

    def render(self, X, Y, screen, facing):
        self.x = X
        self.y = Y
        self.facing = facing
        if self.facing == "up":
            screen.blit(self.imageFlip, (self.x + 6, self.y + 35))
        elif self.facing == "down":
            screen.blit(self.imageFlip, (self.x + 6, self.y - 35))
        elif self.facing == "left":
            screen.blit(self.image, (self.x - 150, self.y + 17))
        elif self.facing == "right":
            screen.blit(self.image, (self.x + 50, self.y + 17))