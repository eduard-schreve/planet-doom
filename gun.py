import pygame

pygame.init()

class Gun():
    def __init__(self):
        self.image = pygame.image.load("gun.png").convert_alpha()
        self.imageFlip = pygame.transform.flip(self.image, True, False)

    def render(self, X, Y, screen, Facing):
        self.facing = Facing
        self.x = X
        self.y = Y
        if self.facing == "up":
            screen.blit(self.image, (self.x, self.y), (62, 0, 12, 35))
        elif self.facing == "down":
            screen.blit(self.image, (self.x, self.y), (52, 0, 12, 35))
        elif self.facing == "left":
            screen.blit(self.imageFlip, (self.x - 100, self.y), (24, 0, 50, 35))
        elif self.facing == "right":
            screen.blit(self.image, (self.x, self.y), (0, 0, 50, 35))