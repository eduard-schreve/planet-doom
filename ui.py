import pygame

pygame.init()

class Ui():
    def __init__(self):
        self.x = 0
        self.y = 0

    def infoTab_render(self, preHealth, health, X, Y, screen):
        self.x = X
        self.y = Y
        infoTab = pygame.image.load("infoTab.png").convert_alpha()
        Health = pygame.image.load("health.png").convert_alpha()
        screen.blit(infoTab, (self.x, self.y))
        for i in range(int(health)):
            screen.blit(Health, (i * 40 + self.x, self.y), (80, 0, 40, 40))
            if health - int(health) == 0.5:
                screen.blit(Health, (i * 40 + 40 + self.x, self.y), (40, 0, 40, 40))
        for c in range(int(preHealth - health)):
            screen.blit(Health, (preHealth * 40 + self.x - 40 * (c + 1), self.y), (0, 0, 40, 40))