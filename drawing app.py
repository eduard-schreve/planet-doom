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
clicking_type = 0
drawing = pygame.Surface((1120, 680), pygame.SRCALPHA)
which_point = None

while run:
    clock.tick(fps)
    screen.fill((20, 20, 20))
    drawing.fill((0, 0, 0, 0))
    mpos = pygame.mouse.get_pos()
    pygame.draw.ellipse(drawing, (0, 255, 0), (0, 0, 85, 23))
    # pygame.draw.rect(screen, (255, 255, 255), (10, 10, 1120, 680))
    
    def line(sX, sY, eX, eY, surface, thickness, coulor):
        pygame.draw.line(surface, coulor, (sX, sY), (eX, eY), thickness)
        pygame.draw.rect(surface, (0, 0, 0), (sX, sY, thickness, thickness))
        pygame.draw.rect(surface, (0, 0, 0), (eX, eY, thickness, thickness))
        p1 = pygame.draw.circle(surface, coulor, (sX, sY), round(thickness/2))
        p2 = pygame.draw.circle(surface, coulor, (eX, eY), round(thickness/2))
        # pygame.draw.rect(surface, (0, 0, 0), p1)
        # pygame.draw.rect(surface, (0, 0, 0), p2)
        return p1, p2

    Points = line(500, 500, 250, 600, drawing, 20, (244, 146, 35))
    # pygame.draw.rect(drawing, (0, 0, 0), (Points[0]))
    # pygame.draw.rect(drawing, (0, 0, 0), (Points[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if isclicked:
            pygame.image.save(drawing, "ellips.png")
            print("saved")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(mpos, "left click")
                for p in range(len(Points)):
                    print(Points[p])
                    if Points[p].collidepoint(mpos):
                        print("you have selected me")
                        which_point = p
            if event.button == 3:
                print(mpos, "right click")

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                which_point = None

        if event.type == pygame.MOUSEMOTION:
            if which_point != None:
                Points[which_point].move_ip(event.rel)

    sb.render(screen, sbX, sbY)
    isclicked = sb.Test_clicked(sbX, sbY, event, mpos)

    screen.blit(drawing, (10, 10))

    pygame.display.flip()
pygame.quit()