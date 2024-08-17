import pygame
pygame.init()

HEIGHT = 1100
WIDTH = 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
VEL = 10


def draw_window(snake, direction):
    screen.fill(BLACK)
    for part in snake:
        if snake.index(part) == 0:
            if direction == "up":
                part.y -= VEL
            elif direction == "down":
                part.y += VEL
            elif direction == "left":
                part.x -= VEL
            elif direction == "right":
                part.x += VEL
        pygame.draw.rect(screen, GREEN, snake[0])
    pygame.display.update()


def main():
    snake = [pygame.Rect(HEIGHT/2 - 25, WIDTH/2 - 25, 50, 50)]
    head_position_x, head_position_y = snake[0].x, snake[0].y
    direction = ""
    play_game = True

    while play_game:
        clock.tick(10)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                play_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "up"
                if event.key == pygame.K_DOWN:
                    direction = "down"
                if event.key == pygame.K_LEFT:
                    direction = "left"
                if event.key == pygame.K_RIGHT:
                    direction = "right"

        draw_window(snake, direction)
    pygame.quit()


if __name__ == '__main__':
    main()
