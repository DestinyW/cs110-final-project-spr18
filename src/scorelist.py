import json

class scoreList:
    def __init__(self, file_name, score):
        self.score = score
        self.flie_name = file_name

    def loadScores(self):
        with open('topFive.json') as json_data: 
            save_data = json.load(json_data)
        return save_data["high_scores"]

    def saveNewScore(self, score):
        with open('topFive.json') as json_data:  
            load_data = json.load(json_data)
        load_data["high_scores"]
        load_data.append({'score': score}) #add a score to the file
        with open('save_file.json', 'w') as outfile: #save the file
            json.dump(load_data, outfile)
