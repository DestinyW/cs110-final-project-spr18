import pygame
# import random

# health bar
# track and store score
# high scorebroad

"""model"""

# color options
red = (200,0,0)
green = (0,200,0)

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
# # set up sprite location
# self.rect.centerx = width / 2
# self.rect.centery = height / 2
        # set other attributes
        self.name = name
        self.speed = 5
        self.health = 3

"""methods to make the dog move easier"""
    def moveUp(self):
        self.rect.y -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

"""If the player collides with the hurdle, the players health decreases by 1
    If the player dodges the hurdle, the players health stay the same
"""
    def tripOver(self, hurdle):
        if(random.randrange(3)):
            self.health -= 1
            print("falls over hurdle")
            return False
        else:
            print("successfully dodges hurdle")
        return True

# import colors
    def health_bar(self):
        # create a health bar image
        # need 3 different images; 1 fill, 1 half fill, 1 empty
        if self.health == 3:
            # add image
            self.health_bar_color = green
        elif self.health <= 2 and self.health != 0:
            # add image
            self.health_bar_color = yellow
        else:
            self.health_bar_color = red
            # OR
            pygame.quit()
        return pygame.draw.rect(self.health_bar_color, (800,25,25))
        # upper right: (800, 0)
        # upper left: (0,0)

"""health bar- guide"""
    def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 200
    BAR_HEIGHT = 20
    fill = (pct/100 * BAR_LENGTH)
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(surf, GREEN, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

# draw health
    if player.health >= 1:
        game_display.blit(sprites.icon, (10, 50))
        if player.health >= 2:
            game_display.blit(sprites.icon, (10+32+10, 50))
            if player.health >= 3:
                game_display.blit(sprites.icon, (10+32+10+32+10, 50))

"""updates players position on the screen"""
    def update(self):
        print("updating position")
