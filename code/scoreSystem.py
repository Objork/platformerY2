

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random
import string
import settings

class ScoreSystem(): 
    def __init__(self):  
        self.coins = 0
        self.deathCounter = 0
        self.timer = 0
        self.score = 0
        self.scores = []

    def readScores(self):
        f = open(settings.SCORES, "r")
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            self.scores.append(line)
        f.close()

    def writeScores(self):
        f = open(settings.SCORES, "a")
        code = self.get_random_letter_code()
        f.write(str(len(self.scores)+1) + code + ": " + str(self.score) + '\n')
        f.close()
    
    def get_random_letter_code(self):
        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(3))
        return code

    def coinCollected(self):
        self.coins +=1

    def playerDeath(self):
        self.deathCounter += 1
        self.coins = 0

    def timerCounter(self):
        self.timer += 1 * 0.01

    def getScore(self):
        self.score = self.timer + self.coins - self.deathCounter
        return self.score
         