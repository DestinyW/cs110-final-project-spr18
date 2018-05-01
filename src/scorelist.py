import json

class Scorelist:
    def __init__(self, file_name, score):
        self.score = score
        #self.flie_name = file_name

    def loadScores(self):
        """
        Function that will load the scores
        """
        with open(file_name) as json_data: #open file
            save_data = json.load(json_data) #load json data and store as "save_data"
        return save_data

    def saveNewScore(self, score):
        """
        Function that will add a score and save it
        """
        with open(file_name) as json_data:  #open
            load_data = json.load(json_data)  #load json data and storeas "load_data"
        load_data.append(score) #add score to the file 
        load_data.sort(reverse=True) #sort list from largest to smallest
        load_data = load_data[:5]    #only want the top 5
        with open(file_name, 'w') as outfile: #save the file
            json.dump(load_data, outfile)
            data = JSON.stringify(load_data)  #convert json data to string
        return data
