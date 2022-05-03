
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import settings

class Coin(QGraphicsPixmapItem):
    def __init__(self, x, y, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(settings.COIN))
        self.setPos(x,y)
        self.setScale(0.8)
