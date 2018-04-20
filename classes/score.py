import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('monospace', 15)

    def draw(self, screen):
        txt = self.font.render('Score: ' + str(self.score), True, black)
        screen.blit(txt, (0,0))

    def add(self):
        self.score += 1

    def val(self):
        return self.score

    def reset(self):
        self.score = 0

    def draw_gameover(self, screen):
        txt = self.font.render('GAMEOVER! You Scored ' + str(self.score) + ' points. Press \'Again!\' to restart.', True, black)
        screen.blit(txt, (400 - text.get_width() / 2, 100))
