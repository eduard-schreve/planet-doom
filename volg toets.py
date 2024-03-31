import pygame
import math
import follow

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('volg')

fps = 60
clock = pygame.time.Clock()
run = True
cx, cy = 500, 300
mpos = pygame.mouse.get_pos()
cordsX, cordsY, gradient = follow.bres(int(cx), int(cy), mpos[0], mpos[1])

speed = 1
t = 0
while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    mpos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        print(mpos)

    dx = mpos[0] - cx
    dy = mpos[1] - cy

    angle = math.atan2(dx, dy)

    mvx = math.sin(angle)
    mvy = math.cos(angle)

    cx += mvx
    cy += mvy

    if t >= len(cordsX):
        t = len(cordsX) - 1
    if gradient > 1:
        pygame.draw.circle(screen, (255, 0, 0), (cordsY[t], cordsX[t]), 50)
        for i in range(t,len(cordsX)):
            lyn = pygame.Rect(cordsY[i], cordsX[i], 1, 1)
            pygame.draw.rect(screen, (0, 255, 0), lyn)
    else:
        pygame.draw.circle(screen, (255, 0, 0), (cordsX[t], cordsY[t]), 50)
        for i in range(t,len(cordsX)):
            lyn = pygame.Rect(cordsX[i], cordsY[i], 1, 1)
            pygame.draw.rect(screen, (0, 255, 0), lyn)

    cordsX, cordsY, gradient = follow.bres(int(cx), int(cy), mpos[0], mpos[1])
    t += speed
    # px, py = cordsX[t], cordsY[t]

    pygame.display.flip()
pygame.quit()