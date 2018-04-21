import pygame
import random

# model
class Frisbee(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image_file):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        self.image = pygame.image.load(image_file).convert_alpha()
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # set other attributes
        self.name = name + str(id(self))
        self.speed = random.randrange(4,8)

    def reset_pos(self):
        self.rect.x = random.randrange(-1,-2)
        self.rect.y = random.randrange(screen_height - self.rect.width)
    
    ######I think we need a throw function where every random amount of time a new frisbee is thrown
        ########https://www.pygame.org/docs/ref/time.html can probably help with this again
    ######it pics randomly from a list of the png files or something?
    #######the frisbees are also going to have to move at a set speed from x=800 (right of screen) to x=0 (left of screen)
    #######the only height the frisbees can be at is y = 280 (jump from lower field to catch) or y = 434 (jump from upper field)

    def update(self):
        self.rect.x -= 1
        # resets any frisbees that slides off the screen
        if self.rect.x > screen_width + 10:
            self.reset_pos()
