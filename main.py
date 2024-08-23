import pygame
pygame.init()
#setup screen
gamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")
#game variables
game_exit = False
game_over = False
#game loop
while not game_exit:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit