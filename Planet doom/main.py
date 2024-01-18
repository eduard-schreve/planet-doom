import pygame
import os
from jhon import jhon
from Grond import ground
from bullet import bullet
from gun import Gun
from enemy import enemy
from imovables import wall
import bressenham

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_hight = info.current_w, info.current_h - 50
screen = pygame.display.set_mode((screen_width, screen_hight), pygame.RESIZABLE) #create the screen instance
surface = pygame.Surface((screen_width, screen_hight), pygame.SRCALPHA)
screen.fill((0, 0, 0))
pygame.display.set_caption('Vici legends') #set a caption for the screen

fps = 60
run = True
jhon = jhon()
ground = ground()
bullet = bullet()
Gun = Gun()
enemy = enemy()
wall = wall()
jhon_x_pos = 100
jhon_y_pos = screen_hight - 300
jhon_facing = 'right'
jhon_img = jhon.qualities('right')
jhon_img_right = jhon.qualities('right')
jhon_img_left = jhon.qualities('left')
jhon_img_up = jhon.qualities('up')
jhon_img_down = jhon.qualities('down')
bulletX = 100
bulletY = 100
nativesX, nativesY = 700, 400
nX, nY = nativesX, nativesY
enemyS = enemy.qualities()
wallX, wallY = 0, 0
wallsrfs = pygame.Rect(0, 0, 120, 80)
is_shooting = False
speed = 1
tTF = True
t = 0
clock = pygame.time.Clock()

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
    cordsX, cordsY, gradient = bressenham.bres(nativesX, nativesY, jhon_x_pos, jhon_y_pos)
    gunX = jhon_x_pos + 48
    gunY = jhon_y_pos + 114
    clock.tick(fps)
    surface.fill((0, 0, 0, 0))
    screen.fill((0, 0, 0)) #fill the screen with a coulor
    
    for event in pygame.event.get(): #check if the user has hit the exit button
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: #check for keypresses
            if event.key == pygame.K_SPACE: #check for the space key
                is_shooting = True
                bulletX = gunX + 48
                bulletY = gunY + 14

    # #create the background
    for y in range(number_of_spritesH):
            for x in range(number_of_spritesW):
                ground.render(cordsW[x], cordsH[y], screen)
                
    #render die sprites
    jhon.render(jhon_x_pos, jhon_y_pos, screen, jhon_img)
    Gun.render(gunX, gunY, screen)
    wall.render(0, 0, screen)
    enemy.render(nX, nY, screen)
    pygame.draw.line(surface, (0, 0, 0, 0), (bulletX, bulletY), (screen_width, bulletY), 1)
    bulletR = pygame.Rect(bulletX, bulletY, screen_width, 10)
    nativesR = pygame.Rect(nX, nY, 58, 200)

    
    if tTF:
        t += speed
    if t >= len(cordsX):
        t = len(cordsX) - 1
        tTF = False
    else:
        tTF = True

    tTF = bressenham.testForCollide(wallsrfs, tTF, cordsX, cordsY, gradient)
    nX, nY = bressenham.moveSprite(screen, t, nativesX, nativesY, jhon_x_pos, jhon_y_pos, gradient, speed)

    if is_shooting:
        bullet.render(bulletX, bulletY, screen)
        bulletX += 100
        if pygame.Rect.colliderect(bulletR, nativesR):
            pygame.draw.rect(surface, (255, 0, 0, 100), nativesR)

    if bulletX >= screen_width - 50:
        is_shooting = False
        bulletX = 100

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT: #check for the left key
            jhon_x_pos -= 4
            if jhon_facing != 'left':
                jhon_img = jhon_img_left
                jhon_facing = 'left'

        if event.key == pygame.K_RIGHT: #check for the right key
            jhon_x_pos += 4
            if jhon_facing != 'right':
                jhon_img = jhon_img_right
                jhon_facing = 'right'
        
        if event.key == pygame.K_UP: #check for the up key
            jhon_y_pos -= 4
            if jhon_facing != 'down':
                jhon_img = jhon_img_up
                jhon_facing = 'down'

        if event.key == pygame.K_DOWN: #check for the down key
            jhon_y_pos += 4
            if jhon_facing != 'up':
                jhon_img = jhon_img_down
                jhon_facing = 'up'

    mpos = pygame.mouse.get_pos() #get the position of the mouse if the mouse is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(mpos)

    screen.blit(surface, (0, 0))
    pygame.display.flip() #update the screen
pygame.quit() #exit the game