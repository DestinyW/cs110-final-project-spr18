import pygame
import time

class Timer(pygame.sprite.Sprite):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.stop_time = self.clock + 180000
        # reduce by 3000
        self.font = pygame.font.SysFont('monospace', 15)
        self.frame_count = 0
        self.frame_rate = 60
        self.start_time = 90
        self.pause = 3
        # self.time = 0
        # self.font = pygame.font.Font('monospace', 15)

    # def draw(self, screen):
    #     self.txt = font.render('Time: ' + str(self.time), True, black)
    #     screen.blit(txt, (0,0))
    #
    # def add(self):
    #     self.time += 1
    #
    # def val(self):
    #     return self.time
    #
    # def reset(self):
    #     self.time = 0

    def minus_3(self):
        now =
        now = pygame.time.get_ticks()
        if now - self.last >== self.cooldown:
            self.last = now
            spawn_dog()



        # if (random.randrange(3)):
        #     self.health -= 1
        #     print("jump failed")
        # else:
        #     self.hurdle.reset.pos()
        #     print("successful jump")
        # return True
