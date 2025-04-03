#Imports
#File must be executed in dir where placed task 
#in the terminal use cd .\Lab8\task1
#then you can start game
import pygame, sys
from pygame.locals import *
import random, time


pygame.init()

 
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
PLAYER_SPEED = 5
SCORE = 10
COIN = 0
# GEAR = 1 
# GEAR_BOX = [4, 4, 6, 8, 10, 12]


font = pygame.font.SysFont("Verdana", 60) #main font
font_small = pygame.font.SysFont("Verdana", 20)

game_over = font.render("Game Over", True, BLACK) #massage "Game over"
you_win = font.render("You Win", True, BLACK) #masssage "You win"

background = pygame.image.load("AnimatedStreet.png")


DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Crush")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png") #if file don't execute send full path to this png file
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)

        if (self.rect.bottom > 600):
            SCORE -= 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    global PLAYER_SPEED
    
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    # def gearBox(self, GEAR_KEY):
    #     global PLAYER_SPEED
    #     global GEAR
    #     if GEAR_KEY == "shift-up" and GEAR >= 1 and GEAR < 5:
    #         GEAR += 1
    #         PLAYER_SPEED = GEAR_BOX[GEAR]
    #         print(GEAR)
    #     if GEAR_KEY == "shift-down" and GEAR >= 0 and GEAR < 5:
    #         GEAR -= 1
    #         PLAYER_SPEED = GEAR_BOX[GEAR]
    #         print(GEAR)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_w]:
            self.gearBox("shift-up")
        if pressed_keys[K_s]:
            self.gearBox("shift-down")

        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-(PLAYER_SPEED), 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(PLAYER_SPEED, 0)


class BuffCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("BuffCoin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        
    def move(self):
        global SCORE
        global SPEED

        self.rect.move_ip(0, 3)
        if(self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 40), 0)
    
    def spawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 40), 0)

    def getBuff(self):
        global SPEED
       
        if SPEED > 10:
            SPEED -= 5
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 40), 0)                  


class TextDisplayer():
    """class for diplsaying text"""

    def __init__(self):
        super().__init__()

    def Print(self, text, text_position: tuple, text_color: tuple = BLACK, bg_color:tuple = WHITE):
        DISPLAYSURF.fill(bg_color)
        DISPLAYSURF.blit(font.render(text, True, text_color),  text_position)


        

Player = Player()
Car_Enemy = Enemy()
text = TextDisplayer()
OB = BuffCoin()
buffers_sprites = pygame.sprite.Group()
buffers_sprites.add(OB)


enemies = pygame.sprite.Group()
enemies.add(Car_Enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(Player)
all_sprites.add(Car_Enemy)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)


while True:
    isBuffed = False

    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"CAR: {str(SCORE)}", True, BLACK)
    coin = font_small.render(f"COIN: {str(COIN)}", True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin, (SCREEN_WIDTH - 100,10))

    if random.randint(1, 50) == 1:
       all_sprites.add(OB)

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(Player, buffers_sprites) and not isBuffed:
        OB.getBuff()
        isBuffed = False
        COIN += 1
        OB.spawn()    

    if pygame.sprite.spritecollideany(Player, enemies):

        time.sleep(1)
                   
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
          
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    

    if SCORE == 97:
        PLAYER_SPEED = 10
        time.sleep(0.5)
        text.Print("SPEED UP", (40, 250), BLACK, BLUE)
        pygame.display.update()
        


    if SCORE == 0:
        time.sleep(1)
        text.Print("YOU WIN", (50, 250), BLACK, GREEN)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
            
        time.sleep(2)
        pygame.quit()
        sys.exit()    
        
    pygame.display.update()
    FramePerSec.tick(FPS)
