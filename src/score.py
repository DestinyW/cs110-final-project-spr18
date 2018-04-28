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

"""Number of points for each frisbee vary by color"""
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

        # draw score
        game_display.blit(message_to_screen("SCORE: {0}".format(score), font, 50, black), (10, 10))

        """ draw high score- guide """
        if score < highscore_int:
            hi_score_message = message_to_screen("HI-SCORE: {0}".format(highscore_int), font, 50, black)
        else:
            highscore_file = open('highscore.dat', "w")
            highscore_file.write(str(score))
            highscore_file.close()
            highscore_file = open('highscore.dat', "r")
            highscore_int = int(highscore_file.read())
            highscore_file.close()
            hi_score_message = message_to_screen("HI-SCORE: {0}".format(highscore_int), font, 50, yellow)

         hi_score_message_rect = hi_score_message.get_rect()

         game_display.blit(hi_score_message, (800-hi_score_message_rect[2]-10, 10))
