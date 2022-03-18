from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Tile(QGraphicsPixmapItem):
    def __init__(self, x, y, tileText, parent=None):
            QGraphicsPixmapItem.__init__(self, parent)
            self.setPixmap(QPixmap(tileText))
            self.setPos(x,y)
            if tileText == "y2_2022_05868_platformer\code\content\MapTiles\platform":
                self.walkable = True
            else:
                self.walkable = False
            self.height = 32
            self.width = 32
    
    def is_walkable(self):
        return self.walkable