import pygame
import math

pygame.init()

def bres(x1,y1,x2,y2):
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = 1000

    if not dx == 0:
        gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1
        xcoordinates.append(x)
        ycoordinates.append(y)

    return xcoordinates, ycoordinates, gradient

def moveSprite(screen, t, cx, cy, X, Y):
    dx = X - cx
    dy = Y - cy

    angle = math.atan2(dx, dy)

    mvx = math.sin(angle)
    mvy = math.cos(angle)

    cx += mvx
    cy += mvy

    cordsX, cordsY, gradient = bres(int(cx), int(cy), X, Y)

    if t >= len(cordsX):
        t = len(cordsX) - 1

    sX, sY = cordsX[t], cordsY[t]

    if gradient > 1:
        sY = cordsX[t]
        sX = cordsY[t]
    return sX, sY

def testForCollide(rect, tTF, cordsX, cordsY, gradient):
    if gradient > 1:
        for i in range(len(cordsX)):
            if pygame.Rect.collidepoint(rect, (cordsY[i], cordsX[i])):
                tTF = False
    else:
        for i in range(len(cordsX)):
            if pygame.Rect.collidepoint(rect, (cordsX[i], cordsY[i])):
                tTF = False
    return tTF

def qualities(screen, sprite, t, cordsX, cordsY, gradient):
    X, Y = moveSprite(screen, sprite, t, cordsX, cordsY, gradient)

    return X, Y