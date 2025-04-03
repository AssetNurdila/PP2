import pygame
import random

pygame.init()

width, height = 1000, 700
cell_size = 25

rows, cols = height // cell_size, width // cell_size 

white = (255, 255, 255)
grey = (0, 255, 0)  
purple = (255, 0, 0)   
brown = (0, 0, 0)  

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKEE game")

snake = [(5, 5)]  
direction = (1, 0)

score = 0
level = 0
speed = 5

# Функция генерации еды
def food_spawn():
    while True:
        food = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if food not in snake:  # Проверяем, чтобы еда не попала на змейку
            return food

havka = food_spawn()

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(brown)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Обновление позиции змейки
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Проверка столкновения со стенами
    if new_head[0] < 0 or new_head[0] >= cols or new_head[1] < 0 or new_head[1] >= rows:
        print("Ты проиграл, стена duns duns!.")
        running = False
        break

    if new_head in snake:
        print("Ты проиграл, каннибализм запрещен!.")
        running = False
        break

    snake.insert(0, new_head)

    if new_head == havka:
        score += 1
        if score % 4 == 0:
            level += 1
            score += 3
        havka = food_spawn()
    else:
        snake.pop()

    for segment in snake:  # змейка
        pygame.draw.rect(screen, grey, (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))

    # Еда
    pygame.draw.rect(screen, purple, (havka[0] * cell_size, havka[1] * cell_size, cell_size, cell_size))

    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
