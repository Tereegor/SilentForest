import pygame
import os
import json
from PIL import Image

# Настройки игры
TILE_SIZE = 20
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


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("SilentForest (Beta)")
        self.clock = pygame.time.Clock()
        self.running = True

        self.map = Map(MAP_FILE)
        self.player = Player(SAVE_FILE, TILE_SIZE)
        self.inventory = Inventory(DIARY_FILE)
        self.mini_map = MiniMap(self.map, (200, 200))

        # self.sounds = {
        #     "step": pygame.mixer.Sound("assets/sounds/step.wav"),
        #     "inventory": pygame.mixer.Sound("assets/sounds/inventory.wav"),
        # }

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(30)
        pygame.quit()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    # self.sounds["inventory"].play()
                    self.inventory.display(self.screen)

        if keys[pygame.K_UP]:
            self.player.move(0, -1, self.map)
            # self.sounds["step"].play()
        if keys[pygame.K_DOWN]:
            self.player.move(0, 1, self.map)
            # self.sounds["step"].play()
        if keys[pygame.K_LEFT]:
            self.player.move(-1, 0, self.map, facing_right=False)
            # self.sounds["step"].play()
        if keys[pygame.K_RIGHT]:
            self.player.move(1, 0, self.map, facing_right=True)
            # self.sounds["step"].play()

    def update(self):
        self.player.update_animation()

    def draw(self):
        self.screen.fill((0, 0, 0))
        offset_x, offset_y = self.map.calculate_offset(self.player.position, self.screen.get_size())
        self.map.draw(self.screen, offset_x, offset_y)
        self.player.draw(self.screen, offset_x, offset_y)
        self.mini_map.draw(self.screen, self.player.position)
        self.draw_sanity_bar()
        pygame.display.flip()

    def draw_sanity_bar(self):
        font = pygame.font.Font(None, 36)
        sanity_text = font.render(f"Рассудок: {self.player.sanity}", True, (255, 255, 255))
        bar_x, bar_y, bar_width, bar_height = 10, 10, 200, 20
        sanity_ratio = self.player.sanity / 100
        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, bar_width * sanity_ratio, bar_height))
        self.screen.blit(sanity_text, (bar_x, bar_y - 30))


class Map:
    def __init__(self, file_path):
        self.grid = self.load_map(file_path)

    def load_map(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл карты {file_path} не найден")
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def draw(self, screen, offset_x, offset_y):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell in COLORS:
                    color = COLORS[cell]
                    pygame.draw.rect(screen, color,
                                     ((x - offset_x) * TILE_SIZE, (y - offset_y) * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def is_walkable(self, x, y):
        for dx in range(3):
            for dy in range(3):
                check_x = x + dx
                check_y = y + dy
                if not (0 <= check_x < len(self.grid[0]) and 0 <= check_y < len(self.grid)):
                    return False
                if self.grid[check_y][check_x] not in (".", "~", "D"):
                    return False
        return True

    def calculate_offset(self, player_pos, screen_size):
        screen_width, screen_height = screen_size
        visible_width = screen_width // TILE_SIZE
        visible_height = screen_height // TILE_SIZE
        offset_x = max(0, min(player_pos[0] - visible_width // 2, len(self.grid[0]) - visible_width))
        offset_y = max(0, min(player_pos[1] - visible_height // 2, len(self.grid) - visible_height))
        return offset_x, offset_y


class Player:
    def __init__(self, save_file, tile_size):
        self.position = [1, 1]
        self.tile_size = tile_size
        self.facing_right = True
        self.frames = self.load_hero_frames(save_file, tile_size)
        self.current_frame_index = 0
        self.animation_speed = 2
        self.animation_counter = 0
        self.sanity = 20

    def load_hero_frames(self, save_file, tile_size):
        if not os.path.exists(save_file):
            raise FileNotFoundError(f"Файл сохранения {save_file} не найден")
        with open(save_file, "r") as file:
            data = json.load(file)
            hero_filename = data.get("selected_hero", "default_hero.gif")

        hero_path = os.path.join("assets", "heroes", hero_filename) + ".gif"
        if not os.path.exists(hero_path):
            raise FileNotFoundError(f"Изображение героя {hero_path} не найдено")

        gif = Image.open(hero_path)
        frames = []
        try:
            while True:
                frame = gif.copy().convert("RGBA")
                frame = frame.resize((tile_size * 3, tile_size * 3))
                frame_surface = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
                frames.append(frame_surface)
                gif.seek(len(frames))
        except EOFError:
            pass
        return frames

    def move(self, dx, dy, game_map, facing_right=None):
        new_x = self.position[0] + dx
        new_y = self.position[1] + dy

        if game_map.is_walkable(new_x, self.position[1]):
            self.position[0] = new_x
        if game_map.is_walkable(self.position[0], new_y):
            self.position[1] = new_y

        if facing_right is not None:
            self.facing_right = facing_right

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
            self.animation_counter = 0

    def draw(self, screen, offset_x, offset_y):
        frame = self.frames[self.current_frame_index]
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, ((self.position[0] - offset_x) * TILE_SIZE, (self.position[1] - offset_y) * TILE_SIZE))


class Inventory:
    def __init__(self, diary_file):
        self.diary_file = diary_file
        self.diary = ["Дневник"]

    def load_diary(self):
        if not os.path.exists(self.diary_file):
            raise FileNotFoundError(f"Файл дневника {self.diary_file} не найден")
        with open(self.diary_file, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    def display(self, screen):
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
                        scroll_offset = min(scroll_offset + 1, max(0, len(self.diary) - max_visible_lines))
                    if event.key == pygame.K_UP:
                        scroll_offset = max(scroll_offset - 1, 0)
                    if event.key == pygame.K_RETURN:
                        diary_opened = True

            diary_surface.fill(background_color)
            diary_surface.blit(header, (padding, padding))

            if diary_opened:
                diary_content = self.load_diary()
                y_offset = padding + 40
                for line in diary_content:
                    rendered_line = font.render(line, True, text_color)
                    diary_surface.blit(rendered_line, (padding, y_offset))
                    y_offset += 25
            else:
                for i, line in enumerate(self.diary[scroll_offset:scroll_offset + max_visible_lines]):
                    line_y = padding + 40 + i * 25
                    rendered_line = font.render(line, True, text_color)
                    if line == "Дневник":
                        rendered_line = font.render(f"> {line} <", True, text_color)
                    diary_surface.blit(rendered_line, (padding, line_y))

            screen.blit(diary_surface, (100, 100))
            pygame.display.flip()


class MiniMap:
    def __init__(self, game_map, size):
        self.game_map = game_map
        self.width, self.height = size

    def draw(self, screen, player_pos):
        minimap_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        minimap_surface.fill((0, 0, 0, 128))

        scale = min(self.width / len(self.game_map.grid[0]), self.height / len(self.game_map.grid))

        for y, row in enumerate(self.game_map.grid):
            for x, cell in enumerate(row):
                if cell in COLORS:
                    color = COLORS[cell]
                    pygame.draw.rect(minimap_surface, color,
                                     (x * scale, y * scale, scale, scale))

        player_x = player_pos[0] * scale
        player_y = player_pos[1] * scale
        pygame.draw.circle(minimap_surface, (255, 0, 0), (int(player_x + scale / 2), int(player_y + scale / 2)), 5)

        pygame.draw.rect(minimap_surface, (255, 255, 255), (0, 0, self.width, self.height), 2)

        screen.blit(minimap_surface, (screen.get_width() - self.width - 10, 10))


if __name__ == "__main__":
    game = Game()
    game.run()
