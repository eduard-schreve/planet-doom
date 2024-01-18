import pygame
import os
from save_button import sb

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screenW, screenH = info.current_w, info.current_h - 50
screen = pygame.display.set_mode((screenW, screenH), pygame.RESIZABLE)
pygame.display.set_caption("Drawing app")
screen.fill((255, 255, 255))
fps = 60
clock = pygame.time.Clock()
run = True

sb = sb()
sbX, sbY = screenW - 78, screenH - 120
isclicked = False
size = pygame.Surface((85, 23))

while run:
    clock.tick(fps)
    screen.fill((255, 255, 255))
    mpos = pygame.mouse.get_pos()
    pygame.draw.ellipse(screen, (0, 255, 0), (100, 100, 85, 23))
    surface = screen.blit(size, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if isclicked:
            pygame.image.save(surface, "ellips.png")
            print("saved")

    sb.render(screen, sbX, sbY)
    isclicked = sb.Test_clicked(sbX, sbY, event, mpos)

    pygame.draw.ellipse(screen, (0, 255, 0), (100, 100, 85, 23))

    if event.type == pygame.MOUSEBUTTONDOWN:
        print(mpos)

    pygame.display.flip()
pygame.quit()