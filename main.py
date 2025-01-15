# import sys
#
# import pygame
#
#
# def main():
#     pygame.init()
#     size = (400, 400)
#     screen = pygame.display.set_mode(size)
#
#     draw(screen)
#
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen):
#     color = pygame.Color('yellow')
#
#
# if __name__ == '__main__':
#     sys.exit(main())

# import sys
# import pygame
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Крест')
#     try:
#         size = width, height = [int(x) for x in input().split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     screen = pygame.display.set_mode(size)
#     draw(screen, width, height)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, widht, height):
#     color = pygame.Color('white')
#     points = [(0, 0), (widht, height)]
#     pygame.draw.line(screen, color, *points, width=5)
#     points = [(0, height), (widht, 0)]
#     pygame.draw.line(screen, color, *points, width=5)
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import sys
# import pygame
#
# COLORS = [pygame.Color('red'), pygame.Color('green'), pygame.Color('blue')]
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Прямоугольник')
#     try:
#         leight, heigth = [int(x) for x in input().split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     size = leight, heigth
#     screen = pygame.display.set_mode(size)
#     draw(screen, leight, heigth)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, leight, height):
#     color = pygame.Color('red')
#     pygame.draw.rect(screen, color, (1, 1, leight - 1, height - 1), width=0)
#
#
# if __name__ == '__main__':
#     sys.exit(main())

# import sys
# import pygame
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Шахматная клетка')
#     try:
#         leight, counter = [int(x) for x in input().split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     size = leight, leight
#     screen = pygame.display.set_mode(size)
#     draw(screen, leight, counter)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, leight, counter):
#     color_1 = pygame.Color('white')
# #     color_2 = pygame.Color('black')
#     row = 0
#     for j in range(counter):
#         number = 0
#         row += 1
#         for i in range(counter):
#             if j % 2 == 0:
#                 if i % 2 == 0:
#                     pygame.draw.rect(screen, color_2, (
#                         number * (leight // counter), leight // counter * (counter - row), leight // counter,
#                         leight // counter), width=0)
#                     number += 1
#                 else:
#                     pygame.draw.rect(screen, color_1, (
#                         number * (leight // counter), leight // counter * (counter - row), leight // counter,
#                         leight // counter), width=0)
#                     number += 1
#             else:
#                 if i % 2 == 0:
#                     pygame.draw.rect(screen, color_1, (
#                         number * (leight // counter), leight // counter * (counter - row), leight // counter,
#                         leight // counter), width=0)
#                     number += 1
#                 else:
#                     pygame.draw.rect(screen, color_2, (
#                         number * (leight // counter), leight // counter * (counter - row), leight // counter,
#                         leight // counter), width=0)
#                     number += 1
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import sys
# import pygame
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Ромбики')
#     try:
#         n = int(input())
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     size = 300, 300
#     screen = pygame.display.set_mode(size)
#     screen.fill(pygame.Color('yellow'))
#     draw(screen, n)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, digit):
#     color = pygame.Color('orange')
#     marker = -digit
#     number = 0
#     for j in range(300 // digit):
#         marker += digit
#         number = 0
#         for i in range(300 // digit):
#             if number + digit <= 300:
#                 pygame.draw.polygon(screen, color,
#                                     [(number + 0, marker + digit * 0.5),
#                                      (number + (digit * 0.5), marker),
#                                      (number + digit, marker + digit * 0.5),
#                                      (number + (digit * 0.5), marker + digit)], 0)
#             number += digit
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import sys
# import pygame
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Ромбики')
#     try:
#         n = int(input())
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     size = 300, 300
#     screen = pygame.display.set_mode(size)
#     screen.fill(pygame.Color('black'))
#     draw(screen, n)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, digit):
#     color = pygame.Color('white')
#     pygame.draw.circle(screen, color,
#                        (150, 150), 150, width=1)
#     number = 150 / digit
#     coords_y1 = 135
#     coords_y2 = 30
#     for i in range(digit - 1):
#         pygame.draw.ellipse(screen, color, (0, coords_y1, 300, coords_y2), width=1)
#         coords_y1 -= number
#         coords_y2 += number * 2
#     coords_x1 = 135
#     coords_x2 = 30
#     for j in range(digit - 1):
#         pygame.draw.ellipse(screen, color, (coords_x1, 0, coords_x2, 300), width=1)
#         coords_x1 -= number
#         coords_x2 += number * 2
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import pygame
#
# if __name__ == '__main__':
#     pygame.init()
#     pygame.display.set_caption('Шарики')
#     size = width, height = 600, 600
#     screen = pygame.display.set_mode(size)
#     running = True
#     draw = False
#     fps = 60
#     plus = 40000
#     plenty_coords = []
#     direction = []
#     screen.fill('black')
#     clock = pygame.time.Clock()
#     color_circle = pygame.Color('yellow')
#     pygame.time.set_timer(plus, 10)
#     cicrle_radius = 10
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 screen.fill('black')
#                 draw = True
#                 cicrle_radius = 10
#                 x_coords, y_coords = event.pos
#                 plenty_time = []
#                 orientation = []
#                 plenty_time.append(x_coords)
#                 plenty_time.append(y_coords)
#                 orientation.append(-1)
#                 orientation.append(-1)
#                 direction.append(orientation)
#                 plenty_coords.append(plenty_time)
#                 pygame.draw.circle(screen, (pygame.Color('red')), (x_coords, y_coords), cicrle_radius)
#             if event.type == plus and draw:
#                 screen.fill('black')
#                 number = 0
#                 for element in plenty_coords:
#                     if 10 <= element[0] <= 590 and 10 <= element[1] <= 590:
#                         plenty_coords[number][0] = plenty_coords[number][0] + direction[number][0] * 1
#                         plenty_coords[number][1] = plenty_coords[number][1] + direction[number][1] * 1
#                         pygame.draw.circle(screen, (pygame.Color('yellow')), (element[0], element[1]), cicrle_radius)
#                         number += 1
#                     elif element[0] >= 590:
#                         direction[number][0] = -1
#                         plenty_coords[number][0] = plenty_coords[number][0] + direction[number][0] * 1
#                         plenty_coords[number][1] = plenty_coords[number][1] + direction[number][1] * 1
#                         pygame.draw.circle(screen, (pygame.Color('white')), (element[0], element[1]), cicrle_radius)
#                         number += 1
#                     elif element[1] >= 590:
#                         direction[number][1] = -1
#                         plenty_coords[number][0] = plenty_coords[number][0] + direction[number][0] * 1
#                         plenty_coords[number][1] = plenty_coords[number][1] + direction[number][1] * 1
#                         pygame.draw.circle(screen, (pygame.Color('brown')), (element[0], element[1]), cicrle_radius)
#                         number += 1
#                     elif element[0] <= 10:
#                         direction[number][0] = 1
#                         plenty_coords[number][0] = plenty_coords[number][0] + direction[number][0] * 1
#                         plenty_coords[number][1] = plenty_coords[number][1] + direction[number][1] * 1
#                         pygame.draw.circle(screen, (pygame.Color('white')), (element[0], element[1]), cicrle_radius)
#                         number += 1
#                     elif element[1] <= 10:
#                         direction[number][1] = 1
#                         plenty_coords[number][0] = plenty_coords[number][0] + direction[number][0] * 1
#                         plenty_coords[number][1] = plenty_coords[number][1] + direction[number][1] * 1
#                         pygame.draw.circle(screen, (pygame.Color('white')), (element[0], element[1]), cicrle_radius)
#                         number += 1
#         pygame.display.flip()
#         clock.tick(fps)
#     pygame.quit()
# import pygame
#
# if __name__ == '__main__':
#     pygame.init()
#     pygame.display.set_caption('Перетаскивание')
#     size = width, height = 300, 300
#     screen = pygame.display.set_mode(size)
#     running = True
#     draw = False
#     fps = 60
#     plus = 40000
#     screen.fill('black')
#     clock = pygame.time.Clock()
#     pygame.time.set_timer(plus, 10)
#     plenty = []
#     plenty.append(0)
#     plenty.append(0)
#     coords_square = []
#     coords_square.append(0)
#     coords_square.append(0)
#     number = 2
#     while running:
#         pygame.draw.rect(screen, (pygame.Color('green')), (coords_square[0], coords_square[1], 100, 100), 0)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if number % 2 == 0 and event.button == 1:
#                     coords_x, coords_y = event.pos
#                     if coords_x in range(coords_square[0], coords_square[0] + 100) and coords_y in range(
#                             coords_square[1], coords_square[1] + 100):
#                         plenty[0] = coords_x - coords_square[0]
#                         plenty[1] = coords_y - coords_square[1]
#                         draw = True
#                         number += 1
#                 else:
#                     plenty[0] = 0
#                     plenty[1] = 0
#                     draw = False
#                     number += 1
#                     pygame.draw.rect(screen, (pygame.Color('green')), (coords_square[0], coords_square[1], 100, 100), 0)
#             if event.type == pygame.MOUSEMOTION and draw:
#                 screen.fill('black')
#                 coordinates_x, coordinates_y = event.pos
#                 pygame.draw.rect(screen, (pygame.Color('green')),
#                                  (coordinates_x - plenty[0], coordinates_y - plenty[1], 100, 100), 0)
#                 coords_square[0] = coordinates_x - plenty[0]
#                 coords_square[1] = coordinates_y - plenty[1]
#         pygame.display.flip()
#         clock.tick(fps)
#     pygame.display.flip()
#     clock.tick(fps)
# pygame.quit()
# import sys
#
# from random import randrange
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt6.QtWidgets import QLCDNumber, QLabel
# plenty = []
#
#
# class NimStrikesBack(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 300)
#         self.setWindowTitle('Ним наносит ответный удар')
#         self.result_label = QLabel(self)
#         self.result_label.move(20, 30)
#         self.result_label.setText('                                                                              ')
#         self.X = randrange(100)
#         self.Y = randrange(100)
#         self.Z = randrange(100)
#         self.btnp = QPushButton(f'+{str(self.Y)}', self)
#         self.btnp.move(20, 60)
#         self.btnp.clicked.connect(self.plus_click)
#
#         self.btnm = QPushButton(f'-{str(self.Z)}', self)
#         self.btnm.move(200, 60)
#         self.btnm.clicked.connect(self.minus_digit)
#         self.play = QLabel(self)
#         self.play.setText('Осталось ходов')
#         self.play.move(20, 100)
#         self.digit = QLabel(self)
#         self.digit.setText('Текущее число')
#         self.digit.move(20, 130)
#
#         self.count = 10
#         self.LCD_count = QLCDNumber(self)
#         self.LCD_count.move(200, 100)
#         self.LCD_count.display(self.count)
#         self.LCD_count_2 = QLCDNumber(self)
#         self.LCD_count_2.move(200, 130)
#         self.LCD_count_2.display(self.X)
#
#     def starts(self):
#         self.X = 0
#         self.X = randrange(100)
#         self.new_Y = randrange(100)
#         self.new_Z = randrange(100)
#         self.count = 10
#         self.LCD_count.display(self.count)
#         self.LCD_count_2.display(self.X)
#         self.btnm.setText(f'-{self.new_Z}')
#         self.btnp.setText(f'+{self.new_Y}')
#
#     def plus_click(self):
#         self.result_label.setText('                                                                            ')
#         self.count -= 1
#         self.LCD_count.display(self.count)
#         self.X += int(self.btnp.text())
#         self.LCD_count_2.display(self.X)
#         if self.X == 0 and self.count >= 0:
#             self.result_label.setText('Вы победили, начинаем новую игру')
#             self.starts()
#         elif self.count == 0:
#             self.result_label.setText('Вы проиграли, начинаем новую игру')
#             self.starts()
#
#     def minus_digit(self):
#         self.result_label.setText('                                                                            ')
#         self.count -= 1
#         self.LCD_count.display(self.count)
#         self.X += int(self.btnm.text())
#         self.LCD_count_2.display(self.X)
#         if self.X == 0 and self.count >= 0:
#             self.result_label.setText('Вы победили, начинаем новую игру')
#             self.starts()
#         elif self.count == 0 and self.X != 0:
#             self.result_label.setText('Вы проиграли, начинаем новую игру')
#             self.starts()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = NimStrikesBack()
#     ex.show()
#     sys.exit(app.exec())
# import sys
# import pygame
#
# COLORS = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('green'),]
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Крест')
#     try:
#         size_circle, number = [int(x) for x in input().split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     size = (2 * size_circle * number, 2 * size_circle * number)
#     screen = pygame.display.set_mode(size)
#     draw(screen, size_circle, number)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, size_circle, number):
#     circle_radius = size_circle * number
#     circle_position = (circle_radius, circle_radius)
#     digit = 0
#     while number > 0:
#         pygame.draw.circle(screen, COLORS[digit % 3], circle_position, circle_radius, width=0)
#         circle_radius -= size_circle
#         number -= 1
#         digit += 1
#
#
# if __name__ == '__main__':
#     sys.exit(main())
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
#
# def main():
#     pygame.init()
#     size = 500, 500
#     screen = pygame.display.set_mode(size)
#     screen.fill('black')
#     pygame.display.set_caption('Инициализация игры')
#
#     board = Board(5, 5)
#     board.set_view(40, 60, 55)
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
# import sys
#
# from random import randrange
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt6.QtWidgets import QLCDNumber, QLabel, QLineEdit
# plenty = []
#
#
# class NimStrikesBack(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 300)
#         self.setWindowTitle('Заказ в Макдональдсе — 2')
#         self.result_label = QLabel(self)
#
#         self.result_label.move(20, 30)
#         self.result_label.setText('                                                                              ')
#         self.X = randrange(100)
#         self.Y = randrange(100)
#         self.Z = randrange(100)
#         self.btnp = QPushButton(f'+{str(self.Y)}', self)
#         self.btnp.move(20, 60)
#         self.btnp.clicked.connect(self.plus_click)
#
#         self.btnm = QPushButton(f'-{str(self.Z)}', self)
#         self.btnm.move(200, 60)
#         self.btnm.clicked.connect(self.minus_digit)
#         self.play = QLabel(self)
#         self.play.setText('Осталось ходов')
#         self.play.move(20, 100)
#         self.digit = QLabel(self)
#         self.digit.setText('Текущее число')
#         self.digit.move(20, 130)
#
#         self.count = 10
#         self.LCD_count = QLCDNumber(self)
#         self.LCD_count.move(200, 100)
#         self.LCD_count.display(self.count)
#         self.LCD_count_2 = QLCDNumber(self)
#         self.LCD_count_2.move(200, 130)
#         self.LCD_count_2.display(self.X)
#
#     def starts(self):
#         self.X = 0
#         self.X = randrange(100)
#         self.new_Y = randrange(100)
#         self.new_Z = randrange(100)
#         self.count = 10
#         self.LCD_count.display(self.count)
#         self.LCD_count_2.display(self.X)
#         self.btnm.setText(f'-{self.new_Z}')
#         self.btnp.setText(f'+{self.new_Y}')
#
#     def plus_click(self):
#         self.result_label.setText('                                                                            ')
#         self.count -= 1
#         self.LCD_count.display(self.count)
#         self.X += int(self.btnp.text())
#         self.LCD_count_2.display(self.X)
#         if self.X == 0 and self.count >= 0:
#             self.result_label.setText('Вы победили, начинаем новую игру')
#             self.starts()
#         elif self.count == 0:
#             self.result_label.setText('Вы проиграли, начинаем новую игру')
#             self.starts()
#
#     def minus_digit(self):
#         self.result_label.setText('                                                                            ')
#         self.count -= 1
#         self.LCD_count.display(self.count)
#         self.X += int(self.btnm.text())
#         self.LCD_count_2.display(self.X)
#         if self.X == 0 and self.count >= 0:
#             self.result_label.setText('Вы победили, начинаем новую игру')
#             self.starts()
#         elif self.count == 0 and self.X != 0:
#             self.result_label.setText('Вы проиграли, начинаем новую игру')
#             self.starts()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = NimStrikesBack()
#     ex.show()
# #     sys.exit(app.exec())
# f = open("pipes", encoding="utf8")
# lines = f.readlines()
# plenty = []
# for i in range(len(lines)):
#     plenty.append(lines[i].rstrip())
# digit = plenty[-1]
# strong = []
# for element in digit.split():
#     strong.append(float(plenty[int(element) - 1]) * 60)
# number = 0
# for element in strong:
#     number += 1 / element
# word = open("time.txt", 'w')
# word.write(str(1 / number))
# word.close()
# f.close()
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
#             if self.board[self.coordinates[0]][self.coordinates[1]] == 0:
#                 pygame.draw.rect(screen, pygame.Color('red'),
#                                  (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                 self.board[self.coordinates[0]][self.coordinates[1]] = 1
#             elif self.board[self.coordinates[0]][self.coordinates[1]] == 1:
#                 pygame.draw.rect(screen, pygame.Color('blue'),
#                                  (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                 self.board[self.coordinates[0]][self.coordinates[1]] = 2
#             elif self.board[self.coordinates[0]][self.coordinates[1]] == 2:
#                 pygame.draw.rect(screen, pygame.Color('black'),
#                                  (digit_x, digit_y, self.cell_size, self.cell_size), 0)
#                 self.board[self.coordinates[0]][self.coordinates[1]] = 0
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
#     board.set_view(40, 60, 55)
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
# if __name__ == '__main__':
#     main()

# import pygame
# import sys
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Куб')
#     try:
#         size, color = [int(x.rstrip()) for x in sys.stdin]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     if size not in range(101) or size % 4 != 0 or color not in range(360):
#         raise ValueError('Неправильный формат ввода')
#     window_size = 300, 300
#     screen = pygame.display.set_mode(window_size)
#     draw(screen, size, color)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, size, colors):
#     color = pygame.Color(0, 0, 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0] + colors, 100, 75, 100)
#     pygame.draw.rect(screen, color, ((300 - size) / 2, (300 - size) / 2, size, size), 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0], 100, 100, 100)
#     pygame.draw.polygon(screen, color,
#                         [((300 - size) / 2, (300 - size) / 2),
#                          ((300 - size) / 2 + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5, (300 - size) / 2 - size / 2),
#                          ((300 - size) / 2 + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5 + size,
#                           (300 - size) / 2 - size / 2),
#                          ((300 - size) / 2 + size, (300 - size) / 2)], 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0], 100, 50, 100)
#     pygame.draw.polygon(screen, color,
#                         [((300 - size) / 2 + size, (300 - size) / 2),
#                          ((300 - size) / 2 + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5 + size,
#                           (300 - size) / 2 - size / 2),
#                          ((300 - size) / 2 + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5 + size,
#                           (300 - size) / 2 - size / 2 + size),
#                          ((300 - size) / 2 + size, (300 - size) / 2 + size),
#                          ], 0)
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import pygame
# import sys
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Куб')
#     try:
#         for line in sys.stdin:
#             size, color = [int(x.rstrip()) for x in line.split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     if size not in range(101) or size % 4 != 0 or color not in range(360):
#         raise ValueError('Неправильный формат ввода')
#     window_size = 300, 300
#     screen = pygame.display.set_mode(window_size)
#     draw(screen, size, color)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, size, colors):
#     color = pygame.Color(0, 0, 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0] + colors, 100, 75, 100)
#     coors_x = 150 - (size * 1.5 / 2)
#     coors_y = 200 - (size * 1.5 / 2)
#     pygame.draw.rect(screen, color, (coors_x, coors_y, size, size), 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0], 100, 100, 100)
#     pygame.draw.polygon(screen, color,
#                         [(coors_x, coors_y),
#                          (coors_x + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5, coors_y - size / 2),
#                          (coors_x + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5 + size, (coors_y - size / 2)),
#                          (coors_x + size, coors_y)], 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0], 100, 50, 100)
#     pygame.draw.polygon(screen, color,
#                         [(coors_x + size, coors_y),
#                          (coors_x + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5 + size,
#                           coors_y - size / 2),
#                          (coors_x + ((size / 2) ** 2 + (size / 2.5) ** 2) ** 0.5 + size,
#                           coors_y - size / 2 + size),
#                          (coors_x + size, coors_y + size),
#                          ], 0)
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import pygame
# import sys
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Куб')
#     try:
#         size, color = [int(x) for x in input().split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     if size not in range(101) or size % 4 != 0 or color not in range(360):
#         raise ValueError('Неправильный формат ввода')
#     window_size = 300, 300
#     screen = pygame.display.set_mode(window_size)
#     draw(screen, size, color)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, size, colors):
#     color = pygame.Color(0, 0, 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0] + colors, 100, 75, 100)
#     coors_x = 150 - (size / 4 * 3)
#     coors_y = 150 - (size / 4)
#     pygame.draw.rect(screen, color, (coors_x, coors_y, size, size), 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0], 100, 100, 100)
#     pygame.draw.polygon(screen, color,
#                         [(coors_x, coors_y),
#                          (coors_x + size / 2, coors_y - size / 2),
#                          (coors_x + size / 2 + size, (coors_y - size / 2)),
#                          (coors_x + size, coors_y)], 0)
#     hsv = color.hsva
#     color.hsva = (hsv[0], 100, 50, 100)
#     pygame.draw.polygon(screen, color,
#                         [(coors_x + size, coors_y),
#                          (coors_x + size / 2 + size,
#                           coors_y - size / 2),
#                          (coors_x + size / 2 + size,
#                           coors_y - size / 2 + size),
#                          (coors_x + size, coors_y + size),
#                          ], 0)
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import sys
# import pygame
#
# COLORS = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('green'), ]
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Крест')
#     try:
#         size_circle, number = [int(x) for x in input().split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     size = (2 * size_circle * number, 2 * size_circle * number)
#     screen = pygame.display.set_mode(size)
#     draw(screen, size_circle, number)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, size_circle, number):
#     circle_radius = size_circle * number
#     circle_position = (circle_radius, circle_radius)
#     digit = 3
#     while number > 0:
#         if number % digit == 0:
#             pygame.draw.circle(screen, COLORS[1], circle_position, circle_radius, width=0)
#             circle_radius -= size_circle
#             number -= 1
#         elif number % digit == 2:
#             pygame.draw.circle(screen, COLORS[2], circle_position, circle_radius, width=0)
#             circle_radius -= size_circle
#             number -= 1
#         elif number % digit == 1:
#             pygame.draw.circle(screen, COLORS[0], circle_position, circle_radius, width=0)
#             circle_radius -= size_circle
#             number -= 1
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import sys
# import pygame
#
# COLORS = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('green'), ]
#
#
# def main():
#     pygame.init()
#     pygame.display.set_caption('Крест')
#     try:
#         size_circle, number = [int(x) for x in input().split()]
#     except ValueError:
#         print('Неправильный формат ввода')
#         return -1
#     size = (2 * size_circle * number, 2 * size_circle * number)
#     screen = pygame.display.set_mode(size)
#     draw(screen, size_circle, number)
#     pygame.display.flip()
#
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
#
#
# def draw(screen, size_circle, number):
#     circle_radius = size_circle * number
#     circle_position = (circle_radius, circle_radius)
#     digit = 3
#     while number > 0:
#         if number % digit == 0:
#             pygame.draw.circle(screen, COLORS[1], circle_position, circle_radius, width=0)
#             circle_radius -= size_circle
#             number -= 1
#         elif number % digit == 2:
#             pygame.draw.circle(screen, COLORS[2], circle_position, circle_radius, width=0)
#             circle_radius -= size_circle
#             number -= 1
#         elif number % digit == 1:
#             pygame.draw.circle(screen, COLORS[0], circle_position, circle_radius, width=0)
#             circle_radius -= size_circle
#             number -= 1
#
#
# if __name__ == '__main__':
#     sys.exit(main())
# import os
# import sys
# import pygame
#
# pygame.init()
# pygame.display.set_caption('Свой курсор мыши')
# size = width, height = 500, 500
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
# cursor = pygame.sprite.Sprite(all_sprites)
# cursor.image = load_image('People.png')
# cursor.rect = cursor.image.get_rect()
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] == 1:
#             plenty[0] -= 10
#             plenty[1] -= 10
#             cursor.rect.x, cursor.rect.y = plenty[0], plenty[1]
#             print('ddd')
#             screen.fill('white')
#             all_sprites.draw(screen)
#     pygame.display.flip()
#     all_sprites.draw(screen)
#     clock.tick(fps)
#
# pygame.quit()
dictionary = {'А': 'ка', 'И': 'ки', 'Р': 'ши', 'Ш': 'ли',
              'Б': 'зу', 'Й': 'фу', 'С': 'ари', 'Щ': 'ни',
              'В': 'ру', 'К': 'ме', 'Т': 'чи', 'Ъ': 'д',
              'Г': 'джи', 'Л': 'та', 'У': 'мей', 'Ы': 'хе',
              'Д': 'те', 'М': 'рин', 'Ф': 'лу', 'Ь': 'ксе',
              'Е': 'ку', 'Ё': 'ку', 'Н': 'то', 'Х': 'ри', 'Э': 'га',
              'Ж': 'зу', 'О': 'мо', 'Ц': 'ми', 'Ю': 'до',
              'З': 'з', 'П': 'но', 'Ч': 'зи', 'Я': 'ма'}
string = ''
number = 1
word = input()
for letter in word:
    string += dictionary[letter.upper()]
print(string.capitalize())