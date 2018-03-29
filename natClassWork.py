class Dog:
    def __init__(self, x, y, pose):
        self.x = x
        self.y = y
        self.pose = pose

    def moveForward(self, x, y):

    def moveBack(self, x, y):

    def jumpUp(self, x, y, pose):

    def tripOver(self, pose):

    def catchDisk(self):

class Disk:
    def __init__(self, x, y, speed, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
              
class Hurdle:
    def __init__(self, x, y):
        self.x = x
        self.y = y  

class Timer:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

class Score:
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score
