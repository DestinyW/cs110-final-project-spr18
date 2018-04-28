import pygame
import random

# model
class Wall(pygame.sprite.Sprite):
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
        self.speed = random.randrange(4,8)    # hurdle speed should be constant for all of them, not random

    #########def scrollAcross()
    #######we will also need a function where the hurdles appear from the from x=800 (right of screen) to x=0 (left of screen)
    #######the hurdles should always be centered on y = 142 (lower field) or y = 296 (upper field) and it should be randomized which one (upper or lower) it is

    def reset_pos(self):
        self.rect.x = random.randrange(-1,-2)
        self.rect.y = random.randrange(screen_height - self.rect.width)

    def update(self):
        self.rect.x -= 1
        # resets any walls that slides off the screen
        if self.rect.x > screen_width + 10:
            self.reset_pos()
