import pygame
from enemy import enemy
import bressenham
import math

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Bressenham test")
screen.fill((0, 0, 0))

run = True
fps = 60
clock = pygame.time.Clock()
enemy = enemy()

mpos = pygame.mouse.get_pos()
x, y = mpos[0], mpos[1]
lX, lY = 450, 300
t = 0
tTF = True
speed = 3
wallsrfs = pygame.Rect(0, 0, 120, 80)
enemyS = enemy.qualities()

while run:
    screen.fill((0, 0, 0))
    clock.tick(fps)
    x, y = mpos[0], mpos[1]
    cordsX, cordsY, gradient = bressenham.bres(lX, lY, x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mpos = pygame.mouse.get_pos() #get the position of the mouse if the mouse is clicked

    tTF = bressenham.testForCollide(wallsrfs, tTF, cordsX, cordsY, gradient)
    if tTF:
        t += speed
    if t >= len(cordsX):
        t = len(cordsX) - 1
        tTF = False
    else:
        tTF = True
    bressenham.moveSprite(screen, enemyS, t, lX, lY, x, y, gradient, speed)

    if event.type == pygame.MOUSEBUTTONDOWN:
        print(mpos)

    pygame.draw.rect(screen, (255, 0, 255), wallsrfs)
    pygame.display.update()
pygame.quit()