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

# methods to make the dog move easier,
######since we have the screen divided into 2 halves the dog can run along these methods have to be more focused on where it is I think
#######Assuming the dog starts in the front half of the feild dog should be centered on (pixles) x=400 (halfway through the screen) y=142.
    def moveUp(self):
        self.rect.y -= self.speed
    ######if dog is in Lower field half and Up arrow is pressed, the dog moves to x+400 y=296
    ######if the dog is in the upper field half and the Up arrow is pressed, nothing happens
    def moveDown(self):
        self.rect.y += self.speed
    ######if dog is in upper field half and down arrow is pressed, the dog moves to x=400 y=142
    ######if the dog is in the Lower field half and the down arrow is pressed, nothing happens

    def jumpUp(self, y):
        self.rect.y += self.jump
    ######The dogs location should go from x=400 to y+=140
    ######the dog should switch to a different sprite for a second here (if possible)
    ######https://www.pygame.org/docs/ref/time.html might have what we need
    
    #####def runDog(self)
    ######if possible every set period of time 80 milliseconds or so the dog should switch from GSDogRun1.png to GSDogRun2.png, same link above should help
    


# method that will update the score
# number of points for each frisbee varys by color
    def catchFrisbee(self, frisbee):
        ######## check for collisions   <=    This segment needs to be moved to the controller
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

# method that will update the time remaning
# failed attempt to jump over hurdle decreases time by 3 seconds
########There should be a function in the Timer class (called something like 'decrease time') that minues 3 seconds from the timer; and a function in the dog class called 'jump' where the dog jumps (and if possible, switches to the GSDogJump.png)

#########The controller will check for a collision between the hurdle and the dog and if there is a collision, call decrease_time() and if there is not then does nothing

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
