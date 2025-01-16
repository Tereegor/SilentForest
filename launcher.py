import pygame
import os
import json

forest_bg = pygame.image.load("assets/images/forest_background.jpg")
forest_bg = pygame.transform.scale(forest_bg, (1000, 529))

WIDTH, HEIGHT = forest_bg.get_width(), forest_bg.get_height()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Silent Forest Launcher")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (34, 139, 34)
HIGHLIGHT_COLOR = (0, 128, 0)
BUTTON_BORDER_COLOR = (0, 100, 0)

SAVE_FILE = "save.json"


def load_save():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r') as f:
            return json.load(f)
    return None


def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def main():
    pygame.init()
    font = pygame.font.SysFont("Impact", 50)
    sub_font = pygame.font.SysFont("Roboto", 30)

    running = True
    save_data = load_save()

    while running:
        screen.fill(WHITE)
        screen.blit(forest_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render_text("Silent Forest", font, BLACK, WIDTH // 2, 50)

        new_game_button = pygame.Rect(250, 150, 500, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, new_game_button)
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, new_game_button, 3)
        render_text("Новая игра", sub_font, WHITE, WIDTH // 2, 175)

        if save_data:
            load_save_button = pygame.Rect(250, 225, 500, 50)
            pygame.draw.rect(screen, BUTTON_COLOR, load_save_button)
            pygame.draw.rect(screen, BUTTON_BORDER_COLOR, load_save_button, 3)
            render_text("Последнее сохранение", sub_font, WHITE, WIDTH // 2, 250)

        stats_button = pygame.Rect(250, 300, 500, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, stats_button)
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, stats_button, 3)
        render_text("Статистика", sub_font, WHITE, WIDTH // 2, 325)

        pygame.display.flip()

        keys = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if new_game_button.collidepoint(pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, new_game_button)
        if save_data and load_save_button.collidepoint(pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, load_save_button)
        if stats_button.collidepoint(pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, stats_button)

        if keys[0]:
            if new_game_button.collidepoint(pos):
                print("Новая игра")
                running = False
            elif load_save_button.collidepoint(pos) and save_data:
                print("Загрузка последнего сохранения")
                running = False
            elif stats_button.collidepoint(pos):
                print("Показать статистику")
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
