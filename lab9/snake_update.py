import pygame
import random
import time
pygame.init()

width, height = 1000, 700
cell_size = 25

rows, cols = height // cell_size, width // cell_size 

white = (255, 255, 255)
grey = (0, 255, 0)  # змейка
purple = (128, 0, 128)  # еда 
brown = (0, 0, 0)  # фон
yellow = (255, 255, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKEE game")

snake = [(5, 5)]  # точка старта 
direction = (1, 0)

sc = 0
score = 0
level = 0
speed = 5


# Функция генерации еды
def food_spawn():
    while True:
        food = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if food not in snake:  # Проверяем, чтобы еда не попала на змейку
            return food
disappearing_food = None
disappearing_food_timer = 0
disappearing_food_interval = 20  # Каждые 20 секунд


havka = food_spawn()

class Havchick:
    def __init__(self):
        self.position = self.havka_position()
        self.value = random.choice([1, 3, 5])  # ЕДА САЛМАГЫ  1, 3 или 5 очков
        
    def havka_position(self):
        while True:
            poz = (random.randint(0, cols -1), random.randint(0, rows-1))
            if poz not in snake: #make sure that meal is not in dnake coordinate
                return poz
    def respawn(self):
        self.position = self.havka_position()
        self.value = random.choice([1, 3, 5])

havka = Havchick()
running = True
clock = pygame.time.Clock()
start_time = time.time( )
while running:
    screen.fill(brown)

    curent_time = time.time() - start_time # устанавливаем таймер для нашего спешал фуд  

    if disappearing_food is None and int(curent_time) % disappearing_food_interval == 0: #invisable food gtntrftion 
        disappearing_food = food_spawn()
        disappearing_food_timer = curent_time + 7 # чеоез 7 секунд еда уходит

    if disappearing_food and curent_time >= disappearing_food_timer:
        disappearing_food = None

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

    if new_head == havka.position:
        score += havka.value
        sc += havka.value
        if sc >= 10:
            level += 1 
            sc = 0
        havka.respawn()
    elif disappearing_food and new_head == disappearing_food:
        score += 10
        level += 1 
        sc = 0
        disappering_food = None
        disappearing_food_timer = 0
    else:
        snake.pop()

        for segment in snake:  # змейка
            pygame.draw.rect(screen, grey, (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))

        # Еда
        pygame.draw.rect(screen, purple, (havka.position[0] * cell_size, havka.position[1] * cell_size, cell_size, cell_size))

        if disappearing_food:
            pygame.draw.rect(screen, yellow, (disappearing_food[0] * cell_size, disappearing_food[1] * cell_size, cell_size, cell_size))
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {score}  Level: {level}", True, white)
        screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
