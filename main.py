import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Get Got!")

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - 60
        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - 50:
            self.rect.x = WIDTH - 50

    def go_left(self):
        self.change_x = -5

    def go_right(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0

# Define the Block class
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([random.randint(20, 30), random.randint(20, 30)])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, WIDTH)

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

blocks = pygame.sprite.Group()

for i in range(5):
    block = Block()
    all_sprites.add(block)
    blocks.add(block)

clock = pygame.time.Clock()
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            elif event.key == pygame.K_RIGHT:
                player.go_right()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

    all_sprites.update()

    block_hits = pygame.sprite.spritecollide(player, blocks, False)
    if block_hits:
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)

    score += 1
    score_text = pygame.font.SysFont('arial', 25).render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
