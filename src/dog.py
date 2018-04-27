import pygame
# import random

# model
class Dog(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        # initialize all the sprite functionality
        pygame.sprite.Sprite.__init__(self)
        # create surface object image
        self.original_image = pygame.image.load(image_file).convert_alpha()
        self.image = self.original_image.copy()
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        # set up sprite location
        self.rect.centerx = screen_width / 2
        self.rect.centery = screen_height / 2
        # set other attributes
        self.moving_up = False
        self.moving_down = False
        self.jumping = False
        self.jump_ticker = 0
        self.falling = False
        # self.size
        self.speed = 10
        self.velocity = 0
        self.angle = 0

    def movement(self):
        if not self.jumping:
            if self.moving_up == True:
                self.rect.centery -= self.speed
            elif self.moving_down == True:
                self.rect.centery += self.speed

    def is_jumping(self):
        if self.jumping == True:
            # self.dog_jump = pygame.image.load("GSDogJump.png")
            self.rotate = pygame.transform.rotate("GSDogJump.png", self.angle)
            self.rect = self.rotate.get_rect()
            self.angle += 1 % 90
            self.image = self.rotate
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
        else:


    def is_falling(self):
        if not self.jumping:
            if self.falling == True:
                self.rotate = pygame.transform.rotate("GSDogRun1.png", self.angle)
                self.angle += 1 % 90
                self.image = self.rotate
                self.rect = self.image.get_rect()
                self.rect.center = (x,y)
            else:

    def update(self):
        if self.jumping:
            self.is_jumping()
        elif self.falling:
            self.is_falling()
        else:
            self.movement()
        print("updating position")






# methods to make the dog move easier.
    def moveUp(self):
        self.rect.y -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

    def jumpUp(self, y):
        if self.jump == True:
            old_rect = self.rect
            #change image and make sure to set rect.x,y to old_rect.x,y
            self.gravity = 0
            self.vector = [0,0]
            # gravity and vector

    def jump(self):
        if self.falling == False:
            if self.jump_ticker < 10:
                #self.rect.y += 10
                self.jump_ticker+=1
                new_size = (self.original_size[0]*(1+self.jump_ticker/10),self.original_size[1]*(1+self.jump_ticker/10))
            else:
                self.Falling = True
        else:
            if self.jump_ticker > 0:
                self.rect.y += 10:
                self.jump_ticker-=1
            else:
                self.Falling = False
                self.jumping = False
        #temp = pos_change(self.vector,self.gravity,time) #make sure to define pos_change
        #self.rect.x+=temp[0]
        #self.rect.y+=temp[1]


# updates players position on the screen
    def update(self):
        # add jumping state
        # can also add the image here
        if self.jump == True:
            # need sin and cos
        print("updating position")
