import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fishing Game test")

# colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Boat properties
boat_width, boat_height = 100, 30
boat_x = width // 2 - boat_width // 2
boat_y = height - boat_height - 20

# Fishing line properties
line_length = 200
line_angle = 0

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    screen.fill(BLUE)  # Background (water)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Boat movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        boat_x -= 5
    if keys[pygame.K_RIGHT]:
        boat_x += 5

    # Cast angle control (left-right)
    if keys[pygame.K_a]:
        line_angle -= 2  # Rotate left
    if keys[pygame.K_d]:
        line_angle += 2  # Rotate right

    # Draw the boat (as a simple rectangle)
    pygame.draw.rect(screen, BLACK, (boat_x, boat_y, boat_width, boat_height))

    # Draw the fishing line (a simple line for now)
    line_end_x = boat_x + boat_width // 2 + math.cos(math.radians(line_angle)) * line_length
    line_end_y = boat_y - math.sin(math.radians(line_angle)) * line_length
    pygame.draw.line(screen, BLACK, (boat_x + boat_width // 2, boat_y), (line_end_x, line_end_y), 3)

     # Display some basic instructions
    font = pygame.font.Font(None, 36)
    text = font.render('Press Spacebar to Cast', True, WHITE)
    screen.blit(text, (10, 10))

     # Update the display
    pygame.display.flip()

     # Limit the frame rate
    clock.tick(FPS)

#Test push

# Quit Pygame
pygame.quit()
sys.exit()
