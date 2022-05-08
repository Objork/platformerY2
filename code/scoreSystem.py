from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import string
import random
import settings

class ScoreSystem(): 
    def __init__(self):  
        self.coins = 0
        self.totalCoins = 0
        self.deathCounter = 0
        self.timer = 0
        self.score = 0
        self.scores = []
        self.saved = False
        self.messageBoxLine = ''
        self.readScores()

    def readScores(self):
        f = open(settings.SCORES, "r")
        lines = f.readlines()
        for line in lines:
            self.messageBoxLine += line
            line = line.rstrip()
            self.scores.append(line)
        f.close()

    def writeScores(self):
        if not self.saved:
            f = open(settings.SCORES, "a")
            code = self.get_random_letter_code()
            f.write(str(len(self.scores)+1) + code + ": " + str(self.getScore()) + '\n')
            f.close()
            self.saved = True
    
    def get_random_letter_code(self):
        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(3))
        return code

    def coinCollected(self):
        self.coins = self.coins + 1

    def playerDeath(self):
        self.deathCounter += 1 * 0.5
        self.coins = 0

    def timerCounter(self):
        self.score -= 0.000016

    def getScore(self):
        self.score =  self.totalCoins * 100 - self.timer - self.deathCounter
        if self.score < 0:
            self.score = 0
        return self.score

    def saveCoins(self):
        self.totalCoins += self.coins