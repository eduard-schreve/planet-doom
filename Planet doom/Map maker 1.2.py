import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Map maker version: 1.2")
fps = 60
clock = pygame.time.Clock()
run = True

# different types of terrain:
ocean = (0, 0, 255)
shallowOcean = (0, 255, 255)
beach = (246, 215, 176)
grass = (50, 255, 50)
hill = (0, 100, 0)

# the different types of details
tree = (150, 75, 0)
rock = (170, 170, 170)
bush = (0, 200, 0)

noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)
xpix, ypix = 50, 50
pic = []
wnCol = []
xVal = 0
yVal = 0
wnY, wnX = 0, 0
height = 0

for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125 * noise4([i/xpix, j/ypix])

        row.append(noise_val)
    pic.append(row)

for i in range(xpix):
    wnRow = []
    for j in range(ypix):
        wnNoiseVal = random.randint(0, 100)
        wnRow.append(wnNoiseVal)
    wnCol.append(wnRow)

plt.imshow(pic, "grey")
plt.show()
plt.imshow(wnCol, "grey")
plt.show()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(50):
        wnY, yVal = i*10, i*10
        for e in range(50):
            wnX, xVal = e*10, e*10
            height = (pic[i])[e]
            details = (wnCol[i])[e]
            # check the height for all the terrain
            if height <= -0.3:
                pygame.draw.rect(screen, ocean, (xVal, yVal, 10, 10))
            if height <= -0.05 and height >= -0.3:
                pygame.draw.rect(screen, shallowOcean, (xVal, yVal, 10, 10))
            if height <= 0.03 and height >= -0.05:
                pygame.draw.rect(screen, beach, (xVal, yVal, 10, 10))
            if height <= 0.3 and height >= 0.03:
                pygame.draw.rect(screen, grass, (xVal, yVal, 10, 10))
            if height <= 0.75 and height >= 0.3:
                pygame.draw.rect(screen, hill, (xVal, yVal, 10, 10))
            
            # check the chance of spawning in a speciffic detail
            # for trees
            if details <= 10 and height >= 0.03:
                pygame.draw.rect(screen, tree, (wnX + 3, wnY, 4, 10))
            # for bushes
            if details <= 60 and details >= 50 and height >= 0.03:
                pygame.draw.circle(screen, bush, (wnX + 5, wnY + 5), 5)
            # for rocks
            if details >= 97 and height >= -0.05:
                pygame.draw.circle(screen, rock, (wnX + 5, wnY + 5), 5)

    pygame.display.update()
pygame.quit()