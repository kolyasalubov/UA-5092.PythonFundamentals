import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=20

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    displayRect = gameDisplay.get_rect()
    
    if keys[pygame.K_LEFT]:
        COORD_X = max(COORD_X - DELTA_STEP, displayRect.left)
    if keys[pygame.K_RIGHT]:
        COORD_X = min(COORD_X + DELTA_STEP, displayRect.right - WIDTH_RECTANGLE)
    if keys[pygame.K_UP]:
        COORD_Y = max(COORD_Y - DELTA_STEP, displayRect.top)
    if keys[pygame.K_DOWN]:
        COORD_Y = min(COORD_Y + DELTA_STEP, displayRect.bottom - HEIGHT_RECTANGLE)


    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X, 
                                              COORD_Y, 
                                              WIDTH_RECTANGLE, 
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    

