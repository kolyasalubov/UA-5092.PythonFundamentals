# task1
from random import randint

secret_number = randint(1, 100)
attempts = 10

for i in range(1, attempts + 1):
    guess = int(input(f"Спроба {i}. Введіть число від 1 до 100: "))

    if guess == secret_number:
        print(f"Вітаю! Ви вгадали число за {i} спроб(и).")
        break
    elif guess < secret_number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
else:
    print(f"Спроби закінчилися. Загадане число: {secret_number}.")

# task2
import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode(
    (WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE
)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win_width, win_height = gameDisplay.get_size()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X - DELTA_STEP >= 0:
        COORD_X -= DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X + WIDTH_RECTANGLE + DELTA_STEP <= win_width:
        COORD_X += DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y - DELTA_STEP >= 0:
        COORD_Y -= DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y + HEIGHT_RECTANGLE + DELTA_STEP <= win_height:
        COORD_Y += DELTA_STEP

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(
        gameDisplay,
        RED_COLOR,
        [COORD_X, COORD_Y, WIDTH_RECTANGLE, HEIGHT_RECTANGLE],
    )
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()