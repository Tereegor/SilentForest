import pygame
import random
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка: Собери 10 яблок за 1 минуту")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        if new_head in self.body or not (0 <= new_head[0] < SCREEN_WIDTH and 0 <= new_head[1] < SCREEN_HEIGHT):
            return False

        self.body.insert(0, new_head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

        return True

    def grow(self):
        self.growing = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

class Apple:
    def __init__(self, snake):
        self.position = self.random_position(snake)

    def random_position(self, snake):
        while True:
            pos = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                   random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            if pos not in snake.body:
                return pos

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

def display_message(message, duration=3):
    text = font.render(message, True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(duration)

display_message("Добро пожаловать в змейку!", 1)
display_message("Соберите 10 яблок за 1 минуту!", 2)

snake = Snake()
apple = Apple(snake)
score = 0
start_time = time.time()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                snake.direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                snake.direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                snake.direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                snake.direction = (CELL_SIZE, 0)

    if not snake.move():
        running = False
        display_message("Вы проиграли!", 3)
        break

    if snake.body[0] == apple.position:
        snake.grow()
        score += 1
        apple = Apple(snake)

    elapsed_time = time.time() - start_time
    if elapsed_time >= 60 or score >= 10:
        running = False
        if score >= 10:
            display_message("Вы победили!", 3)
            print("WIN")
        else:
            display_message("Время вышло! Вы проиграли!", 3)
        break

    screen.fill(BLACK)
    snake.draw()
    apple.draw()

    score_text = font.render(f"Яблоки: {score}/10", True, WHITE)
    screen.blit(score_text, (10, 10))

    time_left = max(0, 60 - int(elapsed_time))
    time_text = font.render(f"Время: {time_left}s", True, WHITE)
    screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
