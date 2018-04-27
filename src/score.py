import pygame

# color options
black = (0,0,0)

class Score(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('monospace', 15)

    def draw_score(self, screen):
        self.txt = font.render('Score: ' + str(self.score), True, black)
        screen.blit(self.txt, (0,0))

    def add_score(self, frisbee):
        if(frisbee == white):
            self.score -= 30
            print("player loses 30 points")
        elif(frisbee == yellow):
            self.score += 0
            print("player gets 0 points")
        elif(frisbee == purple):
            self.score += 10
            print("player gains 10 points")
        elif(frisbee == red):
            self.score += 20
            print("player gains 20 points")
        else:
            self.frisbees.add(frisbee)
        return self.score

    def val(self):
        return self.score

    def reset(self):
        self.score = 0

    def draw_gameover(self, screen):
        self.txt = font.render('GAMEOVER! You Scored ' + str(self.score) + ' points. Press \'Again!\' to restart.', True, black)
        screen.blit(txt, (400 - text.get_width() / 2, 100))
