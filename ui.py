import pygame
import math

pygame.init()

class Ui():
    def __init__(self):
        self.x = 0
        self.y = 0

    def infoTab_render(self, health, X, Y, screen):
        self.x = X
        self.y = Y
        infoTab = pygame.image.load("infoTab.png").convert_alpha()
        pygame.draw.rect(infoTab, (0, 255, 0), (10, 10, int(health), 20))
        screen.blit(infoTab, (self.x, self.y))

    def deathScreen(self, screen, X, Y):
        self.x = X
        self.y = Y
        deathScreen = pygame.image.load("deathMenu.png").convert_alpha()
        screen.blit(deathScreen, (self.x, self.y))

    def score(self, screen, cords, font, fontSize, Score):
        log = math.log10(int(Score)) if Score != 0 else 0
        text = pygame.font.Font(font, fontSize)
        scoreText = text.render("Score:" + str(Score), True, (0, 0, 0))
        screen.blit(scoreText, ((cords[0] - (log + 1) * 37) - 10, cords[1]))