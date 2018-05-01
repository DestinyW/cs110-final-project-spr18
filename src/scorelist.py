import json

class Scorelist:
    def __init__(self, file_name, score):
        self.score = score
#        self.save_data = {}
        self.load_data = {}
        self.file_name = file_name

    def loadScores(self):
        """
        Function that will load the scores
        """
        with open(self.file_name) as json_data: #open file
            self.save_data = json.load(json_data) #load json data and store as "save_data"
        return self.save_data

    def updateScores(self, score):
        """
        Function that will add a score and save it
        """
        with open(self.file_name) as json_data:  #open
            self.load_data = json.load(json_data)  #load json data and storeas "load_data"
        self.load_data.append(score) #add score to the file 
        self.load_data.sort(reverse=True) #sort list from largest to smallest
        self.load_data = self.load_data[:5]    #only want the top 5
        with open(self.file_name, 'w') as outfile: #save the file
            json.dump(self.load_data, outfile)
        return self.load_data
