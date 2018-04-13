import pygame

class Timer(pygame.sprite.Sprite):
    def __init__(self):
        self.time = 0
        self.font = pygame.font.SysFont('monospace', 15)

    def draw(self, screen):
        txt = self.font.render('Time: ' + str(self.time), True, black)
        screen.blit(txt, (0,0))

    def add(self):
        self.time += 1

    def val(self):
        return self.time

    def reset(self):
        self.time = 0
