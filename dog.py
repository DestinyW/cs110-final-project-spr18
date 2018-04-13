import pygame
import random

# COLORS
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#model
class Dog(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        self.image = pygame.image.load('dog.png').convert_alpha()
        self.image.set_colorkey(COLOR)
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        # set up sprite location
        self.rect.center_x = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        # set other attributes
        self.name = name + str(id(self))
        self.speed = 5
        self.health = 1

# methods to make the dog move easier
    def moveUp(self):
        self.rect.y -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

    def jumpUp(self):
            self.rect.y += 2

    def catchFrisbee(self):

    def tripOver(self, hurdle):
        if (random.randrange(1)):
            self.health -= 1
            print("jump failed")
        else:
            print("successful jump")
        return True

    def update(self):
        print("updating position")
