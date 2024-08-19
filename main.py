import pygame
pygame.init()

HEIGHT = 1100
WIDTH = 800
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
VEL = 25

apple_eaten = pygame.USEREVENT + 1
collision = pygame.USEREVENT + 2


def check_collision(snake):
    if pygame.Rect.collidelist(snake[0], snake[1:]) != -1:
        return True
    return False


def move_snake(snake, direction):
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


def main():
    snake = [pygame.Rect(HEIGHT/2, WIDTH/2, 25, 25)]
    apples = [pygame.Rect(HEIGHT/2, WIDTH/2, 25, 25)]
    last_input = None
    next_input = None
    play_game = True

    while play_game:
        clock.tick(15)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                play_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    snake.append(pygame.Rect(HEIGHT / 2, WIDTH / 2, 25, 25))
                if event.key == pygame.K_UP:
                    if last_input != pygame.K_DOWN:
                        next_input = pygame.K_UP

                if event.key == pygame.K_DOWN:
                    if last_input != pygame.K_UP:
                        next_input = pygame.K_DOWN

                if event.key == pygame.K_LEFT:
                    if last_input != pygame.K_RIGHT:
                        next_input = pygame.K_LEFT

                if event.key == pygame.K_RIGHT:
                    if last_input != pygame.K_LEFT:
                        next_input = pygame.K_RIGHT
        last_input = next_input
        if not check_collision(snake):
            screen.fill(BLACK)
            move_snake(snake, last_input)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
