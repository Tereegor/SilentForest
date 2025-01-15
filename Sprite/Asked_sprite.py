# import os
# import sys
# import pygame
#
# pygame.init()
# pygame.display.set_caption('Герой двигается')
# size = width, height = 300, 300
# screen = pygame.display.set_mode(size)
# fps = 30
# plenty = [0, 0]
# screen.fill('white')
#
#
# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image
#
#
# all_sprites = pygame.sprite.Group()
# clock = pygame.time.Clock()
#

#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] == 1:
#             plenty[0] -= 10
#             cursor.rect.x, cursor.rect.y = plenty[0], plenty[1]
#             screen.fill('white')
#             all_sprites.draw(screen)
#         if keys[pygame.K_RIGHT] == 1:
#             plenty[0] += 10
#             cursor.rect.x, cursor.rect.y = plenty[0], plenty[1]
#             screen.fill('white')
#             all_sprites.draw(screen)
#         if keys[pygame.K_UP] == 1:
#             plenty[1] -= 10
#             cursor.rect.x, cursor.rect.y = plenty[0], plenty[1]
#             screen.fill('white')
#             all_sprites.draw(screen)
#         if keys[pygame.K_DOWN] == 1:
#             plenty[1] += 10
#             cursor.rect.x, cursor.rect.y = plenty[0], plenty[1]
#             screen.fill('white')
#             all_sprites.draw(screen)
#     pygame.display.flip()
#     all_sprites.draw(screen)
#     clock.tick(fps)
#
# pygame.quit()
# import pygame
#
# if __name__ == '__main__':
#     pygame.init()
#     pygame.display.set_caption('Вентилятор')
#     size = width, height = 201, 201
#     screen = pygame.display.set_mode(size)
#     running = True
#     fps = 60
#     plus = 40000
#     screen.fill('black')
#     clock = pygame.time.Clock()
#     pygame.time.set_timer(plus, 10)
#     plenty_1 = [80, 30, 120, 30]
#     plenty_2 = [171, 122, 152, 155]
#     plenty_3 = [30, 122, 48, 155]
#     pygame.draw.circle(screen, (pygame.Color('white')), (100, 100), 20)
#     pygame.draw.polygon(screen, (pygame.Color('white')),
#                         [(100, 100), (plenty_1[0], plenty_1[1]), (plenty_1[2], plenty_1[3])])
#     pygame.draw.polygon(screen, (pygame.Color('white')),
#                         [(100, 100), (plenty_2[0], plenty_2[1]), (plenty_2[2], plenty_2[3])])
#     pygame.draw.polygon(screen, (pygame.Color('white')),
#                         [(100, 100), (plenty_3[0], plenty_3[1]), (plenty_3[2], plenty_3[3])])
#     pygame.draw.circle(screen, pygame.Color('white'), (100, 100), 76, 4)
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     if plenty_1[0] <= 100:
#                         plenty_1[0] += 1
#                         plenty_1[1] -= 1
#                         plenty_1[2] += 1
#                         plenty_1[3] += 1
#                         screen.fill('black')
#                         pygame.draw.circle(screen, (pygame.Color('white')), (100, 100), 20)
#                         pygame.draw.polygon(screen, (pygame.Color('white')),
#                                         [(100, 100), (plenty_1[0], plenty_1[1]), (plenty_1[2], plenty_1[3])])
#                         pygame.draw.polygon(screen, (pygame.Color('white')), [(100, 100), (175, 122), (160, 155)])
#                         pygame.draw.polygon(screen, (pygame.Color('white')), [(100, 100), (30, 122), (45, 155)])
#                     else:
#                         plenty_1[0] += 1
#                         plenty_1[1] += 1
#                         plenty_1[2] += 1
#                         plenty_1[3] += 1
#                         screen.fill('black')
#                         pygame.draw.circle(screen, (pygame.Color('white')), (100, 100), 20)
#                         pygame.draw.polygon(screen, (pygame.Color('white')),
#                                         [(100, 100), (plenty_1[0], plenty_1[1]), (plenty_1[2], plenty_1[3])])
#                         pygame.draw.polygon(screen, (pygame.Color('white')), [(100, 100), (175, 122), (160, 155)])
#                         pygame.draw.polygon(screen, (pygame.Color('white')), [(100, 100), (30, 122), (45, 155)])
#         pygame.display.flip()
#         clock.tick(fps)
#     pygame.display.flip()
#     clock.tick(fps)
# pygame.quit()

# import csv
#
# plenty_words = []
# plenty = []
# plenty_achievements = [0]
# plenty_index = [0]
# counter = 1

#     reader = csv.reader(csvfile, delimiter=';', quotechar='"')
#     for index, row in enumerate(reader):
#         plenty_words.append(row)
#         if index >= 1:
#             plenty.append(row[2])
#         if len(plenty) >= 2:
#             if int(plenty[-2]) >= int(plenty[-1]):
#                 counter += 1
#             if int(plenty[-1]) > int(plenty[-2]) and counter > plenty_achievements[0]:
#                 plenty_achievements[0] = counter
#                 plenty_index[0] = index - counter
#                 counter = 1
#             elif int(plenty[-1]) > int(plenty[-2]) and counter <= plenty_achievements[0]:
#                 counter = 1
#     if counter > plenty_achievements[0]:
#         plenty_achievements[0] = counter
#         plenty_index[0] = index - counter + 1
# say = plenty_index[0]

#     csvfile.write(plenty_words[say][0] + ' ')
#     csvfile.write(plenty_words[say][1])
# import pygame
#
#
# class Board:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.board = [[0] * width for _ in range(height)]
#         # значения по умолчанию
#         self.left = 10
#         self.top = 10
#         self.cell_size = 30
#
#     def set_view(self, left, top, cell_size):
#         self.left = left
#         self.top = top
#         self.cell_size = cell_size
#
#     def render(self, screen):
#         for i in range(0, self.width):
#             for j in range(0, self.height):
#                 pygame.draw.rect(screen, pygame.Color('white'),
#                                  (i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
#                                   self.cell_size),
#                                  1)
#
#     def get_click(self, mouse_pos):
#         self.get_cell(mouse_pos)
#         self.on_click(mouse_pos)
#
#     def get_cell(self, mouse_pos):
#         coords_x, coords_y = mouse_pos
#         starts_len = coords_x - self.left
#         starts_height = coords_y - self.top
#         coords_len = starts_len // self.cell_size
#         coords_height = starts_height // self.cell_size
#         if coords_len in range(self.width) and coords_height in range(self.height):
#             return coords_len, coords_height
#         else:
#             return None
#
#     def on_click(self, cell_coords):
#         self.coordinates = self.get_cell(cell_coords)
#
#     def draw(self, screen):
#         if self.coordinates:
#             number = 0
#             for i in range(self.width):
#                 digit_x = self.left + number * self.cell_size
#                 digit_y = self.top + self.coordinates[1] * self.cell_size
#                 if self.board[number][self.coordinates[1]] == 0 and number != self.coordinates[0]:
#                     pygame.draw.rect(screen, pygame.Color('white'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[number][self.coordinates[1]] = 1
#                 elif self.board[number][self.coordinates[1]] == 1 and number != self.coordinates[0]:
#                     pygame.draw.rect(screen, pygame.Color('black'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[number][self.coordinates[1]] = 0
#                 number += 1
#             counter = 0
#             for j in range(self.height):
#                 digit_x = self.left + self.coordinates[0] * self.cell_size
#                 digit_y = self.top + self.cell_size * counter
#                 if self.board[self.coordinates[0]][counter] == 0:
#                     pygame.draw.rect(screen, pygame.Color('white'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[self.coordinates[0]][counter] = 1
#                 elif self.board[self.coordinates[0]][counter] == 1:
#                     pygame.draw.rect(screen, pygame.Color('black'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[self.coordinates[0]][counter] = 0
#                 counter += 1
#
#     def color_change(self, screen):
#         if self.coordinates:
#             digit_x = self.left + self.coordinates[0] * self.cell_size
#             digit_y = self.top + self.coordinates[1] * self.cell_size
#             if self.board[self.coordinates[0]][self.coordinates[1]] == 0 and plenty_priority[0] == 0:
#                 pygame.draw.line(screen, pygame.Color('blue'),
#                                  [digit_x + 2, digit_y + 2],
#                                  [digit_x - 4 + self.cell_size, digit_y - 4 + self.cell_size], 2)
#                 pygame.draw.line(screen, pygame.Color('blue'),
#                                  [digit_x + 2, digit_y + self.cell_size - 2],
#                                  [digit_x + self.cell_size - 2, digit_y + 2], 2)
#                 self.board[self.coordinates[0]][self.coordinates[1]] = 1
#                 plenty_priority[0] = 1
#             elif self.board[self.coordinates[0]][self.coordinates[1]] == 0 and plenty_priority[0] == 1:
#                 pygame.draw.circle(screen, pygame.Color('red'),
#                                    (digit_x + 0.5 * self.cell_size, digit_y + 0.5 * self.cell_size),
#                                    self.cell_size * 0.5 - 2, 2)
#                 self.board[self.coordinates[0]][self.coordinates[1]] = 1
#                 plenty_priority[0] = 0
#
#
# plenty_priority = [0]
#
#
# def main():
#     pygame.init()
#     size = 500, 500
#     screen = pygame.display.set_mode(size)
#     screen.fill('black')
#     pygame.display.set_caption('Инициализация игры')
#
#     board = Board(5, 5)
#     board.set_view(40, 60, 100)
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 board.get_click(event.pos)
#                 # board.draw(screen)
#                 board.color_change(screen)
#         board.render(screen)
#         pygame.display.flip()
#     pygame.quit()
#
#
# # if __name__ == '__main__':

# import pygame
# plenty = [1]
#
# if __name__ == '__main__':
#     pygame.init()
#     pygame.display.set_caption('Шарики')
#     size = width, height = 200, 200
#     screen = pygame.display.set_mode(size)
#     running = True
#     fps = 60
#     screen.fill('black')
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.VIDEOEXPOSE:
#                 screen.fill('black')
#                 font = pygame.font.Font(None, 100)
#                 text = font.render(str(plenty[0]), True, ('red'))
#                 text_x = width // 2 - text.get_width() // 2
#                 text_y = height // 2 - text.get_height() // 2
#                 text_w = text.get_width()
#                 text_h = text.get_height()
#                 screen.blit(text, (text_x, text_y))
#                 plenty[0] += 1
#
#         pygame.display.flip()
#     pygame.quit()
# import os
# import sys
# import pygame
# import random
#
# pygame.init()
# pygame.display.set_caption('Boom them all')
# size = width, height = 500, 500
# screen = pygame.display.set_mode(size)
# fps = 100
# plenty = []
# screen.fill('black')
#
#
# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image
#
#
# clock = pygame.time.Clock()
# all_sprites = pygame.sprite.Group()
#
# # создадим спрайт
# sprite = pygame.sprite.Sprite()
#

#
#     def __init__(self, group):
#         # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
#         # Это очень важно !!!
#         super().__init__(group)
#         self.image = Bomb.image
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(width)
#         self.rect.y = random.randrange(height)
#
#     def update(self, *args):
#         if args and args[0].type == pygame.MOUSEBUTTONUP and \
#                 self.rect.collidepoint(args[0].pos):
#             self.image = self.image_boom
#
#
#
# screen.fill('black')
# for i in range(50):
#     Bomb(all_sprites)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         screen.fill('black')
#         all_sprites.draw(screen)
#         all_sprites.update(event)
#     pygame.display.flip()
#     clock.tick(fps)
#
# pygame.quit()
# import pygame
# plenty = [1]
#
# if __name__ == '__main__':
#     pygame.init()
#     pygame.display.set_caption('Шарики')
#     size = width, height = 200, 200
#     screen = pygame.display.set_mode(size)
#     running = True
#     fps = 60
#     screen.fill('black')
#     font = pygame.font.Font(None, 100)
#     text = font.render(str(plenty[0]), True, 'red')
#     text_x = width // 2 - text.get_width() // 2
#     text_y = height // 2 - text.get_height() // 2
#     text_w = text.get_width()
#     text_h = text.get_height()
#     screen.blit(text, (text_x, text_y))
#     plenty[0] += 1
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.WINDOWMINIMIZED:
#                 screen.fill('black')
#                 font = pygame.font.Font(None, 100)
#                 text = font.render(str(plenty[0]), True, 'red')
#                 text_x = width // 2 - text.get_width() // 2
#                 text_y = height // 2 - text.get_height() // 2
#                 text_w = text.get_width()
#                 text_h = text.get_height()
#                 screen.blit(text, (text_x, text_y))
#                 plenty[0] += 1
#
#         pygame.display.flip()
#     pygame.quit()
# import pygame
#
#
# class Board:
#     def __init__(self):
#         self.left = 10
#         self.top = 10
#         self.cell_size = 30
#
#     def set_view(self, cell_size):
#         self.cell_size = cell_size
#         self.width = 480 // cell_size
#         self.height = 480 // cell_size
#         self.board = [[0] * self.width for _ in range(self.height)]
#
#     def render(self, screen):
#         for i in range(0, self.width):
#             for j in range(0, self.height):
#                 pygame.draw.rect(screen, pygame.Color('white'),
#                                  (i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
#                                   self.cell_size),
#                                  1)
#
#     def get_click(self, mouse_pos):
#         self.get_cell(mouse_pos)
#         self.on_click(mouse_pos)
#
#     def get_cell(self, mouse_pos):
#         coords_x, coords_y = mouse_pos
#         starts_len = coords_x - self.left
#         starts_height = coords_y - self.top
#         coords_len = starts_len // self.cell_size
#         coords_height = starts_height // self.cell_size
#         if coords_len in range(self.width) and coords_height in range(self.height):
#             return coords_len, coords_height
#         else:
#             return None
#
#     def on_click(self, cell_coords):
#         self.coordinates = self.get_cell(cell_coords)
#
#     def draw(self, screen):
#         if self.coordinates:
#             number = 0
#             for i in range(self.width):
#                 digit_x = self.left + number * self.cell_size
#                 digit_y = self.top + self.coordinates[1] * self.cell_size
#                 if self.board[number][self.coordinates[1]] == 0 and number != self.coordinates[0]:
#                     pygame.draw.rect(screen, pygame.Color('white'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[number][self.coordinates[1]] = 1
#                 elif self.board[number][self.coordinates[1]] == 1 and number != self.coordinates[0]:
#                     pygame.draw.rect(screen, pygame.Color('black'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[number][self.coordinates[1]] = 0
#                 number += 1
#             counter = 0
#             for j in range(self.height):
#                 digit_x = self.left + self.coordinates[0] * self.cell_size
#                 digit_y = self.top + self.cell_size * counter
#                 if self.board[self.coordinates[0]][counter] == 0:
#                     pygame.draw.rect(screen, pygame.Color('white'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[self.coordinates[0]][counter] = 1
#                 elif self.board[self.coordinates[0]][counter] == 1:
#                     pygame.draw.rect(screen, pygame.Color('black'),
#                                      (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                     self.board[self.coordinates[0]][counter] = 0
#                 counter += 1
#
#     def color_change(self, screen):
#         if self.coordinates:
#             digit_x = self.left + self.coordinates[0] * self.cell_size
#             digit_y = self.top + self.coordinates[1] * self.cell_size
#             if self.board[self.coordinates[0]][self.coordinates[1]] == 0 and plenty_priority[0] == 0:
#                 pygame.draw.line(screen, pygame.Color('blue'),
#                                  [digit_x + 2, digit_y + 2],
#                                  [digit_x - 4 + self.cell_size, digit_y - 4 + self.cell_size], 2)
#                 pygame.draw.line(screen, pygame.Color('blue'),
#                                  [digit_x + 2, digit_y + self.cell_size - 2],
#                                  [digit_x + self.cell_size - 2, digit_y + 2], 2)
#                 self.board[self.coordinates[0]][self.coordinates[1]] = 1
#                 plenty_priority[0] = 1
#             elif self.board[self.coordinates[0]][self.coordinates[1]] == 0 and plenty_priority[0] == 1:
#                 pygame.draw.circle(screen, pygame.Color('red'),
#                                    (digit_x + 0.5 * self.cell_size, digit_y + 0.5 * self.cell_size),
#                                    self.cell_size * 0.5 - 2, 2)
#                 self.board[self.coordinates[0]][self.coordinates[1]] = 1
#                 plenty_priority[0] = 0
#
#
# plenty_priority = [0]
#
#
# def main():
#     pygame.init()
#     size = 500, 500
#     screen = pygame.display.set_mode(size)
#     screen.fill('black')
#     pygame.display.set_caption('Инициализация игры')
#
#     board = Board()
#     board.set_view(30)
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 board.get_click(event.pos)
#                 board.color_change(screen)
#         board.render(screen)
#         pygame.display.flip()
#     pygame.quit()
#
#
# if __name__ == '__main__':
#     main()
# import pygame
# import random
#
# digit = int(input())
#
#
# class Board:
#     def __init__(self):
#         self.left = 10
#         self.top = 10
#         self.cell_size = 30
#
#     def set_view(self, cell_size):
#         self.cell_size = cell_size
#         self.width = cell_size * digit
#         self.height = cell_size * digit
#         self.board = [[0] * digit for _ in range(digit)]
#
#     def render(self, screen):
#         for i in range(0, digit):
#             for j in range(0, digit):
#                 pygame.draw.rect(screen, pygame.Color('white'),
#                                  (i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
#                                   self.cell_size),
#                                  1)
#
#     def color(self):
#         for i in range(digit):
#             for j in range(digit):
#                 number = random.randrange(0, 2)
#                 self.board[i][j] = number
#
#     def filling(self, screen):
#         for i in range(0, digit):
#             for j in range(0, digit):
#                 if self.board[i][j] == 1:
#                     pygame.draw.circle(screen, pygame.Color('red'),
#                                        (i * self.cell_size + self.left + 0.5 * self.cell_size,
#                                         j * self.cell_size + self.top + 0.5 * self.cell_size), self.cell_size / 2 - 1)
#                 elif self.board[i][j] == 0:
#                     pygame.draw.circle(screen, pygame.Color('blue'),
#                                        (i * self.cell_size + self.left + 0.5 * self.cell_size,
#                                         j * self.cell_size + self.top + 0.5 * self.cell_size), self.cell_size / 2 - 1)
#
#     def draw(self, screen):
#         if self.coordinates and plenty_motion[0] == 1:
#             for i in range(digit):
#                 digit_x = self.left + i * self.cell_size
#                 digit_y = self.top + self.coordinates[1] * self.cell_size
#                 if self.board[i][self.coordinates[1]] == 0 and i != self.coordinates[0]:
#                     pygame.draw.circle(screen, pygame.Color('red'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[i][self.coordinates[1]] = 1
#             for j in range(digit):
#                 digit_x = self.left + self.coordinates[0] * self.cell_size
#                 digit_y = self.top + self.cell_size * j
#                 if self.board[self.coordinates[0]][j] == 0:
#                     pygame.draw.circle(screen, pygame.Color('red'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[self.coordinates[0]][j] = 1
#             plenty_motion[0] = 0
#         elif self.coordinates and plenty_motion[0] == 0:
#             for i in range(digit):
#                 digit_x = self.left + i * self.cell_size
#                 digit_y = self.top + self.coordinates[1] * self.cell_size
#                 if self.board[i][self.coordinates[1]] == 1 and i != self.coordinates[0]:
#                     pygame.draw.circle(screen, pygame.Color('blue'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[i][self.coordinates[1]] = 0
#             for j in range(digit):
#                 digit_x = self.left + self.coordinates[0] * self.cell_size
#                 digit_y = self.top + self.cell_size * j
#                 if self.board[self.coordinates[0]][j] == 1:
#                     pygame.draw.circle(screen, pygame.Color('blue'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[self.coordinates[0]][j] = 0
#             plenty_motion[0] = 1
#
#     def get_click(self, mouse_pos):
#         self.get_cell(mouse_pos)
#         self.on_click(mouse_pos)
#
#     def get_cell(self, mouse_pos):
#         coords_x, coords_y = mouse_pos
#         starts_len = coords_x - self.left
#         starts_height = coords_y - self.top
#         coords_len = starts_len // self.cell_size
#         coords_height = starts_height // self.cell_size
#         if coords_len in range(self.width) and coords_height in range(self.height):
#             return coords_len, coords_height
#         else:
#             return None
#
#     def on_click(self, cell_coords):
#         self.coordinates = self.get_cell(cell_coords)
#
#
# plenty_motion = [1]
#
#
# def main():
#     pygame.init()
#     size = 500, 500
#     screen = pygame.display.set_mode(size)
#     screen.fill('black')
#     pygame.display.set_caption('Инициализация игры')
#
#     board = Board()
#     board.set_view(30)
#     board.color()
#     board.filling(screen)
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 board.get_click(event.pos)
#                 board.draw(screen)
#         board.render(screen)
#         pygame.display.flip()
#     pygame.quit()
#
#
# if __name__ == '__main__':
#     main()
# import os
# import sys
# import pygame
# import random
#
# pygame.init()
# pygame.display.set_caption('Boom them all')
# size = width, height = 500, 500
# screen = pygame.display.set_mode(size)
# fps = 100
# plenty = []
# screen.fill('black')
#
#
# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image
#
#
# clock = pygame.time.Clock()
# all_sprites = pygame.sprite.Group()
#
# # создадим спрайт
# sprite = pygame.sprite.Sprite()
#

#
#     def __init__(self, group):
#         # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
#         # Это очень важно !!!
#         super().__init__(group)
#         self.image = Bomb.image
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(width)
#         self.rect.y = random.randrange(height)
#
#     def update(self, *args):
#         if args and args[0].type == pygame.MOUSEBUTTONUP and \
#                 self.rect.collidepoint(args[0].pos):
#             self.image = self.image_boom
#
#
# screen.fill('black')
# for i in range(50):
#     Bomb(all_sprites)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         screen.fill('black')
#         all_sprites.draw(screen)
#         all_sprites.update(event)
#     pygame.display.flip()
#     clock.tick(fps)
#
# pygame.quit()
# class LittleBell:
#
#     def sound(self):
#         print('ding')
#
#
# class BigBell:
#     def __init__(self):
#         self.numder = 0
#
#     def sound(self):
#         if self.numder % 2 == 0:
#             print('ding')
#             self.numder += 1
#         else:
#             print('dong')
#             self.numder += 1
#
#
# class BellTower:
#     def __init__(self, *args):
#         self.plenty_variation = []
#         if args:
#             for element in args:
#                 self.plenty_variation.append(element)
#
#     def append(self, name):
#         self.plenty_variation.append(name)
#
#     def sound(self):
#         number = 0
#         if len(self.plenty_variation) != 0:
#             for element in self.plenty_variation:
#                 name = element
#                 name.sound()
#                 number += 1
#         print('...')
#
#
# b_tower1 = BellTower(*[LittleBell(), BigBell()])
# b_tower2 = BellTower(*[LittleBell()])
# b_tower3 = BellTower(BigBell())
# b_tower4 = BellTower()
# b_tower1.sound()
# b_tower2.sound()
# b_tower3.sound()
# b_tower4.sound()
# b_tower4.append(BigBell())
# b_tower2.append(LittleBell())
# b_tower2.append(LittleBell())
# b_tower3.append(LittleBell())
# b_tower3.append(BigBell())
# b_tower1.sound()
# b_tower2.sound()
# b_tower3.sound()
# b_tower4.sound()
# b_tower3.append(BigBell())
# b_tower1.append(BigBell())
# b_tower1.append(BigBell())
# b_tower1.append(BigBell())
# b_tower3.append(LittleBell())
# b_tower1.sound()
# b_tower2.sound()
# b_tower3.sound()
# b_tower4.sound()
# digit = input()
# number = input()
# plenty_1 = digit.split()
# plenty_2 = number.split()
# fact_1 = False
# fact_2 = False
# for i in range(int(plenty_1[0]), int(plenty_1[0]) + int(plenty_1[2]) + 1):
#     if i in range(int(plenty_2[0]), int(plenty_2[0]) + int(plenty_2[2]) + 1):
#         fact_1 = True
# for i in range(int(plenty_1[1]), int(plenty_1[1]) + int(plenty_1[3]) + 1):
#     if i in range(int(plenty_2[1]), int(plenty_2[1]) + int(plenty_2[3]) + 1):
#         fact_2 = True
# if fact_1 and fact_2:
#     print('YES')
# else:
#     print('NO')
# import os
# import sys
# import pygame
#
# pygame.init()
# pygame.display.set_caption('Машинка')
# size = width, height = 600, 95
# screen = pygame.display.set_mode(size)
# fps = 70
# plenty = []
# screen.fill('white')
#
#
# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image
#
#
# clock = pygame.time.Clock()
# all_sprites = pygame.sprite.Group()
# sprite = pygame.sprite.Sprite()
# plenty_queue = [0]
#

#
#     def __init__(self, group):
#         super().__init__(group)
#         self.image = Car.image
#         self.rect = self.image.get_rect()
#         self.rect.x = 0
#         self.rect.y = 0
#
#     def update(self):
#         if self.rect.x < 450 and plenty_queue[0] == 0:
#             self.rect = self.rect.move(2, 0)
#         elif self.rect.x >= 450 and plenty_queue[0] == 0:
#             self.image = pygame.transform.flip(self.image, True, False)
#             self.rect = self.rect.move(-2, 0)
#             plenty_queue[0] = 1
#         elif self.rect.x > 0 and plenty_queue[0] == 1:
#             self.rect = self.rect.move(-2, 0)
#         elif self.rect.x <= 0 and plenty_queue[0] == 1:
#             self.image = pygame.transform.flip(self.image, True, False)
#             self.rect = self.rect.move(2, 0)
#             plenty_queue[0] = 0
#
#
# screen.fill('white')
# Car(all_sprites)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill('white')
#     all_sprites.draw(screen)
#     all_sprites.update()
#     pygame.display.flip()
#     clock.tick(fps)
#
# pygame.quit()
#
# import os
# import sys
# import pygame
#
# pygame.init()
# pygame.display.set_caption('Game over')
# size = width, height = 600, 300
# screen = pygame.display.set_mode(size)
# fps = 70
# plenty = []
# screen.fill('blue')
#
#
# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image
#
#
# clock = pygame.time.Clock()
# all_sprites = pygame.sprite.Group()
# sprite = pygame.sprite.Sprite()
# plenty_queue = [0]
#

#     def __init__(self, group):
#         super().__init__(group)
#         self.image = Car.image
#         self.rect = self.image.get_rect()
#         self.rect.x = -600
#         self.rect.y = 0
#
#     def update(self):
#         if self.rect.x < 0 and plenty_queue[0] == 0:
#             self.rect = self.rect.move(5, 0)
#
#
# screen.fill('blue')
# Car(all_sprites)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill('blue')
#     all_sprites.draw(screen)
#     all_sprites.update()
#     pygame.display.flip()
#     clock.tick(fps)
#
# pygame.quit()
# import sys
# import pygame
# import os
#
# pygame.init()
# pygame.display.set_caption('Платформы')
# size = width, height = 500, 500
# screen = pygame.display.set_mode(size)
# running = True
# screen.fill('black')
# fps = 60
# clock = pygame.time.Clock()
# all_sprites = pygame.sprite.Group()
#
#
# class Square(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         super().__init__(all_sprites)
#         self.image = pygame.Surface([width, height])
#         self.image.fill(pygame.Color('white'))
#         pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect(pos[0], pos[1], 10, 10))
#         self.rect = self.image.get_rect()
#         print(True)
#
#     def update(self):
#         self.rect = self.rect.move(0, 1)
#
#
# # class Platform(pygame.sprite.Sprite):
# #     def __init__(self, pos):
# #         super().__init__(all_sprites)
# #         self.image = pygame.draw.line(screen, pygame.Color('gray'), [pos[0], pos[1]], [pos[0] + 30, pos[1]], 5)
# #         self.image = Platform.image
# #         self.rect = self.image.get_rect()
# #         self.mask = pygame.mask.from_surface(self.image)
# #         self.rect.bottom = height
#
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             screen.fill('white')
#             Square(event.pos)
#             # Platform(event.pos)
#             all_sprites.draw(screen)
#             all_sprites.update()
#     screen.fill('white')
#     all_sprites.draw(screen)
#     all_sprites.update()
#     clock.tick(fps)
#     pygame.display.flip()
#
# pygame.quit()

#
# import pygame
# import random
#
# # GLOBAL VARIABLES
# COLOR = (255, 100, 98)
# SURFACE_COLOR = (167, 255, 100)
# WIDTH = 500
# HEIGHT = 500
#
#
# # Object class
# class Sprite(pygame.sprite.Sprite):
#     def __init__(self, color, height, width):
#         super().__init__()
#
#         self.image = pygame.Surface([width, height])
#         self.image.fill(SURFACE_COLOR)
#         self.image.set_colorkey(COLOR)
#
#         pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
#
#         self.rect = self.image.get_rect()
#
#
# pygame.init()
#
# RED = (255, 0, 0)
#
# size = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Creating Sprite")
#
# all_sprites_list = pygame.sprite.Group()
#
# object_ = Sprite(RED, 20, 30)
# object_.rect.x = 200
# object_.rect.y = 300
#
# all_sprites_list.add(object_)
#
# exit = True
# clock = pygame.time.Clock()
#
# while exit:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit = False
#
#     all_sprites_list.update()
#     screen.fill(SURFACE_COLOR)
#     all_sprites_list.draw(screen)
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
# import pygame
#
# all_sprites = pygame.sprite.Group()
# lines = pygame.sprite.Group()
#
# need = False
#
#
# class Sprite(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         super().__init__(all_sprites)
#         self.image = pygame.Surface([20, 20])
#         self.image.fill((0, 0, 255))
#         self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
#         self.x = pos[0]
#         self.y = pos[1]
#
#     def update(self):
#         if not pygame.sprite.spritecollideany(self, lines):
#             self.y += 1
#             self.rect = self.rect.move(0, 1)
#             if len(plenty_copy) != 0:
#                 plenty_copy[1] = self.y
#                 plenty_copy[0] = self.x
#
#     def right(self):
#         if pygame.sprite.spritecollideany(self, lines):
#             self.x += 10
#             self.rect = self.rect.move(10, 0)
#             if len(plenty_copy) != 0:
#                 plenty_copy[0] = self.x
#                 plenty_copy[1] = self.y
#
#     def left(self):
#         if pygame.sprite.spritecollideany(self, lines):
#             self.x -= 10
#             self.rect = self.rect.move(-10, 0)
#             if len(plenty_copy) != 0:
#                 plenty_copy[0] = self.x
#                 plenty_copy[1] = self.y
#
#
# class Line(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         super().__init__(all_sprites)
#         self.add(lines)
#         self.image = pygame.Surface([70, 10])
#         self.image.fill(pygame.Color('grey'))
#         self.rect = pygame.Rect(pos[0], pos[1], 70, 10)
#
#
# pygame.init()
# size = (500, 500)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Платформы")
#
# running = True
# clock = pygame.time.Clock()
# need = True
# plenty = []
# plenty_copy = []
# coord_line = []
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 3:
#                 if need:
#                     Sprite(event.pos)
#                     screen.fill(pygame.Color('white'))
#                     all_sprites.update()
#                     all_sprites.draw(screen)
#                     x = event.pos[0]
#                     y = event.pos[1]
#                     plenty.append(x)
#                     plenty.append(y)
#                     plenty_copy = plenty.copy()
#                     need = False
#                 else:
#                     all_sprites = pygame.sprite.Group()
#                     Sprite((event.pos[0], event.pos[1]))
#                     plenty.clear()
#                     plenty.append(event.pos[0])
#                     plenty.append(event.pos[1])
#                     plenty_copy = plenty.copy()
#                     screen.fill(pygame.Color('black'))
#                     for element in coord_line:
#                         Line(element)
#                     all_sprites.update()
#                     all_sprites.draw(screen)
#             elif event.button == 1:
#                 Line(event.pos)
#                 coord_line.append([event.pos[0], event.pos[1]])
#                 screen.fill(pygame.Color('black'))
#                 all_sprites.update()
#                 all_sprites.draw(screen)
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 all_sprites = pygame.sprite.Group()
#                 name = Sprite((plenty_copy[0], plenty_copy[1]))
#                 name.right()
#                 for element in coord_line:
#                     Line(element)
#                 screen.fill(pygame.Color('black'))
#                 all_sprites.update()
#                 all_sprites.draw(screen)
#             elif event.key == pygame.K_LEFT:
#                 all_sprites = pygame.sprite.Group()
#                 name = Sprite((plenty_copy[0], plenty_copy[1]))
#                 name.left()
#                 for element in coord_line:
#                     Line(element)
#                 screen.fill(pygame.Color('black'))
#                 all_sprites.update()
#                 all_sprites.draw(screen)
#     screen.fill(pygame.Color('black'))
#     all_sprites.update()
#     all_sprites.draw(screen)
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
# import pygame
# import random
#
# digit = int(input())
#
#
# class Board:
#     def __init__(self):
#         self.left = 10
#         self.top = 10
#         self.cell_size = 30
#
#     def set_view(self, cell_size):
#         self.cell_size = cell_size
#         self.width = cell_size * digit
#         self.height = cell_size * digit
#         self.board = [[0] * digit for _ in range(digit)]
#
#     def render(self, screen):
#         for i in range(0, digit):
#             for j in range(0, digit):
#                 pygame.draw.rect(screen, pygame.Color('white'),
#                                  (i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
#                                   self.cell_size),
#                                  1)
#
#     def color(self):
#         for i in range(digit):
#             for j in range(digit):
#                 number = random.randrange(0, 2)
#                 self.board[i][j] = number
#
#     def filling(self, screen):
#         for i in range(0, digit):
#             for j in range(0, digit):
#                 if self.board[i][j] == 1:
#                     pygame.draw.circle(screen, pygame.Color('red'),
#                                        (i * self.cell_size + self.left + 0.5 * self.cell_size,
#                                         j * self.cell_size + self.top + 0.5 * self.cell_size), self.cell_size / 2 - 1)
#                 elif self.board[i][j] == 0:
#                     pygame.draw.circle(screen, pygame.Color('blue'),
#                                        (i * self.cell_size + self.left + 0.5 * self.cell_size,
#                                         j * self.cell_size + self.top + 0.5 * self.cell_size), self.cell_size / 2 - 1)
#
#     def draw(self, screen):
#         if self.coordinates and plenty_motion[0] == 1 and self.board[self.coordinates[0]][self.coordinates[1]] == 1:
#             for i in range(digit):
#                 digit_x = self.left + i * self.cell_size
#                 digit_y = self.top + self.coordinates[1] * self.cell_size
#                 if self.board[i][self.coordinates[1]] == 0 and i != self.coordinates[0]:
#                     pygame.draw.circle(screen, pygame.Color('red'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[i][self.coordinates[1]] = 1
#             for j in range(digit):
#                 digit_x = self.left + self.coordinates[0] * self.cell_size
#                 digit_y = self.top + self.cell_size * j
#                 if self.board[self.coordinates[0]][j] == 0:
#                     pygame.draw.circle(screen, pygame.Color('red'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[self.coordinates[0]][j] = 1
#             plenty_motion[0] = 0
#         elif self.coordinates and plenty_motion[0] == 0 and self.board[self.coordinates[0]][self.coordinates[1]] == 0:
#             for i in range(digit):
#                 digit_x = self.left + i * self.cell_size
#                 digit_y = self.top + self.coordinates[1] * self.cell_size
#                 if self.board[i][self.coordinates[1]] == 1 and i != self.coordinates[0]:
#                     pygame.draw.circle(screen, pygame.Color('blue'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[i][self.coordinates[1]] = 0
#             for j in range(digit):
#                 digit_x = self.left + self.coordinates[0] * self.cell_size
#                 digit_y = self.top + self.cell_size * j
#                 if self.board[self.coordinates[0]][j] == 1:
#                     pygame.draw.circle(screen, pygame.Color('blue'),
#                                        (digit_x + self.cell_size / 2, digit_y + self.cell_size / 2),
#                                        self.cell_size / 2 - 1)
#                     self.board[self.coordinates[0]][j] = 0
#             plenty_motion[0] = 1
#
#     def get_click(self, mouse_pos):
#         self.get_cell(mouse_pos)
#         self.on_click(mouse_pos)
#
#     def get_cell(self, mouse_pos):
#         coords_x, coords_y = mouse_pos
#         starts_len = coords_x - self.left
#         starts_height = coords_y - self.top
#         coords_len = starts_len // self.cell_size
#         coords_height = starts_height // self.cell_size
#         if coords_len in range(self.width) and coords_height in range(self.height):
#             return coords_len, coords_height
#         else:
#             return None
#
#     def on_click(self, cell_coords):
#         self.coordinates = self.get_cell(cell_coords)
#
#
# plenty_motion = [1]
#
#
# def main():
#     pygame.init()
#     size = 500, 500
#     screen = pygame.display.set_mode(size)
#     screen.fill('black')
#     pygame.display.set_caption('Инициализация игры')
#
#     board = Board()
#     board.set_view(30)
#     board.color()
#     board.filling(screen)
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 board.get_click(event.pos)
#                 board.draw(screen)
#         board.render(screen)
#         pygame.display.flip()
#     pygame.quit()
#
#
# if __name__ == '__main__':
# #     main()
# import os
# import sys
# import pygame
# import random
#
# pygame.init()
# pygame.display.set_caption('Boom them all')
# size = width, height = 500, 500
# screen = pygame.display.set_mode(size)
# fps = 100
# plenty = []
# screen.fill('black')
#
#
# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image
#
#
# clock = pygame.time.Clock()
# all_sprites = pygame.sprite.Group()
# sprite = pygame.sprite.Sprite()
#
#

#
#     def __init__(self, group):
#         super().__init__(group)
#         self.image = Bomb.image
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(55, width - 55)
#         self.rect.y = random.randrange(55, height - 55)
#
#     def update(self, *args):
#         if args and args[0].type == pygame.MOUSEBUTTONUP and \
#                 self.rect.collidepoint(args[0].pos):
#             self.image = self.image_boom
#
#
# screen.fill('black')
# for i in range(50):
#     Bomb(all_sprites)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         screen.fill('black')
#         all_sprites.draw(screen)
#         all_sprites.update(event)
#     pygame.display.flip()
#     clock.tick(fps)
# pygame.quit()
# import pygame
#
# all_sprites = pygame.sprite.Group()
# lines = pygame.sprite.Group()
# vertical_lines = pygame.sprite.Group()
#
# need = False
#
#
# class Sprite(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         super().__init__(all_sprites)
#         self.image = pygame.Surface([20, 20])
#         self.image.fill((0, 0, 255))
#         self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
#         self.x = pos[0]
#         self.y = pos[1]
#
#     def update(self):
#         if not pygame.sprite.spritecollideany(self, lines) and not pygame.sprite.spritecollideany(self, vertical_lines):
#             self.y += 1
#             self.rect = self.rect.move(0, 1)
#             if len(plenty_copy) != 0:
#                 plenty_copy[1] = self.y
#                 plenty_copy[0] = self.x
#
#     def right(self):
#         if pygame.sprite.spritecollideany(self, lines) or pygame.sprite.spritecollideany(self, vertical_lines):
#             self.x += 10
#             self.rect = self.rect.move(10, 0)
#             if len(plenty_copy) != 0:
#                 plenty_copy[0] = self.x
#                 plenty_copy[1] = self.y
#
#     def left(self):
#         if pygame.sprite.spritecollideany(self, lines) or pygame.sprite.spritecollideany(self, vertical_lines):
#             self.x -= 10
#             self.rect = self.rect.move(-10, 0)
#             if len(plenty_copy) != 0:
#                 plenty_copy[0] = self.x
#                 plenty_copy[1] = self.y
#
#     def up(self):
#         if pygame.sprite.spritecollideany(self, vertical_lines):
#             self.y -= 10
#             self.rect = self.rect.move(0, -10)
#             if len(plenty_copy) != 0:
#                 plenty_copy[0] = self.x
#                 plenty_copy[1] = self.y
#
#     def down(self):
#         if pygame.sprite.spritecollideany(self, vertical_lines):
#             self.y += 10
#             self.rect = self.rect.move(0, 10)
#             if len(plenty_copy) != 0:
#                 plenty_copy[0] = self.x
#                 plenty_copy[1] = self.y
#
#
# class Line(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         super().__init__(all_sprites)
#         self.add(lines)
#         self.image = pygame.Surface([70, 10])
#         self.image.fill(pygame.Color('grey'))
#         self.rect = pygame.Rect(pos[0], pos[1], 70, 10)
#
#
# class Vertical_line(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         super().__init__(all_sprites)
#         self.add(vertical_lines)
#         self.image = pygame.Surface([10, 70])
#         self.image.fill(pygame.Color('red'))
#         self.rect = pygame.Rect(pos[0], pos[1], 10, 70)
#
#
# pygame.init()
# size = (500, 500)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Платформы")
#
# running = True
# clock = pygame.time.Clock()
# need = True
# plenty = []
# plenty_copy = []
# coord_line = []
# coord_vertical_line = []
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 3:
#                 if need:
#                     Sprite(event.pos)
#                     screen.fill(pygame.Color('white'))
#                     all_sprites.update()
#                     all_sprites.draw(screen)
#                     x = event.pos[0]
#                     y = event.pos[1]
#                     plenty.append(x)
#                     plenty.append(y)
#                     plenty_copy = plenty.copy()
#                     need = False
#                 else:
#                     all_sprites = pygame.sprite.Group()
#                     Sprite((event.pos[0], event.pos[1]))
#                     plenty.clear()
#                     plenty.append(event.pos[0])
#                     plenty.append(event.pos[1])
#                     plenty_copy = plenty.copy()
#                     screen.fill(pygame.Color('black'))
#                     for element in coord_line:
#                         Line(element)
#                     for parts in coord_vertical_line:
#                         Vertical_line(parts)
#                     all_sprites.update()
#                     all_sprites.draw(screen)
#             elif event.button == 1:
#                 if pygame.key.get_mods() & pygame.KMOD_LCTRL:
#                     Vertical_line(event.pos)
#                     coord_vertical_line.append([event.pos[0], event.pos[1]])
#                     screen.fill(pygame.Color('black'))
#                     all_sprites.update()
#                     all_sprites.draw(screen)
#                 else:
#                     Line(event.pos)
#                     coord_line.append([event.pos[0], event.pos[1]])
#                     screen.fill(pygame.Color('black'))
#                     all_sprites.update()
#                     all_sprites.draw(screen)
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 all_sprites = pygame.sprite.Group()
#                 name = Sprite((plenty_copy[0], plenty_copy[1]))
#                 name.right()
#                 for element in coord_line:
#                     Line(element)
#                 for parts in coord_vertical_line:
#                     Vertical_line(parts)
#                 screen.fill(pygame.Color('black'))
#                 all_sprites.update()
#                 all_sprites.draw(screen)
#             elif event.key == pygame.K_LEFT:
#                 all_sprites = pygame.sprite.Group()
#                 name = Sprite((plenty_copy[0], plenty_copy[1]))
#                 name.left()
#                 for element in coord_line:
#                     Line(element)
#                 for parts in coord_vertical_line:
#                     Vertical_line(parts)
#                 screen.fill(pygame.Color('black'))
#                 all_sprites.update()
#                 all_sprites.draw(screen)
#             elif event.key == pygame.K_DOWN:
#                 all_sprites = pygame.sprite.Group()
#                 name = Sprite((plenty_copy[0], plenty_copy[1]))
#                 name.down()
#                 for element in coord_line:
#                     Line(element)
#                 for parts in coord_vertical_line:
#                     Vertical_line(parts)
#                 screen.fill(pygame.Color('black'))
#                 all_sprites.update()
#                 all_sprites.draw(screen)
#             elif event.key == pygame.K_UP:
#                 all_sprites = pygame.sprite.Group()
#                 name = Sprite((plenty_copy[0], plenty_copy[1]))
#                 name.up()
#                 for element in coord_line:
#                     Line(element)
#                 for parts in coord_vertical_line:
#                     Vertical_line(parts)
#                 screen.fill(pygame.Color('black'))
#                 all_sprites.update()
#                 all_sprites.draw(screen)
#
#     screen.fill(pygame.Color('black'))
#     all_sprites.update()
#     all_sprites.draw(screen)
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
# from yandex_testing_lesson import is_palindrome(data)
#
#
# def test_reverse():
#     # Список тестов
#     # Каждый тест — это пара (входное значение, ожидаемое выходное значение)
#     test_data = (
#         # неправильный тип входного аргумента, ни с чем не будем сравнивать
#         (42, None),
#         # тоже неправильный входной аргумент, но он "похож" на строку
#         # (можно итерироваться и брать срезы)
#         (['a', 'b', 'c'], None),
#         # "граничный" случай — пустая строка
#         ('', ''),
#         # "особый" случай — строка, которая не меняется при разворачивании
#         ('aba', 'aba'),
#         # ещё один "особый" и почти "граничный" случай
#         ('a', 'a'),
#         # "обычный" случай
#         ('abc', 'cba'),
#     )
#
import os
import sys
import pygame


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


player = None


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = pos_x, pos_y

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)


def move(hero, movevent):
    x, y = hero.pos
    if movevent == 'up':
        if y > 0 and level_map[y - 1][x] == '.':
            hero.move(x, y - 1)
    elif movevent == 'down':
        if y < max_y - 1 and level_map[y + 1][x] == '.':
            hero.move(x, y + 1)
    elif movevent == 'left':
        if x > 0 and level_map[y][x - 1] == '.':
            hero.move(x - 1, y)
    elif movevent == 'right':
        if x > 0 and level_map[y][x + 1] == '.':
            hero.move(x + 1, y)


pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Платформы")
FPS = 50
running = True
clock = pygame.time.Clock()
tile_images = {
    'wall': load_image('box.jpeg', -1),
    'empty': load_image('grass.jpeg', -1)
}
player_image = load_image('mario.png', -1)

tile_width = tile_height = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('foto.jpeg'), (size))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
level_map = load_level('map.map')
hero, max_x, max_y = generate_level(level_map)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(hero, 'up')
            elif event.key == pygame.K_DOWN:
                move(hero, 'down')
            elif event.key == pygame.K_RIGHT:
                move(hero, 'right')
            elif event.key == pygame.K_LEFT:
                move(hero, 'left')

    screen.fill('black')
    tiles_group.draw(screen)
    player_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
