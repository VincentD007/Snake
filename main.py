import pygame
pygame.init()

HEIGHT = 1100
WIDTH = 800
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
VEL = 25


def draw_window(snake, direction):
    screen.fill(BLACK)
    for num in range(1, len(snake)):
        snake[-num].x = snake[-num - 1].x
        snake[-num].y = snake[-num - 1].y

    if direction == pygame.K_UP:
        snake[0].y -= VEL
    elif direction == pygame.K_DOWN:
        snake[0].y += VEL
    elif direction == pygame.K_LEFT:
        snake[0].x -= VEL
    elif direction == pygame.K_RIGHT:
        snake[0].x += VEL
    for part in snake:
        pygame.draw.rect(screen, GREEN, part)
    pygame.display.update()


def main():
    snake = [pygame.Rect(HEIGHT/2, WIDTH/2, 25, 25)]
    for _ in range(5):
        snake.append(pygame.Rect(HEIGHT/2, WIDTH/2, 25, 25))
    last_input = None
    play_game = True

    while play_game:
        clock.tick(15)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                play_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    last_input = pygame.K_UP
                if event.key == pygame.K_DOWN:
                    last_input = pygame.K_DOWN
                if event.key == pygame.K_LEFT:
                    last_input = pygame.K_LEFT
                if event.key == pygame.K_RIGHT:
                    last_input = pygame.K_RIGHT

        draw_window(snake, last_input)
    pygame.quit()


if __name__ == '__main__':
    main()
