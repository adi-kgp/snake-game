import pygame
import random

pygame.init()
# colors defined
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Creating display window
screen_width = 1000
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Game title
pygame.display.set_caption('Snakes Game')
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x,y, snake_size, snake_size])

# Game Loop
def gameLoop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 7
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    snake_size = 20
    fps = 30
    score = 0
    snake_length = 1
    snake_list = []
    # creating a game loop
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen('Game over! Press Enter to continue', red, 150, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length += 5

            gameWindow.fill(white)
            text_screen("Score: " + str(score * 10), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if (len(snake_list) > snake_length):
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameLoop()