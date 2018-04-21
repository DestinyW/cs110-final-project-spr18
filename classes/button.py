import pygame

# model
class Button(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y, name):
        pygame.sprite.Sprite.__init__(self)    # initialize all the sprite functionality
        self.image = pygame.image.load(image_file).convert_alpha()   # create surface object image
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.rect.x = x
        self.rect.y = y
        self.name = name
