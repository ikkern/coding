import pygame
import sys
import subprocess

pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("iPod Interface")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
LIGHT_GRAY = (240, 240, 240)
BLUE = (50, 150, 255)
DARK_GRAY = (100, 100, 100)

# Fonts
font = pygame.font.SysFont("Arial", 22)
title_font = pygame.font.SysFont("Arial", 18, bold=True)

# Menu items
menu_items = ["Music", "Photos", "Settings", "Games", "Now Playing"]
selected_index = 0

def draw_interface():
    screen.fill(WHITE)

    # Draw screen frame
    pygame.draw.rect(screen, GRAY, (40, 40, 320, 220), border_radius=12)
    pygame.draw.rect(screen, LIGHT_GRAY, (50, 60, 300, 180))  # inner screen

    # Title bar
    pygame.draw.rect(screen, GRAY, (50, 60, 300, 30))
    title = title_font.render("iPod", True, BLACK)
    screen.blit(title, (60, 65))

    # Draw menu items
    for i, item in enumerate(menu_items):
        y = 95 + i * 28
        if i == selected_index:
            pygame.draw.rect(screen, BLUE, (55, y - 4, 290, 26))
            label = font.render(item, True, WHITE)
        else:
            label = font.render(item, True, BLACK)
        screen.blit(label, (70, y))

    # Draw wheel
    pygame.draw.circle(screen, GRAY, (WIDTH // 2, 470), 100)
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, 470), 40)

    # Draw wheel text
    wheel_font = pygame.font.SysFont("Arial", 16)
    screen.blit(wheel_font.render("MENU", True, BLACK), (WIDTH//2 - 20, 370))
    screen.blit(wheel_font.render("⏯", True, BLACK), (WIDTH//2 - 8, 520))
    screen.blit(wheel_font.render("<<", True, BLACK), (140, 460))
    screen.blit(wheel_font.render(">>", True, BLACK), (WIDTH - 160, 460))

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    draw_interface()
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_index = (selected_index - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_index = (selected_index + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                selected_item = menu_items[selected_index]
                print(f"Selected: {selected_item}")
                if selected_item == "Games":
                    pygame.quit()
                    subprocess.call(["python", "pong_game.py"])
                    pygame.init()
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
