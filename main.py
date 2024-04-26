import pygame
from snake import *

pygame.init()

# screen
windowsScreen = {'width': 750, 'height': 570}
screen = pygame.display.set_mode((windowsScreen['width'], windowsScreen['height']))
pygame.display.set_caption('Snake by Vaydal')

# clock
clock = pygame.time.Clock()
fps = 10

# head of the snake
snake = Snake(25, 25, 25, 25)
food = Food(25, 25)

font = pygame.font.SysFont('comicsansms', 20)

def draw():
    global fps

    screen.fill((54, 54, 54))
    text = font.render(f'Score: {snake.score}', True, (255,255,255))
    screen.blit(text, text.get_rect())

    food.draw(screen)
    
    if not(snake.dead):
        snake.move()
        snake.update(screen)
        snake.handleCollision(food)
        fps += snake.addLevel()
    else:
        return False

    pygame.display.flip()
    return True

def main():
    run = True

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        run = draw()

    pygame.quit()

if __name__=='__main__':
    main()