import pygame
import random
from enum import Enum, auto

class Colors(Enum):
    BLUE = auto()
    DARK_BLUE = auto()
    MINT = auto()

class GameStates(Enum):
    PLAY = auto()
    WIN = auto()
    LOOSE = auto()
        
class Game:

    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 740
    NUMERIC_KEYS = [
        pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
        pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9
    ]

    NUMERIC_VALUES = {
        pygame.K_0: "0",
        pygame.K_1: "1",
        pygame.K_2: "2",
        pygame.K_3: "3",
        pygame.K_4: "4",
        pygame.K_5: "5",
        pygame.K_6: "6",
        pygame.K_7: "7",
        pygame.K_8: "8",
        pygame.K_9: "9",
    }

    colors = {
        Colors.BLUE: (0, 153, 204),
        Colors.DARK_BLUE: (0, 23, 46),
        Colors.MINT: (204, 255, 255)
    } 

    def __init__(self, numbers_range):
        self.numbers_range = numbers_range
        self.state = GameStates.PLAY
        self.attempts = 1

    def create_number_to_guess(self):
        min, max = self.numbers_range
        number_to_guess = random.randint(min, max)
        return number_to_guess
    
    def draw_label(self, label_text, screen, x_pos = "center", y_pos = 100, color = None):
        if not color:
            color = self.colors[Colors.MINT]

        myfont = pygame.font.SysFont("impact", 64, bold=True, italic=True)
        label = myfont.render(label_text, 1, color)
        if isinstance(x_pos, str) and x_pos == "center":
            x_pos = (self.SCREEN_WIDTH - label.get_width()) // 2
        screen.blit(label, (x_pos, y_pos))
        return None

    def draw_title(self, title, screen):
        self.draw_label(title, screen)
        return None

    def draw_user_input(self, user_input, screen, x_pos, y_pos):
        self.draw_label(user_input, screen, x_pos = x_pos, y_pos = y_pos, color = self.colors[Colors.DARK_BLUE])
        return None

    def draw_attemps_left(self, attempts, screen, y_pos):
        text = f"Attempts left: {11 - attempts}"
        self.draw_label(text, screen, y_pos = y_pos)
        return None

    def create_input_rect(self):
        rect_width = 400
        rect_height = 100
        rect_x_pos = (self.SCREEN_WIDTH - rect_width) // 2
        rect_y_pos = 300
        return pygame.Rect(rect_x_pos, rect_y_pos, rect_width, rect_height)

    def fill_gradient_screen(self, screen):
        gradient_colors = [self.colors[Colors.DARK_BLUE], self.colors[Colors.BLUE]]
        num_gradient_steps = self.SCREEN_HEIGHT
        gradient_step = 1 / num_gradient_steps
                    
        for i in range(num_gradient_steps):
            color = tuple(int(gradient_colors[0][c] * (1 - gradient_step * i) + gradient_colors[1][c] * gradient_step * i) for c in range(3))
            pygame.draw.rect(screen, color, (0, i, self.SCREEN_WIDTH, 1))    

        return None

    def draw_hint(self, hint_message, screen, y_pos):
        self.draw_label(hint_message, screen, y_pos = y_pos)
        return None

    
    def main(self):
        pygame.init()
        running = True
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        label_text = f"Guess number in range {self.numbers_range}"
        input_rect = self.create_input_rect()
        user_input = ""
        number_to_guess = self.create_number_to_guess()

        hint = ""
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.state == GameStates.PLAY:
                            if user_input:
                                user_number = int(user_input)
                                if user_number == number_to_guess:
                                    self.state = GameStates.WIN
                                    hint = ""
                                else:
                                    if self.attempts >= 10:
                                        self.state = GameStates.LOOSE
                                    else:
                                        self.attempts += 1
                                        user_input = ""
                                        hint = "Should be bigger number" if user_number < number_to_guess else "Should be smaller number"
                        else:
                            self.state = GameStates.PLAY
                            number_to_guess = self.create_number_to_guess()
                            user_input = ""
                            self.attempts = 1

                    if self.state == GameStates.PLAY:
                        if event.key == pygame.K_BACKSPACE and user_input:
                            user_input = user_input[:-1]  
                        elif event.key in self.NUMERIC_KEYS:
                            user_input += self.NUMERIC_VALUES[event.key]
            
            self.fill_gradient_screen(screen)

            if self.state == GameStates.PLAY:
                self.draw_title(label_text, screen)
                pygame.draw.rect(screen, self.colors[Colors.MINT], input_rect)
                self.draw_user_input(user_input, screen, input_rect.x + 10, input_rect.y + 25)
                self.draw_attemps_left(self.attempts, screen, input_rect.y + 200)
                self.draw_hint(hint, screen, input_rect.y + 300)
            elif self.state == GameStates.WIN:
                self.draw_title("You win! Press Enter to play again!", screen)
            elif self.state == GameStates.LOOSE:
                self.draw_title("You loose :( Press Enter to play again!", screen)
                        
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    numbers_range = (1, 100)
    game = Game(numbers_range)
    game.main()


