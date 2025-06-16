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
BLUE = (50, 150, 255)

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Menu items
menu_items = ["Music", "Photos", "Settings", "Games", "Now Playing"]
selected_index = 0


def draw_interface():
    screen.fill(WHITE)

    # Draw screen
    pygame.draw.rect(screen, GRAY, (50, 50, 300, 200), border_radius=10)
    for i, item in enumerate(menu_items):
        color = BLUE if i == selected_index else BLACK
        label = font.render(item, True, color)
        screen.blit(label, (70, 60 + i * 30))

    # Draw wheel
    pygame.draw.circle(screen, GRAY, (WIDTH // 2, 450), 100)
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, 450), 40)

    # Draw wheel text
    center_font = pygame.font.SysFont("Arial", 20)
    screen.blit(center_font.render("MENU", True, BLACK), (WIDTH // 2 - 25, 360))
    screen.blit(center_font.render("⏯", True, BLACK), (WIDTH // 2 - 10, 520))
    screen.blit(center_font.render("<<", True, BLACK), (140, 445))
    screen.blit(center_font.render(">>", True, BLACK), (WIDTH - 160, 445))


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

                    # Run Pong game (separate turtle screen)
                    pygame.quit()
                    subprocess.call(["python", "pong_game.py"])
                    pygame.init()
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
