import pygame
import random


pygame.init()

HEIGHT = 800
WIDTH = 1000
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
VEL = 25
end_font = pygame.font.SysFont("comicsans", 100)


# Detects all collisions while simultaneously adding and removing apples
def collision(snake, boarders, apple):
    if pygame.Rect.collidelist(snake[0], snake[1:]) != -1:
        return True
    elif pygame.Rect.collidelist(snake[0], boarders[0:]) != -1:
        return True
    if len(apple) == 1:
        #If the snake eats an apple, it adds three to its length
        if pygame.Rect.collidelist(snake[0], apple) != -1:
            for _ in range(3):
                snake.append(pygame.Rect(snake[-1].x, snake[-1].y, 25, 25))
            apple.pop()
        else:
            pygame.draw.rect(screen, RED, apple[0])
    # Prevents apple from spawning onto the snake
    else:
        apple_loc = [(random.choice([x for x in range(0, WIDTH-25, 25)]),
                      random.choice([y for y in range(0, HEIGHT-25, 25)]))]

        snake_loc = [(part.x, part.y) for part in snake]
        if set(apple_loc).intersection(set(snake_loc)) != set():
            collision(snake, boarders, apple)
        else:
            apple.append(pygame.Rect(apple_loc[0][0], apple_loc[0][1], 25, 25))
    return False

# Moves the snake by starting from the last snake cube and setting the (x, y) values equal to the next cube
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
    snake = [pygame.Rect(WIDTH/2, HEIGHT/2, 25, 25)]
    apple = []

    boarders_top = pygame.Rect(0, -5, WIDTH, 5)
    boarders_bottom = pygame.Rect(0, HEIGHT, WIDTH, 5)
    boarders_left = pygame.Rect(-5, 0, 5, HEIGHT)
    boarders_right = pygame.Rect(WIDTH, 0, 5, HEIGHT)
    # List of all 4 boarders as rectangle objects to be passed into the collision function
    boarders = [boarders_top, boarders_bottom, boarders_left, boarders_right]

    last_input = None
    next_input = None
    play_game = True
# Game loop simultaneously updates movement inputs using the pygame event buffer
    while play_game:
        clock.tick(15)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                play_game = False
            elif event.type == pygame.KEYDOWN:
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
        # Locks in the input to prevent player from making illegal inputs such as moving the snake backwards onto itself
        last_input = next_input


        if not collision(snake, boarders, apple):
            pygame.display.update()
            screen.fill(BLACK)
            for boarder in boarders:
                pygame.draw.rect(screen, RED, boarder)
            move_snake(snake, last_input)
            #End screen text
        else:
            end_screen_text = pygame.font.Font.render(end_font, f"You Died!", True, (255, 255, 255))
            end_score_text = pygame.font.Font.render(end_font, "Score: ", True, (255, 255, 255))
            end_score = pygame.font.Font.render(end_font, f"{len(snake) - 1}", True, (0, 150, 0))
            screen.blit(end_screen_text, ((WIDTH/2) - 160, (HEIGHT/2) - 100))
            screen.blit(end_score_text, ((WIDTH / 2) - 140, (HEIGHT / 2)))
            screen.blit(end_score, ((WIDTH / 2) + 100, (HEIGHT / 2)))
            pygame.display.update()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main()
                    elif event.key == pygame.K_ESCAPE:
                        play_game = False
    pygame.quit()

if __name__ == '__main__':
    main()
