import json
import pygame

class HighScore():
    def __init__(self, filename, score):
        with open(filename, 'r+') as file:
            try:
                myfile = json.load(file)
                self.score_list = myfile['highscores']
                self.score_list.append(score)
                temp = len(self.score_list)
                self.score_list.sort(reverse=True)
                if temp > 5:
                    temp = 5
                    self.score_list.pop()
                myfile["highscores"] = self.score_list
            except:
                high_score = 0
                print("There is no high score yet")
        with open(filename,'w') as file:
            json.dump(myfile,file)
        
    def draw_highscore(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        score_list = []
        for i in self.score_list:
            score_list.append(myfont.render(str(i),True,(255,255,255)))
        return score_list
