import pygame
import random

# model
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
        # set up sprite location
        self.rect.centerx = screen_width / 2
        self.rect.centery = screen_height / 2
        # set other attributes
        self.name = name
        self.speed = 5
        self.jump = 2
        self.health = 3
        self.score = 0

# methods to make the dog move easier
    def moveUp(self):
        self.rect.y -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

    def jumpUp(self):
        self.rect.y += self.jump

# method that will update the score
# number of points for each frisbee varys by color
    def catchFrisbee(self, frisbee):
        # check for collisions
        frisbees_hit_list = pygame.sprite.spritecollide(self.dog, self.frisbees, True)
        if(frisbees_hit_list):
            for frisbee in frisbees_hit_list:
                if(frisbee == white):
                    self.score -= 30
                    self.frisbee.reset_pos()
                    print("player loses 30 points")
                elif(frisbee == yellow):
                    self.score += 0
                    self.frisbee.reset_pos()
                    print("player gets 0 points")
                elif(frisbee == purple):
                    self.score += 10
                    frisbee.reset_pos()
                    print("player gains 10 points")
                elif(frisbee == red):
                    self.score += 20
                    self.frisbee.reset_pos()
                    print("player gains 20 points")
                else:
                    self.frisbees.add(frisbee)
                return self.score

# method that will update the players health
# failed attempt to jump over hurdle decreases health by 1
    def tripOver(self, hurdle):
        if (random.randrange(1)):
            self.health -= 1
            print("jump failed")
        else:
            print("successful jump")
        return True

        # check for collisions
        # dog_hit_hurdle = pygame.sprite.spritecollide(self.dog, self.hurdle, True)
        # if(dog_hit_hurdle):
        #     if (random.randrange(3)):
        #         self.health -= 1
        #         print("jump failed")
        #     else:
        #         self.hurdle.reset.pos()
        #         print("successful jump")
        #     return True
        # if(self.dog.health == 0):
        #     self.dog.kill()
        #     pygame.quit()

# updates players position on the screen
    def update(self):
        print("updating position")
