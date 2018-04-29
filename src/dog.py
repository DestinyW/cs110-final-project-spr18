import pygame

"""model"""

class Dog(pygame.sprite.Sprite):
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
        self.name = name
        self.speed = 10

    """methods to make the dog move easier"""
    def moveUp(self):
        """
        Dog moves up
        """
        TBuffer = 310
        if(self.rect.y > 305):         #prevents dog from going off field
            self.rect.y -= self.speed
        else:
            self.rect.y = TBuffer
    def moveDown(self):
        """
        Dog moves down
        """
        BBuffer = 600
        if(self.rect.y < 605):           #prevents dog from going off screen
            self.rect.y += self.speed
        else:
            self.rect.y = BBuffer
    def moveRight(self):
        """
        Dog moves right
        """
        RBuffer = 640
        if(self.rect.x < 645):           #prevents dog from going off screen
            self.rect.x += self.speed
        else:
            self.rect.x = RBuffer
    def moveLeft(self):
        """
        Dog moves left
        """
        LBuffer = 10
        if(self.rect.x > 5):           #prevents dog from going off screen
            self.rect.x -= self.speed
        else:
                self.rect.x = LBuffer
