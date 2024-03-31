import pygame
import os
import random
from jhon import jhon
from Grond import ground
from bullet import bullet
from gun import Gun
from enemy import enemy
from imovables import wall
from ui import Ui
import follow

pygame.init()
pygame.font.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_hight = info.current_w, info.current_h - 50
screen = pygame.display.set_mode((screen_width, screen_hight), pygame.RESIZABLE) #create the screen instance
surface = pygame.Surface((screen_width, screen_hight), pygame.SRCALPHA)
font = pygame.font.Font("Radiof.ttf", 80)
screen.fill((0, 0, 0))
pygame.display.set_caption('Astronomical (1.0.0)') #set a caption for the screen

fps = 60
run = True
jhon = jhon()
ground = ground()
bullet = bullet()
Gun = Gun()
enemy = enemy()
wall = wall()
Ui = Ui()
jhonX = 100
jhonY = screen_hight - 300
quadeshDX, quadeshDY = 4, 4# how much the player moves every frame
jhon_facing = 'right'
jhon_img = jhon.qualities('right')
jhon_img_right = jhon.qualities('right')
jhon_img_left = jhon.qualities('left')
jhon_img_up = jhon.qualities('up')
jhon_img_down = jhon.qualities('down')
quadeshHealth = 200
score = 0
nativesHealthCooldown = 0
nativesDeathCooldown = 0
spawnradius = pygame.Rect(jhonX - 100, jhonY - 100, 400, 400)
quadeshRect = pygame.Rect(jhonX, jhonY, 49, 200)
hited = False
bulletHit = True
rotation = 360
bulletX = 100
bulletY = 100
bulletR = pygame.Rect(bulletX, bulletY, screen_width, 10)
nativesX, nativesY = 700, 400
nX, nY = nativesX, nativesY
nativesR = pygame.Rect(nX, nY, 58, 200)
nativesHealth = 0
enemyS = enemy.qualities()
wallX, wallY = 0, 0
wallsrfs = pygame.Rect(0, 0, 120, 80)
is_shooting = False
speed = 1
tTF = True
t = 0
clock = pygame.time.Clock()
counter = 0
mpos = pygame.mouse.get_pos()

#figure everything out for the path sprite
new_sceenH, new_sceenW = round(screen_hight, -2), round(screen_width, -2) #round of the screen height and width
if screen_hight > new_sceenH: #figure out how many spites there are going to be height wise
    number_of_spritesH = new_sceenH / 100
    number_of_spritesH = int(number_of_spritesH)
else:
    number_of_spritesH = (new_sceenH / 100) + 1
    number_of_spritesH = int(number_of_spritesH)

cordsH = [None]*number_of_spritesH #figure out the co-ordinates height wise
for i in range(number_of_spritesH):
    cordsH[i] = i*100

if screen_width > new_sceenW: #figure out how many spites there are going to be width wise
    number_of_spritesW = new_sceenW / 100
    number_of_spritesW = int(number_of_spritesW)
else:
    number_of_spritesW = (new_sceenW / 100) + 1
    number_of_spritesW = int(number_of_spritesW)

cordsW = [None]*number_of_spritesW #figure out the co-ordinates width wise
for i in range(number_of_spritesW):
    cordsW[i] = i*100

while run: #main game loop
    if counter < fps:
        counter += 1
    elif counter == fps:
        counter = 0
    cordsX, cordsY, gradient = follow.bres(nativesX, nativesY, jhonX, jhonY)
    gunX = jhonX + 48
    gunY = jhonY + 114
    clock.tick(fps)
    surface.fill((0, 0, 0, 0))
    screen.fill((0, 0, 0)) #fill the screen with a coulor
    spawnradius = pygame.Rect(jhonX - 100, jhonY - 100, 400, 400)

    for event in pygame.event.get(): #check if the user has hit the exit button
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: #check for keypresses
            if event.key == pygame.K_SPACE: #check for the space key
                is_shooting = True
                bulletX = gunX
                bulletY = gunY
                if nativesHealth == 5:
                    score += 3

    # #create the background
    for y in range(number_of_spritesH):
            for x in range(number_of_spritesW):
                ground.render(cordsW[x], cordsH[y], screen)
                
    #render die sprites
    pygame.draw.rect(surface, (255, 0, 0, 100), spawnradius)
    jhon.render(jhonX, jhonY, screen, jhon_img)
    Gun.render(gunX, gunY, screen, jhon_facing)
    Ui.infoTab_render(quadeshHealth, 0, 0, screen)
    Ui.score(screen, (screen_width-255, 0), "Radiof.ttf", 70, score)

    if nativesHealth == 0:
        nativesX, nativesY = random.randint(0, screen_width), random.randint(0, screen_hight)
        if spawnradius.collidepoint(nativesX, nativesY):
            nativesHealth = 0
        else:
            nativesHealth = 20

    # check for collision in x direction
    if nativesR.colliderect(jhonX + quadeshDX, jhonY, 49, 200) == False:
        nX, nY = follow.moveSprite(screen, t, nativesX, nativesY, jhonX, jhonY)
    if nativesR.colliderect(jhonX - quadeshDX, jhonY, 49, 200) == False:
        nX, nY = follow.moveSprite(screen, t, nativesX, nativesY, jhonX, jhonY)
    # check for collision in y direction
    if nativesR.colliderect(jhonX, jhonY + quadeshDY, 49, 200) == False:
        nX, nY = follow.moveSprite(screen, t, nativesX, nativesY, jhonX, jhonY)
    if nativesR.colliderect(jhonX, jhonY - quadeshDY, 49, 200) == False:
        nX, nY = follow.moveSprite(screen, t, nativesX, nativesY, jhonX, jhonY)

    # enemy spawning code
    if nativesHealth > 0:# check that the enemy is not dead
        enemy.render(nX, nY, screen)
        nativesR = pygame.Rect(nX, nY, 58, 200)
        if pygame.Rect.colliderect(quadeshRect, nativesR):
            hited = True
        if hited and counter == fps and  quadeshHealth > 0:
            quadeshHealth -= 10
            hited = False
            pygame.draw.rect(surface, (255, 0, 0, 100), quadeshRect)
        if quadeshHealth == 0:
            deathAnim = jhon.deathScreen(surface, screen_hight, screen_width)
            if deathAnim:
                Ui.deathScreen(surface, 368, 329)
    
    # check if the respawn button is clicked
    respawnRect = pygame.Rect(368, 384, 315, 110)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.Rect.collidepoint(respawnRect, mpos):
            quadeshHealth = 200

    quadeshRect = pygame.Rect(jhonX, jhonY, 49, 200)
    
    # make the enemy('s) follow the sprite
    if tTF:
        t += speed
    if t >= len(cordsX):
        t = len(cordsX) - 1
        tTF = False
    else:
        tTF = True
    tTF = follow.testForCollide(wallsrfs, tTF, cordsX, cordsY, gradient)

    # make the gun shoot in all cardinal directions
    if quadeshHealth > 0:
        if is_shooting:
            bullet.render(bulletX, bulletY, screen, jhon_facing)
            if jhon_facing == "up":
                bulletY += 100
                bulletR = pygame.Rect(bulletX, 0, 10, bulletY)
            elif jhon_facing == "down":
                bulletY -= 100
                bulletR = pygame.Rect(bulletX, bulletY, 10, screen_hight)
            elif jhon_facing == "left":
                bulletX -= 100
                bulletR = pygame.Rect(0, bulletY, bulletX, 10)
            elif jhon_facing == "right":
                bulletX += 100
                bulletR = pygame.Rect(bulletX, bulletY, screen_width, 10)
            if nativesHealth > 0:
                nativesHealth = enemy.takeDamage(surface, nativesHealth, nativesR, bulletR)

    if bulletX >= screen_width - 50:
        is_shooting = False
        bulletX = 100

    # make the player move
    if quadeshHealth > 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and nativesR.colliderect(jhonX - quadeshDX, jhonY + 1, 1, 198) == False: #check for the left key
                jhonX -= quadeshDX
                if jhon_facing != 'left':
                    jhon_img = jhon_img_left
                    jhon_facing = 'left'

            if event.key == pygame.K_RIGHT and nativesR.colliderect(jhonX + quadeshDX, jhonY - 1, 1, 198) == False: #check for the right key
                jhonX += quadeshDX
                if jhon_facing != 'right':
                    jhon_img = jhon_img_right
                    jhon_facing = 'right'
            
            if event.key == pygame.K_UP and nativesR.colliderect(jhonX + 1, jhonY - quadeshDY, 47, 1) == False: #check for the up key
                jhonY -= quadeshDY
                if jhon_facing != 'down':
                    jhon_img = jhon_img_up
                    jhon_facing = 'down'

            if event.key == pygame.K_DOWN and nativesR.colliderect(jhonX - 1, jhonY + quadeshDY, 47, 1) == False: #check for the down key
                jhonY += quadeshDY
                if jhon_facing != 'up':
                    jhon_img = jhon_img_down
                    jhon_facing = 'up'

    mpos = pygame.mouse.get_pos() #get the position of the mouse if the mouse is clicked !!!for debugging prposes only!!!
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(mpos)

    screen.blit(surface, (0, 0))
    pygame.display.flip() #update the screen
pygame.quit() #exit the game
pygame.font.quit()