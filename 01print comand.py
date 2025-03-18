import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Donkey Kong Recreation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# FPS
FPS = 60


# Classes for the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 60
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = True  # Check if player is standing

    def update(self, platforms, ladders):
        # Apply gravity
        self.velocity_y += 1

        # Reset flags
        self.on_ground = False

        # Horizontal movement
        self.rect.x += self.velocity_x

        # Platform collision (horizontal)
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y >= 0:
                if platform.rect.top <= self.rect.bottom <= platform.rect.top + 6:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True

        # Vertical movement
        self.rect.y += self.velocity_y

        # Platform collision (vertical)
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if platform.rect.top <= self.rect.bottom <= platform.rect.top + 10:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True

        # Prevent climbing unless on ladders
        ladder_collision = pygame.sprite.spritecollide(self, ladders, False)
        if ladder_collision:
            self.on_ground = True

        # Respawn the player if they fall off the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = 50  # Reset player to starting position
            self.rect.y = SCREEN_HEIGHT - 60

    def move(self, x, y):
        self.velocity_x = x
        if y < 0 and self.on_ground:  # Jumping
            self.velocity_y = y
        elif y > 0:  # Simulate climbing logic
            self.velocity_y = y


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = random.choice([-3, 3])
        self.velocity_y = 0

    def update(self, platforms):
        # Update barrel position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Gravity applies to barrels
        self.velocity_y += 1

        # Collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.velocity_y = 0
                self.rect.bottom = platform.rect.top

        # Bounce barrels off screen edges
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity_x *= -1  # Reverse direction


class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
ladders = pygame.sprite.Group()
barrels = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms
for i in range(5):
    platform = Platform(100 * i, SCREEN_HEIGHT - (100 * i + 40), 200, 20)
    platforms.add(platform)
    all_sprites.add(platform)

# Create ladders
for i in range(4):
    ladder = Ladder(100 * (i + 1) - 50, SCREEN_HEIGHT - (100 * i + 120), 20, 100)
    ladders.add(ladder)
    all_sprites.add(ladder)

# Add barrels
for _ in range(3):
    barrel = Barrel(random.randint(0, SCREEN_WIDTH - 20), 20)
    barrels.add(barrel)
    all_sprites.add(barrel)

# Create goal
goal = Goal(700, 60)
all_sprites.add(goal)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    move_x = 0
    move_y = 0
    if keys[pygame.K_LEFT]:
        move_x = -5
    if keys[pygame.K_RIGHT]:
        move_x = 5
    if keys[pygame.K_UP]:
        move_y = -5  # Climb ladder or jump
    if keys[pygame.K_DOWN]:
        move_y = 5  # Descend ladder

    player.move(move_x, move_y)

    # Update all sprites
    barrels.update(platforms)
    all_sprites.update(platforms, ladders)

    # Check for collisions
    if pygame.sprite.spritecollide(player, barrels, False):
        print("Game Over!")
        running = False

    if pygame.sprite.collide_rect(player, goal):
        print("You Win!")
        running = False

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = random.choice([-3, 3])
        self.velocity_y = 0

    def update(self, platforms, ladders=None):  # Adjusted to accept 2 arguments
        # Update barrel position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Gravity applies to barrels
        self.velocity_y += 1

        # Collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.velocity_y = 0
                self.rect.bottom = platform.rect.top

        # Bounce barrels off screen edges
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity_x *= -1  # Reverse direction