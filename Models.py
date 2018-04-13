import sys
import pygame
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

class Dog(pygame.sprite.Sprite):
    def __init__(self, name):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        self.image = pygame.image.load('dog.png').convert()
        self.image.set_colorkey(COLOR)
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        # set up sprite location
        self.rect.center_x = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        # set other attributes
        self.name = name

    def update(self):
        self.speed_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed_y = -5
        if keys[pygame.K_DOWN]:
            self.speed_y = 5
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

    def jumpUp(self, x, y, pose):

    def tripOver(self, pose):

    def catchFrisbee(self):

class Frisbee(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('frisbee.png').convert()
        self.image.set_colorkey(COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.speed_x = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.x = random.randrange(-3,3)

class Hurdle(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hurdle.png').convert()
        self.image.set_colorkey(COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.speed_x = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.speed_x = random.randrange(-3, 3)

class Timer(pygame.sprite.Sprite):
    def __init__(self):
        self.time = 0
        self.font = pygame.font.SysFont('monospace', 15)

    def draw(self, screen):
        txt = self.font.render('Time: ' + str(self.timme), True, black)
        screen.blit(txt, (0,0))

    def add(self):
        self.time += 1

    def val(self):
        return self.time

    def reset(self):
        self.time = 0

class Score(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('monospace', 15)

    def draw(self, screen):
        txt = self.font.render('Score: ' + str(self.score), True, black)
        screen.blit(txt, (0,0))

    def add(self):
        self.score += 1

    def val(self):
        return self.score

    def reset(self):
        self.score = 0

    def draw_gameover(self, screen):
        txt = self.font.render('GAMEOVER! You Scored ' + str(self.score) + ' points. Press \'Again!\' to restart.', True, black)
        screen.blit(txt, (400 - text.get_width() / 2, 100))
