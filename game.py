import pygame
import os
import json
import random
import subprocess
from PIL import Image

TILE_SIZE = 12
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 900
FPS = 60
MAP_FILE = 'assets/for_game/map.jpg'
SPAWN = (10, 170)
SPEED = 1
MAX_WINS_PER_GAME = 1


class Game:
    def __init__(self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("SilentForest (Beta)")
        self.clock = pygame.time.Clock()
        self.running = True

        self.map = Map(MAP_FILE)
        self.player = Player('save.json', TILE_SIZE, scale_factor=4)
        self.inventory = Inventory("assets/for_game/diary.txt")

        self.minigames = ["minigames/first.py", "minigames/second.py", "minigames/third.py"]

        self.game_locations = [(248, 88), (68, 453), (496, 338)]
        self.location_minigames = {loc: random.choice(self.minigames) for loc in self.game_locations}

        self.final_game_location = (457, 97)
        self.final_game_path = "minigames/final_game/Project_pygame/Project.py"

        self.notification_text = None
        self.current_location = None

        self.first_game_won = False
        self.second_game_won = False
        self.third_game_won = False
        self.final_game_won = False

        self.e_pressed = False

    def check_game_location(self):
        """Проверяет, находится ли игрок рядом с одной из целей."""
        player_x, player_y = self.player.position

        for target_x, target_y in self.game_locations:
            if (abs(player_x - target_x) <= 7) and (abs(player_y - target_y) <= 7):
                self.current_location = (target_x, target_y)
                minigame_script = self.location_minigames[self.current_location]

                if self.is_game_won(minigame_script):
                    self.notification_text = "Вы уже побеждали в этой мини-игре!"
                else:
                    self.notification_text = "Нажмите 'E', чтобы начать мини-игру"
                return

        fx, fy = self.final_game_location
        if (abs(player_x - fx) <= 7) and (abs(player_y - fy) <= 7):
            if self.all_games_won():
                self.notification_text = "Нажмите 'E' для финальной игры!"
                self.current_location = self.final_game_location
            else:
                self.notification_text = "Вы должны победить в 3 мини-играх!"
                self.current_location = None
            return

        self.notification_text = None
        self.current_location = None

    def all_games_won(self):
        """Проверяет, победил ли игрок во всех 3 мини-играх."""
        return self.first_game_won and self.second_game_won and self.third_game_won

    def is_game_won(self, game_script):
        """Возвращает True, если игрок уже побеждал в данной мини-игре."""
        if game_script == "minigames/first.py":
            return self.first_game_won
        elif game_script == "minigames/second.py":
            return self.second_game_won
        elif game_script == "minigames/third.py":
            return self.third_game_won
        elif game_script == self.final_game_path:
            return self.final_game_won
        return False

    def mark_game_won(self, game_script):
        """Помечает мини-игру как выигранную."""
        if game_script == "minigames/first.py":
            self.first_game_won = True
        elif game_script == "minigames/second.py":
            self.second_game_won = True
        elif game_script == "minigames/third.py":
            self.third_game_won = True
        elif game_script == self.final_game_path:
            self.final_game_won = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.check_game_location()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    print(f"Координаты игрока: X={self.player.position[0]}, Y={self.player.position[1]}")

                if event.key == pygame.K_e and not self.e_pressed and self.notification_text:
                    self.e_pressed = True
                    self.start_mini_game()

                if event.key == pygame.K_i:
                    self.inventory.display(self.screen)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    self.e_pressed = False

        if keys[pygame.K_w]:
            self.player.move(0, -1, self.map)
        if keys[pygame.K_s]:
            self.player.move(0, 1, self.map)
        if keys[pygame.K_a]:
            self.player.move(-1, 0, self.map, facing_right=False)
        if keys[pygame.K_d]:
            self.player.move(1, 0, self.map, facing_right=True)

    def start_mini_game(self):
        """Запускает мини-игру, если игрок ещё не побеждал в ней."""
        if self.current_location:
            if self.current_location == self.final_game_location:
                if self.all_games_won():
                    minigame_script = "minigames/final_game/Project_pygame/Project.py"
                else:
                    print("Вы должны победить в 3 мини-играх перед финальной игрой!")
                    return
            else:
                minigame_script = self.location_minigames[self.current_location]

            if self.is_game_won(minigame_script):
                print("Вы уже побеждали в этой мини-игре!")
                return

            print(f"Запуск мини-игры: {minigame_script}")
            result = subprocess.run(["python", minigame_script], capture_output=True, text=True)

            if "WIN" in result.stdout:
                self.mark_game_won(minigame_script)
                print(f"Вы победили в {minigame_script}!")

    def update(self):
        self.player.update_animation()

    def draw(self):
        self.screen.fill((0, 0, 0))

        offset_x = SCREEN_WIDTH // 2 - self.player.position[0] * TILE_SIZE
        offset_y = SCREEN_HEIGHT // 2 - self.player.position[1] * TILE_SIZE

        self.map.draw(self.screen, offset_x, offset_y)
        self.player.draw(self.screen)

        if self.notification_text:
            font = pygame.font.SysFont(None, 36)
            text_surface = font.render(self.notification_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (SCREEN_WIDTH - text_surface.get_width() - 20, 20))

        pygame.display.flip()


class Map:
    def __init__(self, file_path):
        self.image = pygame.image.load(file_path).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.walkable_colors = [
            (190, 120, 86),
            (36, 114, 13)
        ]
        self.tolerance = 10

    def is_walkable(self, x, y):
        """Проверяет, является ли клетка (x, y) проходимой."""
        if 0 <= x < self.width and 0 <= y < self.height:
            color = self.image.get_at((x, y))[:3]
            for walkable_color in self.walkable_colors:
                if all(abs(c - wc) <= self.tolerance for c, wc in zip(color, walkable_color)):
                    return True
            return False
        return False

    def draw(self, screen, offset_x, offset_y):
        start_x = max(0, (-offset_x) // TILE_SIZE)
        start_y = max(0, (-offset_y) // TILE_SIZE)
        end_x = min(self.width, (SCREEN_WIDTH - offset_x) // TILE_SIZE + 1)
        end_y = min(self.height, (SCREEN_HEIGHT - offset_y) // TILE_SIZE + 1)

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                color = self.image.get_at((x, y))
                pygame.draw.rect(screen, color,
                                 (x * TILE_SIZE + offset_x,
                                  y * TILE_SIZE + offset_y,
                                  TILE_SIZE, TILE_SIZE))


class Player:
    def __init__(self, save_file, tile_size, scale_factor=2):
        self.position = list(SPAWN)
        self.tile_size = tile_size
        self.scale_factor = scale_factor
        self.facing_right = True
        self.frames = self.load_hero_frames(save_file)
        self.current_frame_index = 0
        self.animation_speed = 2
        self.animation_counter = 0
        self.sanity = 20

    def load_hero_frames(self, save_file):
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
        frame_index = 0
        while True:
            try:
                gif.seek(frame_index)
                frame = gif.copy().convert("RGBA")
                new_size = (self.tile_size * self.scale_factor, self.tile_size * self.scale_factor)
                frame = frame.resize(new_size)
                frame_surface = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
                frames.append(frame_surface)
                frame_index += 1
            except EOFError:
                break
        return frames

    def draw(self, screen):
        frame = self.frames[self.current_frame_index]
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)

        player_width = self.tile_size * self.scale_factor
        player_height = self.tile_size * self.scale_factor

        player_x = SCREEN_WIDTH // 2 - player_width // 2
        player_y = SCREEN_HEIGHT // 2 - player_height // 2

        screen.blit(frame, (player_x, player_y))

    def move(self, dx, dy, game_map, facing_right=None):
        dx *= SPEED
        dy *= SPEED

        new_x = self.position[0] + dx
        new_y = self.position[1] + dy

        if game_map.is_walkable(int(new_x), int(self.position[1])):
            self.position[0] = new_x
        if game_map.is_walkable(int(self.position[0]), int(new_y)):
            self.position[1] = new_y

        if facing_right is not None:
            self.facing_right = facing_right

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
            self.animation_counter = 0


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


if __name__ == "__main__":
    game = Game()
    game.run()
