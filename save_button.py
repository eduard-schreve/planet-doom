import pygame

pygame.init()

class sb():
    def __init__(self):
        self.image = pygame.image.load("save_button.png").convert_alpha()
        self.x = 0
        self.y = 0

    def render(self, screen, X, Y):
        self.x = X
        self.y = Y
        screen.blit(self.image, (self.x, self.y))

    def Test_clicked(self, X, Y, event, mpos):
        self.x, self.y = X, Y
        ifclicked = False
        rect = pygame.Rect(self.x, self.y, 78, 20)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect.collidepoint(rect, mpos[0], mpos[1]):
                ifclicked = True
            else:
                ifclicked = False
        return ifclicked