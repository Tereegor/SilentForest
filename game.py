import pygame
import os
import json

# Настройки игры
TILE_SIZE = 10
MAP_FILE = "assets/for_game/map.shifr"
SAVE_FILE = "save.json"
DIARY_FILE = "assets/for_game/diary.txt"

COLORS = {
    "#": (139, 69, 19),  # Коричневый цвет для стены
    ".": (34, 139, 34),  # Зеленый цвет для земли
    "~": (0, 0, 255),  # Синий цвет для воды
    "T": (0, 128, 0),  # Темно-зеленый для деревьев
    "G": (128, 128, 128),  # Серый для камней
    "D": (184, 134, 11),  # Золотистый для песка
}

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SilentForest (Beta)")

def load_map(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл карты {file_path} не найден")

    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def load_hero_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл сохранения {file_path} не найден")

    with open(file_path, "r") as file:
        data = json.load(file)
        return data.get("selected_hero", "default_hero.png")

def load_diary(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл дневника {file_path} не найден")

    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def draw_map(game_map, player_pos, offset_x, offset_y, player_image):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell in COLORS:
                color = COLORS[cell]
                pygame.draw.rect(screen, color,
                                 ((x - offset_x) * TILE_SIZE, (y - offset_y) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    screen.blit(player_image, ((player_pos[0] - offset_x) * TILE_SIZE, (player_pos[1] - offset_y) * TILE_SIZE))

def is_walkable(game_map, x, y):
    for dx in range(3):
        for dy in range(3):
            check_x = x + dx
            check_y = y + dy
            if not (0 <= check_x < len(game_map[0]) and 0 <= check_y < len(game_map)):
                return False
            if game_map[check_y][check_x] not in (".", "~", "D"):  # Проходимые клетки
                return False
    return True

def display_inventory(diary):
    running = True
    font = pygame.font.Font(None, 24)
    header_font = pygame.font.Font(None, 36)
    background_color = (50, 50, 50)
    text_color = (255, 255, 255)
    padding = 10

    diary_surface = pygame.Surface((600, 400))
    diary_surface.fill(background_color)

    header = header_font.render("Инвентарь", True, text_color)
    diary_surface.blit(header, (padding, padding))

    scroll_offset = 0
    max_visible_lines = 15
    diary_opened = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    running = False
                if event.key == pygame.K_DOWN:
                    scroll_offset = min(scroll_offset + 1, max(0, len(diary) - max_visible_lines))
                if event.key == pygame.K_UP:
                    scroll_offset = max(scroll_offset - 1, 0)
                if event.key == pygame.K_RETURN:  # Открыть дневник
                    diary_opened = True

        diary_surface.fill(background_color)
        diary_surface.blit(header, (padding, padding))

        if diary_opened:
            diary_content = load_diary(DIARY_FILE)
            y_offset = padding + 40
            for line in diary_content:
                rendered_line = font.render(line, True, text_color)
                diary_surface.blit(rendered_line, (padding, y_offset))
                y_offset += 25
        else:
            for i, line in enumerate(diary[scroll_offset:scroll_offset + max_visible_lines]):
                line_y = padding + 40 + i * 25
                rendered_line = font.render(line, True, text_color)
                if line == "Дневник":
                    rendered_line = font.render(f"> {line} <", True, text_color)
                diary_surface.blit(rendered_line, (padding, line_y))

        screen.blit(diary_surface, (100, 100))
        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True

    selected_hero_filename = load_hero_data(SAVE_FILE)
    player_image_path = os.path.join("assets", "heroes", f"{selected_hero_filename}.png")

    if not os.path.exists(player_image_path):
        raise FileNotFoundError(f"Изображение героя {selected_hero_filename} не найдено в папке assets/heroes/")

    player_image = pygame.image.load(player_image_path)
    player_image = pygame.transform.scale(player_image, (TILE_SIZE * 3, TILE_SIZE * 3))

    game_map = load_map(MAP_FILE)
    diary = ["Дневник"]  # Элемент дневника в инвентаре

    player_pos = [1, 1]

    screen_width, screen_height = screen.get_size()
    visible_width = screen_width // TILE_SIZE
    visible_height = screen_height // TILE_SIZE

    while running:
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    display_inventory(diary)

        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1

        new_x = player_pos[0] + dx
        new_y = player_pos[1] + dy

        if is_walkable(game_map, new_x, player_pos[1]):
            player_pos[0] = new_x
        if is_walkable(game_map, player_pos[0], new_y):
            player_pos[1] = new_y

        # Сдвиг карты так, чтобы игрок всегда был по центру
        offset_x = max(0, min(player_pos[0] - visible_width // 2, len(game_map[0]) - visible_width))
        offset_y = max(0, min(player_pos[1] - visible_height // 2, len(game_map) - visible_height))

        screen.fill((0, 0, 0))
        draw_map(game_map, player_pos, offset_x, offset_y, player_image)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
