import pygame

pygame.init()

class jhon():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image_right = pygame.image.load('Jhon_side.png').convert_alpha()
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image_up = pygame.image.load('Jhon_back.png').convert_alpha()
        self.image_down = pygame.image.load('Jhon_front.png').convert_alpha()

    def render(self, X, Y, screen, image):
        self.x = X
        self.y = Y
        self.image = image
        screen.blit(self.image, (self.x, self.y))

    def qualities(self, facing):
        self.facing = facing
        if self.facing == 'right':
            return self.image_right
        if self.facing == 'left':
            return self.image_left
        if self.facing == 'up':
            return self.image_up
        if self.facing == 'down':
            return self.image_down
        