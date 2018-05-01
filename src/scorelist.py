import json

class HighScore():
    def __init__(self, filename, score):
        with open(filename, 'r+') as file:
            try:
                myfile = json.loads(file)
                self.score_list = myfile['highscore']
                # for line in file.readlines():
                #     high_score = int(line)
                #     self.score_list.append(high_score)
                self.score_list.append(score)
                temp = len(score_list)
                self.score_list.sort(reverse=True)
                if temp > 5:
                    temp = 5
                    self.score_list.pop()
                # for i in range(temp):
                #     file.write(str(self.score_list[i]+ "/n")
                myfile["highscore"] = self.score_list
                json.dumps(myfile,file)
            except:
                high_score = 0
                print("There is no high score yet")

    def draw_highscore(self):
        myfont.render.draw_highscore("High Scores: " +str(self.score_list))

        # if self.score > self.highscore:
        #     self.highscore = self.score
        # self.draw_text("New High Score!: " + str(self.highscore), 22, (0,0,0), (0,0))
        # with open(filename, 'w') as file:
        #     file.write(str(self.score))
        # else:
        #     self.draw_text("High Score: " + str(self.highscore), 22, (0,0,0), (0,0))

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


# class Scorelist:
#     def __init__(self, file_name, score):
#         self.score = score
# #        self.save_data = {}
#         self.load_data = {}
#         self.file_name = file_name
#
#     def loadScores(self):
#         """
#         Function that will load the scores
#         """
#         with open(self.file_name) as json_data: #open file
#             self.save_data = json.load(json_data) #load json data and store as "save_data"
#         return self.save_data
#
#     def updateScores(self, score):
#         """
#         Function that will add a score and save it
#         """
#         with open(self.file_name) as json_data:  #open
#             self.load_data = json.load(json_data)  #load json data and storeas "load_data"
#         self.load_data.append(score) #add score to the file
#         self.load_data.sort(reverse=True) #sort list from largest to smallest
#         self.load_data = self.load_data[:5]    #only want the top 5
#         with open(self.file_name, 'w') as outfile: #save the file
#             json.dump(self.load_data, outfile)
#         return self.load_data
