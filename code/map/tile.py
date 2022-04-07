from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import settings
class Tile(QGraphicsPixmapItem):
    def __init__(self, x, y, tileText, parent=None):
            QGraphicsPixmapItem.__init__(self, parent)
            self.setPixmap(QPixmap(tileText))
            self.setPos(x,y)
            if tileText == settings.TILE_FLOOR:
                self.walkable = True
            else:
                self.walkable = False     
    
    def is_walkable(self):
        return self.walkable