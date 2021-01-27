import pygame

pygame.init()

screen_width = 1200
screen_height = 600

pygame.display.set_caption('Snakes Game')
pygame.display.update()

# creating game specific variables
exit_game = False
game_over = False

# creating a game loop
while not exit_game:

