import pygame
import os
import json
import game

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

# Файл сохранений
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


def save_game(data):
    with open(SAVE_FILE, 'w') as f:
        json.dump(data, f)


def load_heroes():
    heroes_folder = "assets/heroes"
    heroes = []
    for hero_name in os.listdir(heroes_folder):
        hero_image_path = os.path.join(heroes_folder, hero_name)
        if hero_name.endswith(".png"):
            hero_image = pygame.image.load(hero_image_path)
            hero_image = pygame.transform.scale(hero_image, (100, 100))
            heroes.append((hero_name.split(".")[0], hero_image))
    return heroes


def main():
    pygame.init()
    font = pygame.font.SysFont("Impact", 50)
    sub_font = pygame.font.SysFont("Roboto", 30)

    running = True
    save_data = load_save()

    heroes = load_heroes()

    selected_hero = "Rogue"  # По умолчанию выбран "Rogue"

    selected_hero_image = None
    for hero_name, hero_image in heroes:
        if hero_name == selected_hero:
            selected_hero_image = hero_image
            break

    while running:
        screen.fill(WHITE)
        screen.blit(forest_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        render_text("Silent Forest", font, BLACK, WIDTH // 2, 50)

        button_width, button_height = 500, 50
        button_x = 50
        button_y = 150

        new_game_button = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, BUTTON_COLOR, new_game_button)
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, new_game_button, 3)
        render_text("Новая игра", sub_font, WHITE, button_x + button_width // 2, button_y + button_height // 2)

        load_save_button = None
        if save_data:
            load_save_button = pygame.Rect(button_x, button_y + 75, button_width, button_height)
            pygame.draw.rect(screen, BUTTON_COLOR, load_save_button)
            pygame.draw.rect(screen, BUTTON_BORDER_COLOR, load_save_button, 3)
            render_text("Последнее сохранение", sub_font, WHITE, button_x + button_width // 2,
                        button_y + 75 + button_height // 2)

        stats_button = pygame.Rect(button_x, button_y + 150, button_width, button_height)
        pygame.draw.rect(screen, BUTTON_COLOR, stats_button)
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, stats_button, 3)
        render_text("Статистика", sub_font, WHITE, button_x + button_width // 2, button_y + 150 + button_height // 2)

        render_text(f"Выбран: {selected_hero}", sub_font, BLACK, WIDTH // 2 + 300, HEIGHT // 2 - 150)

        hero_x = WIDTH // 2 + 50
        hero_y = 150
        for hero_name, hero_image in heroes:
            hero_button = pygame.Rect(hero_x, hero_y, 100, 100)
            screen.blit(hero_image, (hero_x, hero_y))
            render_text(hero_name, sub_font, BLACK, hero_x + 50, hero_y + 110)

            if hero_button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, hero_button, 5)

            if pygame.mouse.get_pressed()[0] and hero_button.collidepoint(pygame.mouse.get_pos()):
                selected_hero = hero_name

            hero_x += 120

        if not selected_hero:
            select_hero_button = pygame.Rect(button_x, HEIGHT - 250, button_width, button_height)
            pygame.draw.rect(screen, BUTTON_COLOR, select_hero_button)
            pygame.draw.rect(screen, BUTTON_BORDER_COLOR, select_hero_button, 3)
            render_text("Подтвердить выбор", sub_font, WHITE, button_x + button_width // 2,
                        HEIGHT - 225 + button_height // 2)

            if select_hero_button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, select_hero_button, 5)

            if pygame.mouse.get_pressed()[0] and select_hero_button.collidepoint(pygame.mouse.get_pos()):
                print(f"Подтвержден выбор персонажа: {selected_hero}")
                save_game({"new_game": True, "selected_hero": selected_hero})
                running = False

        pygame.display.flip()

        keys = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if new_game_button.collidepoint(pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, new_game_button)
        if load_save_button and load_save_button.collidepoint(pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, load_save_button)
        if stats_button.collidepoint(pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, stats_button)

        if keys[0]:
            if new_game_button.collidepoint(pos):
                save_game({"new_game": True, "selected_hero": selected_hero})
                game.Game().run()
                running = False
            elif load_save_button and load_save_button.collidepoint(pos) and save_data:
                print("Загрузка последнего сохранения")
                running = False
            elif stats_button.collidepoint(pos):
                print("Показать статистику")
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()