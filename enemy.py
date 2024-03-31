import pygame

pygame.init()

class enemy():
    def __init__(self):
        self.image = pygame.image.load('natives.png').convert_alpha()
        self.y = 0
        self.x = 0

    def render(self, X, Y, screen):
        self.y = Y
        self.x = X
        screen.blit(self.image, (self.x, self.y))
        
    def qualities(self):
        return self.image
    
    def takeDamage(self, screen, health, eRect, bRect):
        if pygame.Rect.colliderect(eRect, bRect):
            health -= 5
            pygame.draw.rect(screen, (255, 0, 0, 100), eRect)

        return health