import pygame
import random
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Мини-игра: Избегай шипы и собирай предметы")

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GREEN, (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed


class Spike(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, RED, [(0, 30), (15, 0), (30, 30)])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, SCREEN_WIDTH - 30)


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, SCREEN_WIDTH - 30)


all_sprites = pygame.sprite.Group()
spikes = pygame.sprite.Group()
powerups = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(5):
    spike = Spike()
    all_sprites.add(spike)
    spikes.add(spike)

for _ in range(3):
    powerup = PowerUp()
    all_sprites.add(powerup)
    powerups.add(powerup)

font = pygame.font.SysFont(None, 36)


def display_message(message, duration=3):
    text = font.render(message, True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(duration)


display_message("Добро пожаловать в игру!", 1)
display_message("Избегайте шипы и собирайте полезные предметы!", 2)
display_message("Набери 50 очков чтобы победить!", 2)

running = True
score = 0
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = time.time() - start_time
    if elapsed_time >= 60 or score >= 50:
        running = False
        result = "win" if score >= 50 else "loose"

    all_sprites.update()

    if pygame.sprite.spritecollide(player, spikes, True):
        score -= 5
        spike = Spike()
        all_sprites.add(spike)
        spikes.add(spike)

    if pygame.sprite.spritecollide(player, powerups, True):
        score += 1
        powerup = PowerUp()
        all_sprites.add(powerup)
        powerups.add(powerup)

    screen.fill(BLACK)
    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    time_left = max(0, 60 - int(elapsed_time))
    time_text = font.render(f"Time: {time_left}s", True, WHITE)
    screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

    pygame.display.flip()

    clock.tick(60)

if score >= 10:
    display_message("Вы победили!", 3)
    print("WIN")
else:
    display_message("Вы проиграли.", 3)

pygame.quit()
