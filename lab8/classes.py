import pygame, random
from pygame.locals import *

inv_speed = 15
SPEED = 5
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


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

    def getBuff(self, player_sprite):
        global SCORE
        global SPEED
       
        SCORE += 5
        if SPEED > 10:
            SPEED -= 5