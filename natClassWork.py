import sys
import pygame

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
        self.speed_y = 0

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

    def catchDisk(self):

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
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

class Score(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score
