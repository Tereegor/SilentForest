import os
import pygame
import sys
import random
import datetime as dt
import csv

pygame.init()
pygame.display.set_caption('Гонки')
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
running = True
screen.fill('white')
fps = 60
clock = pygame.time.Clock()
woods = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
car_sprite = pygame.sprite.Group()
money_sprite = pygame.sprite.Group()
plenty_speed = []
plenty_speed.append(30)
plenty_money = []
plenty_money.append(100)
plenty_order = []
plenty_order.append(3)
plenty_need_money = []
plenty_need_money.append(1)
play_end = False
pletny_second = [120]
plenty_number = []
Need_write = [1]
your_place = []


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
        if colorkey == 2:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    plenty_turn = [0]
    def draw_1():

        intro_text = ["Правила игры",
                      "Нужно набрать как можно больше монет",
                      "за две минут не касаясь леса"]

        fon = pygame.transform.scale(load_image('Start_foto.jpeg'), (1000, 700))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 35)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('Yellow'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.bottom = text_coord
            intro_rect.x = 280

            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    def draw_2():
        intro_text_2 = ["Управление",
                        "кнопки: вверх, вниз, вправо, влево - передвигают машинку",
                        "кнопки: вверх и вправо, влево и вправо, разворачивают машинку",
                        "кнопки: плюс и минус добавляют скорость",
                        "удачной игры!"]
        font = pygame.font.Font(None, 35)
        text_coord = 150
        for line in intro_text_2:
            string_rendered = font.render(line, 1, pygame.Color('Yellow'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.bottom = text_coord
            intro_rect.x = 20

            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    Right = True
    Left = False
    Jump = False
    Jump_down = False
    Hight_jump = [350]
    sprite_sheet_run = load_image("Jump.png", 2)
    jump_right = [sprite_sheet_run.subsurface((55 * i, 210, 50, 110)) for i in range(6)]
    jump_left = [pygame.transform.flip(x, True, False) for x in jump_right]
    foto_car = load_image("Car_for_starting.png")
    foto_car_left = pygame.transform.scale(foto_car, (170, 130))
    foto_car_right = pygame.transform.flip(foto_car_left, True, False)
    Number = 1
    coords_car = [0, 355]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        if Number < 5 and Jump and not Jump_down and Right:
            Number += 0.1
            Hight_jump[0] -= 1
        elif Number < 5 and Jump and Jump_down and Right:
            Number += 0.1
            if Hight_jump[0] <= 349:
                Hight_jump[0] += 1
            else:
                Jump_down = False
                Jump = False
        elif Number < 5 and Jump and not Jump_down and Left:
            Number += 0.1
            Hight_jump[0] -= 1
        elif Number < 5 and Jump and Jump_down and Left:
            Number += 0.1
            if Hight_jump[0] <= 349:
                Hight_jump[0] += 1
            else:
                Jump_down = False
                Jump = False
        else:
            Number = 1
        draw_1()
        draw_2()
        pygame.draw.line(screen, pygame.Color('white'), (0, 390), (1000, 390), 120)
        if plenty_turn[0] == 0:
            screen.blit(jump_left[int(Number)], (400, Hight_jump[0]))
        elif plenty_turn[0] == 1:
            screen.blit(jump_right[int(Number)], (400, Hight_jump[0]))
        if coords_car[0] < 840 and Right:
            coords_car[0] += 2
            screen.blit(foto_car_right, (coords_car[0], coords_car[1]))
            plenty_turn[0] = 0
        elif coords_car[0] >= 840:
            Right = False
            Left = True
            coords_car[0] -= 2
            screen.blit(foto_car_left, (coords_car[0], coords_car[1]))
            plenty_turn[0] = 1
        elif coords_car[0] > 5 and Left:
            coords_car[0] -= 2
            screen.blit(foto_car_left, (coords_car[0], coords_car[1]))
        elif coords_car[0] <= 5:
            Left = False
            Right = True
            coords_car[0] += 2
            screen.blit(foto_car_right, (coords_car[0], coords_car[1]))
        if 210 > coords_car[0] >= 200 and Right:
            Jump = True
        if coords_car[0] >= 350 and Right:
            Jump_down = True
        if 470 > coords_car[0] >= 460 and Left:
            Jump = True
        if coords_car[0] <= 270 and Left:
            Jump_down = True
        pygame.display.flip()
        clock.tick(fps)


start_screen()


class Fences(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(woods)
        self.image = pygame.Surface([280, 180])
        self.image.fill(pygame.Color('green'))
        self.rect = pygame.Rect(x1, y1, x2, y2)


class Fir(pygame.sprite.Sprite):
    image = load_image('Fil_3.bmp', -1)
    image_1 = pygame.transform.scale(image, (50, 50))

    def __init__(self, group):
        super().__init__(group)
        self.image = Fir.image_1
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(area_start[0], area_start[1])
        self.rect.y = random.randrange(area_finish[0], area_finish[1])


class Make_money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(money_sprite)
        self.add(money_sprite)
        self.image = pygame.Surface((15, 15),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("yellow"),
                           (7.5, 7.5), 7.5)

        if plenty_order[0] % 4 == 0:
            self.rect = pygame.Rect(random.randrange(315, 345), random.randrange(0, 690), 10, 10)
        elif plenty_order[0] % 4 == 1:
            self.rect = pygame.Rect(random.randrange(640, 680), random.randrange(0, 690), 10, 10)
        elif plenty_order[0] % 4 == 2:
            self.rect = pygame.Rect(random.randrange(10, 990), random.randrange(215, 255), 10, 10)
        elif plenty_order[0] % 4 == 3:
            self.rect = pygame.Rect(random.randrange(10, 990), random.randrange(470, 520), 10, 10)


def road(screen):
    pygame.draw.rect(screen, pygame.Color('grey'), (280, 0, 80, 700))
    pygame.draw.rect(screen, pygame.Color('grey'), (640, 0, 80, 700))
    pygame.draw.rect(screen, pygame.Color('grey'), (0, 180, 1000, 90))
    pygame.draw.rect(screen, pygame.Color('grey'), (0, 450, 1000, 90))
    for i in range(0, 700, 50):
        pygame.draw.line(screen, pygame.Color('white'), [320, i], [320, i + 30], 5)
    for i in range(0, 700, 50):
        pygame.draw.line(screen, pygame.Color('white'), [680, i], [680, i + 30], 5)
    for i in range(0, 1000, 50):
        pygame.draw.line(screen, pygame.Color('white'), [i, 225], [i + 30, 225], 5)
    for i in range(0, 1000, 50):
        pygame.draw.line(screen, pygame.Color('white'), [i, 495], [i + 30, 495], 5)


def place_in_total_list():
    with open('dictwriter.csv', 'a', newline='', encoding="utf8") as f:
        writer = csv.writer(
            f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if Need_write[0] == 1:
            writer.writerow([plenty_money[0]])
            Need_write[0] = 0


plenty_finally = []
plenty_place = []


def place_total():
    with open('dictwriter.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            if index != 0:
                 plenty_place.append(row[0])
        for i in range(len(plenty_place)):
            plenty_finally.append(int(plenty_place[i]))
        plenty_finally_2 = sorted(plenty_finally)
        your_place.append(len(plenty_finally) - plenty_finally_2.index(plenty_money[0]))


def remaining_time(screen):
    font = pygame.font.Font(None, 25)
    text = font.render(f'Осталось времени {pletny_second[0]} секунд', True, (pygame.Color('black')))
    text_x = 370
    text_y = 70
    screen.blit(text, (text_x, text_y))


def speed(screen):
    font = pygame.font.Font(None, 33)
    text = font.render(f'Ваша скорость {plenty_speed[0]} км/ч', True, (pygame.Color('black')))
    text_x = 730
    text_y = 70
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 10,
                                         text_w + 30, text_h + 20), 1)


def draw_end(screen):
    screen.fill('yellow')
    place_total()
    font = pygame.font.Font(None, 55)
    text = font.render(f'Поздравляю! Вы набрали {plenty_money[0]} монет', True, (pygame.Color('black')))
    text_x = 125
    text_y = 230
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 55)
    text = font.render(f'Вы заняли {your_place[0]} место общем зачёте', True, (pygame.Color('black')))
    text_x = 125
    text_y = 370
    screen.blit(text, (text_x, text_y))


def money(screen):
    font = pygame.font.Font(None, 33)
    text = font.render(f'У вас {plenty_money[0]} монет', True, (pygame.Color('black')))
    text_x = 30
    text_y = 70
    text_w = 170
    text_h = 25
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 10,
                                         text_w + 60, text_h + 20), 1)
    pygame.draw.circle(screen, pygame.Color('yellow'), (225, 80), 12)
    pygame.draw.circle(screen, pygame.Color('black'), (225, 80), 12, 2)


fence = Fences(0, 0, 270, 180)
fence_2 = Fences(360, 0, 270, 180)
fence_3 = Fences(720, 0, 270, 180)
fence_4 = Fences(0, 270, 270, 180)
fence_5 = Fences(360, 270, 270, 180)
fence_6 = Fences(720, 270, 270, 180)
fence_7 = Fences(0, 540, 270, 180)
fence_8 = Fences(360, 540, 270, 180)
fence_9 = Fences(720, 540, 270, 180)


class Car(pygame.sprite.Sprite):
    image = load_image("car_2.png", 2)
    image_1 = pygame.transform.scale(image, (90, 90))

    def __init__(self):
        super().__init__(car_sprite)
        self.image = Car.image_1
        self.rect = self.image.get_rect()
        self.rect.x = 635
        self.rect.y = 600

    def up(self):
        if not pygame.sprite.collide_mask(self, fence) and not pygame.sprite.collide_mask(self,
                                                                                          fence_2) and not pygame.sprite.collide_mask(
            self, fence_3) and not pygame.sprite.collide_mask(self, fence_4) \
                and not pygame.sprite.collide_mask(self, fence_5) and not pygame.sprite.collide_mask(self, fence_6) \
                and not pygame.sprite.collide_mask(self, fence_7) and not pygame.sprite.collide_mask(self, fence_8) \
                and not pygame.sprite.collide_mask(self, fence_9) and not pygame.sprite.collide_mask(self, cash):
            if plenty_speed[0] * 0.1 >= 1:
                self.rect = self.rect.move(0, -(plenty_speed[0] * 0.1))
                self.rect.y -= plenty_speed[0] * 0.1
            elif plenty_speed[0] != 0:
                self.rect = self.rect.move(0, -1)
                self.rect.y -= 1
        elif pygame.sprite.collide_mask(self, cash):
            plenty_money[0] += 10
            global money_sprite
            money_sprite = pygame.sprite.Group()
            plenty_order[0] += 1
            plenty_need_money[0] = 1
        else:
            if plenty_money[0] != 0:
                plenty_money[0] -= 5
            self.image = Car.image_1
            self.rect.x = 635
            self.rect.y = 600

    def turn_right(self):
        if not pygame.sprite.collide_mask(self, fence) and not pygame.sprite.collide_mask(self,
                                                                                          fence_2) and not pygame.sprite.collide_mask(
            self, fence_3) and not pygame.sprite.collide_mask(self, fence_4) \
                and not pygame.sprite.collide_mask(self, fence_5) and not pygame.sprite.collide_mask(self, fence_6) \
                and not pygame.sprite.collide_mask(self, fence_7) and not pygame.sprite.collide_mask(self, fence_8) \
                and not pygame.sprite.collide_mask(self, fence_9) and not pygame.sprite.collide_mask(self, cash):
            self.image = pygame.transform.rotate(self.image, -90)
            self.rect = self.rect.move(-3, 3)
            self.rect.x -= 3
            self.rect.y += 3
        elif pygame.sprite.collide_mask(self, cash):
            plenty_money[0] += 10
            global money_sprite
            money_sprite = pygame.sprite.Group()
            plenty_order[0] += 1
            plenty_need_money[0] = 1
        else:
            if plenty_money[0] != 0:
                plenty_money[0] -= 5
            self.image = Car.image_1
            self.rect.x = 635
            self.rect.y = 600

    def turn_left(self):
        if not pygame.sprite.collide_mask(self, fence) and not pygame.sprite.collide_mask(self,
                                                                                          fence_2) and not pygame.sprite.collide_mask(
            self, fence_3) and not pygame.sprite.collide_mask(self, fence_4) \
                and not pygame.sprite.collide_mask(self, fence_5) and not pygame.sprite.collide_mask(self, fence_6) \
                and not pygame.sprite.collide_mask(self, fence_7) and not pygame.sprite.collide_mask(self, fence_8) \
                and not pygame.sprite.collide_mask(self, fence_9) and not pygame.sprite.collide_mask(self, cash):
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.rect.move(3, 3)
            self.rect.x += 3
            self.rect.y += 3
        elif pygame.sprite.collide_mask(self, cash):
            plenty_money[0] += 10
            global money_sprite
            money_sprite = pygame.sprite.Group()
            plenty_order[0] += 1
            plenty_need_money[0] = 1
        else:
            if plenty_money[0] != 0:
                plenty_money[0] -= 5
            self.image = Car.image_1
            self.rect.x = 635
            self.rect.y = 600

    def right(self):
        if not pygame.sprite.collide_mask(self, fence) and not pygame.sprite.collide_mask(self,
                                                                                          fence_2) and not pygame.sprite.collide_mask(
            self, fence_3) and not pygame.sprite.collide_mask(self, fence_4) \
                and not pygame.sprite.collide_mask(self, fence_5) and not pygame.sprite.collide_mask(self, fence_6) \
                and not pygame.sprite.collide_mask(self, fence_7) and not pygame.sprite.collide_mask(self, fence_8) \
                and not pygame.sprite.collide_mask(self, fence_9) and not pygame.sprite.collide_mask(self, cash):
            self.rect = self.rect.move(plenty_speed[0] * 0.1, 0)
            self.rect.x += plenty_speed[0] * 0.1
        elif pygame.sprite.collide_mask(self, cash):
            plenty_money[0] += 10
            global money_sprite
            money_sprite = pygame.sprite.Group()
            plenty_order[0] += 1
            plenty_need_money[0] = 1
        else:
            if plenty_money[0] != 0:
                plenty_money[0] -= 5
            self.image = Car.image_1
            self.rect.x = 635
            self.rect.y = 600

    def left(self):
        if not pygame.sprite.collide_mask(self, fence) and not pygame.sprite.collide_mask(self,
                                                                                          fence_2) and not pygame.sprite.collide_mask(
            self, fence_3) and not pygame.sprite.collide_mask(self, fence_4) \
                and not pygame.sprite.collide_mask(self, fence_5) and not pygame.sprite.collide_mask(self, fence_6) \
                and not pygame.sprite.collide_mask(self, fence_7) and not pygame.sprite.collide_mask(self, fence_8) \
                and not pygame.sprite.collide_mask(self, fence_9) and not pygame.sprite.collide_mask(self, cash):
            if plenty_speed[0] * 0.1 >= 1:
                self.rect = self.rect.move(-(plenty_speed[0] * 0.1), 0)
                self.rect.x -= plenty_speed[0] * 0.1
            elif plenty_speed[0] != 0:
                self.rect = self.rect.move(-1, 0)
                self.rect.x -= 1
        elif pygame.sprite.collide_mask(self, cash):
            plenty_money[0] += 10
            global money_sprite
            money_sprite = pygame.sprite.Group()
            plenty_order[0] += 1
            plenty_need_money[0] = 1
        else:
            if plenty_money[0] != 0:
                plenty_money[0] -= 5
            self.image = Car.image_1
            self.rect.x = 635
            self.rect.y = 600

    def down(self):
        if not pygame.sprite.collide_mask(self, fence) and not pygame.sprite.collide_mask(self,
                                                                                          fence_2) and not pygame.sprite.collide_mask(
            self, fence_3) and not pygame.sprite.collide_mask(self, fence_4) \
                and not pygame.sprite.collide_mask(self, fence_5) and not pygame.sprite.collide_mask(self, fence_6) \
                and not pygame.sprite.collide_mask(self, fence_7) and not pygame.sprite.collide_mask(self, fence_8) \
                and not pygame.sprite.collide_mask(self, fence_9) and not pygame.sprite.collide_mask(self, cash):
            self.rect = self.rect.move(0, plenty_speed[0] * 0.1)
            self.rect.y += plenty_speed[0] * 0.1
        elif pygame.sprite.collide_mask(self, cash):
            plenty_money[0] += 10
            global money_sprite
            money_sprite = pygame.sprite.Group()
            plenty_order[0] += 1
            plenty_need_money[0] = 1
        else:
            if plenty_money[0] != 0:
                plenty_money[0] -= 5
            self.image = Car.image_1
            self.rect.x = 635
            self.rect.y = 600

    def more_speed(self):
        plenty_speed[0] += 5

    def less_speed(self):
        if plenty_speed[0] != 0:
            plenty_speed[0] -= 5

    def transfer_gorizontal_first(self):
        if self.rect.x >= 980:
            self.rect.x = 5

    def transfer_gorizontal_twice(self):
        if self.rect.x <= 0:
            self.rect.x = 975

    def transfer_vertical_first(self):
        if self.rect.y >= 695:
            self.rect.y = 5

    def transfer_vertical_twice(self):
        if self.rect.y <= 0:
            self.rect.y = 690


area_start = [0, 230]
area_finish = [270, 400]
for i in range(120):
    Fir(all_sprites)
area_start = [360, 590]
area_finish = [270, 400]
for i in range(120):
    Fir(all_sprites)
area_start = [720, 950]
area_finish = [270, 400]
for i in range(120):
    Fir(all_sprites)
area_start = [0, 230]
area_finish = [540, 680]
for i in range(120):
    Fir(all_sprites)
area_start = [360, 590]
area_finish = [540, 680]
for i in range(120):
    Fir(all_sprites)
area_start = [720, 950]
area_finish = [540, 680]
for i in range(120):
    Fir(all_sprites)
name = Car()
move_left = move_right = move_up = move_down = False
number = dt.datetime.now().time()
plenty_time = (str(number).split(':'))
while running:
    digit = dt.datetime.now().time()
    plenty_time_2 = str(digit).split(':')
    if float(plenty_time_2[0]) - float(plenty_time[0]) == 1:
        if float(plenty_time_2[1]) + 60 - float(plenty_time[1]) >= 2 \
                and float(plenty_time_2[-1]) - float(plenty_time[-1]) >= 0:
            play_end = True
    else:
        if float(plenty_time_2[1]) - float(plenty_time[1]) >= 2 \
                and float(plenty_time_2[-1]) - float(plenty_time[-1]) >= 0:
            play_end = True
    if int(plenty_time_2[1]) == int(plenty_time[1]):
        if int(plenty_time_2[-1].split('.')[0]) - int(plenty_time[-1].split('.')[0]) >= 0 and int(
                plenty_time_2[-1].split('.')[0]) - int(plenty_time[-1].split('.')[0]) not in plenty_number:
            if pletny_second[0] != 0:
                pletny_second[0] -= 1
            plenty_number.append(int(plenty_time_2[-1].split('.')[0]) - int(plenty_time[-1].split('.')[0]))
    elif int(plenty_time_2[1]) - int(plenty_time[1]) == 1:
        if int(plenty_time_2[-1].split('.')[0]) + 60 - int(plenty_time[-1].split('.')[0]) >= 0 and int(
                plenty_time_2[-1].split('.')[0]) + 60 - int(plenty_time[-1].split('.')[0]) not in plenty_number:
            if pletny_second[0] != 0:
                pletny_second[0] -= 1
            plenty_number.append(int(plenty_time_2[-1].split('.')[0]) + 60 - int(plenty_time[-1].split('.')[0]))
    elif int(plenty_time_2[1]) - int(plenty_time[1]) == 2:
        if int(plenty_time_2[-1].split('.')[0]) + 120 - int(plenty_time[-1].split('.')[0]) >= 0 and int(
                plenty_time_2[-1].split('.')[0]) + 120 - int(plenty_time[-1].split('.')[0]) not in plenty_number:
            if pletny_second[0] != 0:
                pletny_second[0] -= 1
            plenty_number.append(int(plenty_time_2[-1].split('.')[0]) + 120 - int(plenty_time[-1].split('.')[0]))
    if plenty_need_money[0] == 1:
        cash = Make_money()
        plenty_need_money[0] = 0
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            name.turn_right()
        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            name.turn_left()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
            elif event.unicode == '+':
                name.more_speed()
            elif event.unicode == '-':
                name.less_speed()
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                move_left = move_right = move_down = move_up = False
    if not play_end:
        screen.fill('white')
        road(screen)
        all_sprites.draw(screen)
        if move_right:
            name.right()
        elif move_left:
            name.left()
        elif move_up:
            name.up()
        elif move_down:
            name.down()
        speed(screen)
        remaining_time(screen)
        money(screen)
        money_sprite.draw(screen)
        name.transfer_gorizontal_first()
        name.transfer_gorizontal_twice()
        name.transfer_vertical_first()
        name.transfer_vertical_twice()
        car_sprite.update()
        car_sprite.draw(screen)
    else:
        place_in_total_list()
        draw_end(screen)
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
