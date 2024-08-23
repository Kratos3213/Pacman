import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PACMAN_SIZE = 30
GHOST_SIZE = 30
BLOCK_SIZE = 30
PACMAN_SPEED = 5
GHOST_SPEED = 3

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Load images
pacman_image = pygame.image.load("pacman.png")
pacman_image = pygame.transform.scale(pacman_image, (PACMAN_SIZE, PACMAN_SIZE))
ghost_image = pygame.image.load("ghost.png")
ghost_image = pygame.transform.scale(ghost_image, (GHOST_SIZE, GHOST_SIZE))

# Define classes
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "RIGHT"

    def draw(self):
        screen.blit(pacman_image, (self.x, self.y))

    def move(self, direction):
        if direction == "UP":
            self.y -= PACMAN_SPEED
        elif direction == "DOWN":
            self.y += PACMAN_SPEED
        elif direction == "LEFT":
            self.x -= PACMAN_SPEED
        elif direction == "RIGHT":
            self.x += PACMAN_SPEED
        self.direction = direction

    def check_boundary(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= SCREEN_WIDTH - PACMAN_SIZE:
            self.x = SCREEN_WIDTH - PACMAN_SIZE
        if self.y <= 0:
            self.y = 0
        elif self.y >= SCREEN_HEIGHT - PACMAN_SIZE:
            self.y = SCREEN_HEIGHT - PACMAN_SIZE

class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def draw(self):
        screen.blit(ghost_image, (self.x, self.y))

    def move(self):
        directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        directions.remove(self.direction)
        self.direction = random.choice(directions)
        if self.direction == "UP":
            self.y -= GHOST_SPEED
        elif self.direction == "DOWN":
            self.y += GHOST_SPEED
        elif self.direction == "LEFT":
            self.x -= GHOST_SPEED
        elif self.direction == "RIGHT":
            self.x += GHOST_SPEED

    def check_boundary(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= SCREEN_WIDTH - GHOST_SIZE:
            self.x = SCREEN_WIDTH - GHOST_SIZE
        if self.y <= 0:
            self.y = 0
        elif self.y >= SCREEN_HEIGHT - GHOST_SIZE:
            self.y = SCREEN_HEIGHT - GHOST_SIZE

# Create objects
pacman = Pacman(SCREEN_WIDTH // 2 - PACMAN_SIZE // 2, SCREEN_HEIGHT // 2 - PACMAN_SIZE // 2)
ghost = Ghost(random.randint(0, SCREEN_WIDTH - GHOST_SIZE), random.randint(0, SCREEN_HEIGHT - GHOST_SIZE))

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.move("UP")
            elif event.key == pygame.K_DOWN:
                pacman.move("DOWN")
            elif event.key == pygame.K_LEFT:
                pacman.move("LEFT")
            elif event.key == pygame.K_RIGHT:
                pacman.move("RIGHT")
    
    # Move pacman and ghost
    pacman.check_boundary()
    ghost.move()
    ghost.check_boundary()
    
    # Draw objects
    pacman.draw()
    ghost.draw()
    
    # Collision detection
    if pacman.x < ghost.x + GHOST_SIZE and pacman.x + PACMAN_SIZE > ghost.x and pacman.y < ghost.y + GHOST_SIZE and pacman.y + PACMAN_SIZE > ghost.y:
        print("Game Over!")  # For now, just print Game Over on console
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
