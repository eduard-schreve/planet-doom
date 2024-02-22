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
        self.blackness = 0

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

    def deathScreen(self, screen, screenW, screenH):
        done = False
        pygame.draw.rect(screen, (0, 0, 0, self.blackness), (0, 0, screenH, screenW))
        if self.blackness < 255:
            self.blackness += 5
        if self.blackness == 255:
            done = True
        return done