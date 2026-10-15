"""Guess the number game.

Controls:
    digits      - type a guess
    Backspace   - erase the last digit
    Enter       - submit the guess
    R           - start a new game
    Esc         - quit
"""

from random import randint

import pygame

LOWER_BOUND = 1
UPPER_BOUND = 100
MAX_ATTEMPTS = 10

WINDOW_SIZE = (640, 480)
FPS = 60

BACKGROUND_COLOR = (24, 28, 38)
TEXT_COLOR = (235, 238, 245)
HINT_COLOR = (150, 158, 175)
INPUT_COLOR = (255, 214, 102)
WIN_COLOR = (126, 217, 137)
LOSE_COLOR = (233, 112, 112)


def new_game() -> dict:
    """Create the state of a new game: a secret number and empty counters."""
    return {
        "running": True,
        "secret_number": randint(LOWER_BOUND, UPPER_BOUND),
        "attempts_used": 0,
        "typed_text": "",
        "message": f"I guessed a number from {LOWER_BOUND} to {UPPER_BOUND}.",
        "message_color": TEXT_COLOR,
        "history": [],
        "game_over": False,
    }


def attempts_left(state: dict) -> int:
    """Return how many attempts the player still has."""
    return MAX_ATTEMPTS - state["attempts_used"]


def submit_guess(state: dict) -> None:
    """Check the typed number and update the game state."""
    if not state["typed_text"]:
        return

    guess = int(state["typed_text"])
    state["typed_text"] = ""

    if not LOWER_BOUND <= guess <= UPPER_BOUND:
        state["message"] = f"Enter a number from {LOWER_BOUND} to {UPPER_BOUND}."
        state["message_color"] = LOSE_COLOR
        return

    state["attempts_used"] += 1

    if guess == state["secret_number"]:
        state["history"].append(f"{guess} - correct!")
        state["message"] = (f"Congratulations! You guessed it "
                            f"in {state['attempts_used']} attempt(s).")
        state["message_color"] = WIN_COLOR
        state["game_over"] = True
    elif guess < state["secret_number"]:
        state["history"].append(f"{guess} - too low")
        state["message"] = "My number is greater."
        state["message_color"] = TEXT_COLOR
    else:
        state["history"].append(f"{guess} - too high")
        state["message"] = "My number is less."
        state["message_color"] = TEXT_COLOR

    if not state["game_over"] and attempts_left(state) == 0:
        state["message"] = (f"Attempts are over. "
                            f"My number was {state['secret_number']}.")
        state["message_color"] = LOSE_COLOR
        state["game_over"] = True


def handle_key(state: dict, event: pygame.event.Event) -> dict:
    """Handle a single key press and return the (possibly new) game state."""
    if event.key == pygame.K_ESCAPE:
        state["running"] = False
    elif event.key == pygame.K_r:
        state = new_game()
    elif state["game_over"]:
        return state
    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
        submit_guess(state)
    elif event.key == pygame.K_BACKSPACE:
        state["typed_text"] = state["typed_text"][:-1]
    elif event.unicode.isdigit() and len(state["typed_text"]) < len(str(UPPER_BOUND)):
        state["typed_text"] += event.unicode

    return state


def handle_events(state: dict) -> dict:
    """Process the events that happened since the previous frame."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
        elif event.type == pygame.KEYDOWN:
            state = handle_key(state, event)

    return state


def draw_text(screen, text: str, font: pygame.font.Font, color, y: int) -> None:
    """Draw a line of text horizontally centered at the given height."""
    surface = font.render(text, True, color)
    screen.blit(surface, surface.get_rect(center=(WINDOW_SIZE[0] // 2, y)))


def draw(screen, fonts: dict, state: dict) -> None:
    """Render the current frame."""
    screen.fill(BACKGROUND_COLOR)

    draw_text(screen, "Guess the number", fonts["title"], TEXT_COLOR, 50)
    draw_text(screen, state["message"], fonts["main"], state["message_color"], 110)
    draw_text(screen, f"Attempts left: {attempts_left(state)}",
              fonts["main"], HINT_COLOR, 150)

    if state["game_over"]:
        draw_text(screen, "Press R to play again or Esc to quit",
                  fonts["main"], HINT_COLOR, 200)
    else:
        draw_text(screen, f"Your guess: {state['typed_text']}_",
                  fonts["main"], INPUT_COLOR, 200)

    for number, record in enumerate(state["history"]):
        draw_text(screen, record, fonts["small"], HINT_COLOR, 250 + number * 22)

    pygame.display.flip()


def main() -> None:
    """Set up pygame and run the main game loop."""
    pygame.init()
    pygame.display.set_caption("Guess the number")
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    fonts = {
        "title": pygame.font.SysFont("arial", 34, bold=True),
        "main": pygame.font.SysFont("arial", 24),
        "small": pygame.font.SysFont("arial", 18),
    }

    state = new_game()

    while state["running"]:
        state = handle_events(state)
        draw(screen, fonts, state)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
