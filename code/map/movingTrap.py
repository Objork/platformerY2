from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random

import settings

class MovingTrap(QGraphicsPixmapItem):
    def __init__(self, x, y, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(settings.SPIKE_BALL))
        self.setPos(x,y)
        self.moveRandom = random.randint(80,140)
        self.moveCount = 0
        self.moveSwitch = True

    def update(self):
        dx = 0
        if self.moveSwitch:
            dx += 3
            self.moveCount += 1
            if self.moveCount > self.moveRandom:
                self.moveCount = 0
                self.moveSwitch = not self.moveSwitch
        elif not self.moveSwitch:
            dx -= 3
            self.moveCount += 1
            if self.moveCount > self.moveRandom:
                self.moveCount = 0
                self.moveSwitch = not self.moveSwitch

        self.setPos(self.x()+dx, self.y())