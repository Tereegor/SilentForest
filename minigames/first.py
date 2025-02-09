import pygame
import random
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (160, 32, 240)
RED = (255, 0, 0)

COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 40

SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Упрощенный Тетрис")

clock = pygame.time.Clock()


class Tetrimino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]


def check_collision(grid, tetrimino, offset_x=0, offset_y=0):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = tetrimino.x + x + offset_x
                new_y = tetrimino.y + y + offset_y
                if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or grid[new_y][new_x]:
                    return True
    return False


def merge_tetrimino(grid, tetrimino):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[tetrimino.y + y][tetrimino.x + x] = tetrimino.color


def clear_lines(grid):
    new_grid = [row for row in grid if any(cell is None for cell in row)]
    cleared = GRID_HEIGHT - len(new_grid)
    for _ in range(cleared):
        new_grid.insert(0, [None] * GRID_WIDTH)
    return new_grid, cleared


def show_message(text):
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 3))
    pygame.display.flip()
    time.sleep(2)


def game_loop():
    grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    tetrimino = Tetrimino()
    score = 0
    speed = 5
    running = True
    game_over = False

    show_message("Очистите 2 линии для победы!")

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(grid, tetrimino, offset_x=-1):
                    tetrimino.x -= 1
                if event.key == pygame.K_RIGHT and not check_collision(grid, tetrimino, offset_x=1):
                    tetrimino.x += 1
                if event.key == pygame.K_DOWN:
                    while not check_collision(grid, tetrimino, offset_y=1):
                        tetrimino.y += 1
                if event.key == pygame.K_UP:
                    tetrimino.rotate()
                    if check_collision(grid, tetrimino):
                        tetrimino.rotate()
                        tetrimino.rotate()
                        tetrimino.rotate()

        if not check_collision(grid, tetrimino, offset_y=1):
            tetrimino.y += 1
        else:
            merge_tetrimino(grid, tetrimino)
            grid, cleared = clear_lines(grid)
            score += cleared
            tetrimino = Tetrimino()
            if check_collision(grid, tetrimino):
                game_over = True

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        for y, row in enumerate(tetrimino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, tetrimino.color, (
                    (tetrimino.x + x) * BLOCK_SIZE, (tetrimino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, GRAY, (
                    (tetrimino.x + x) * BLOCK_SIZE, (tetrimino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        text = pygame.font.SysFont(None, 36).render(f"Очищено: {score}/2", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()

        if score >= 2:
            running = False
            show_message("Поздравляем, вы победили!")
            print("WIN")
            break

        if game_over:
            show_message("Вы проиграли!")
            break

        clock.tick(speed)


game_loop()
pygame.quit()
