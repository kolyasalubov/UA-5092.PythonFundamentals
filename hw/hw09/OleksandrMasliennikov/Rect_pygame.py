"""Move a red rectangle around the window with the arrow keys."""

import pygame


class Config:
    """Game settings collected in one place."""

    FPS = 60
    WINDOW_SIZE = (500, 500)
    CAPTION = 'My first game'

    RECT_START = (50, 50)
    RECT_SIZE = (40, 60)
    STEP = 5

    BACKGROUND_COLOR = (0, 0, 0)
    RECT_COLOR = (250, 0, 0)


def move_rect(rect: pygame.Rect,
              keys: pygame.key.ScancodeWrapper,
              bounds: pygame.Rect) -> None:
    """Move the rectangle by pressed arrow keys and keep it inside bounds."""
    if keys[pygame.K_LEFT]:
        rect.x -= Config.STEP
    if keys[pygame.K_RIGHT]:
        rect.x += Config.STEP
    if keys[pygame.K_UP]:
        rect.y -= Config.STEP
    if keys[pygame.K_DOWN]:
        rect.y += Config.STEP
    rect.clamp_ip(bounds)


def main() -> None:
    """Initialize pygame and run the game loop until the window is closed."""
    _, failed = pygame.init()
    if failed:
        print(f'Warning: {failed} pygame module(s) failed to initialize.')

    screen = pygame.display.set_mode(Config.WINDOW_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption(Config.CAPTION)
    clock = pygame.time.Clock()
    rect = pygame.Rect(Config.RECT_START, Config.RECT_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_rect(rect, pygame.key.get_pressed(), screen.get_rect())

        screen.fill(Config.BACKGROUND_COLOR)
        pygame.draw.rect(screen, Config.RECT_COLOR, rect)
        pygame.display.update()
        clock.tick(Config.FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
