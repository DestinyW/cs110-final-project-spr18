# import json

class HighScore():
    def __init__(self, filename, score):
        filename = "HighScore.txt"
        with open(filename, 'r') as file:
            try:
                self.highscore = int(file.read())
                self.score = score
            except:
                self.highscore = 0
                print("There is no high score yet")

    def draw_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("New High Score!: " + str(self.highscore), 22, (0,0,0), (0,0))
            with open(filename, 'w') as file:
                file.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, (0,0,0), (0,0))

    # def __init__(self, file_name, score):
    #     self.score = score
    #     self.flie_name = file_name
    #
    # def loadScores(self):
    #     with open('topFive.json') as json_data:
    #         save_data = json.load(json_data)
    #     return save_data["high_scores"]
    #
    # def saveNewScore(self, score):
    #     with open('topFive.json') as json_data:
    #         load_data = json.load(json_data)
    #     load_data["high_scores"]
    #     load_data.append({'score': score}) #add a score to the file
    #     with open('save_file.json', 'w') as outfile: #save the file
    #         json.dump(load_data, outfile)
