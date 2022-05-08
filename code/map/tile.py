from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import settings

class Tile(QGraphicsPixmapItem):
    def __init__(self, x, y, tileText, parent=None):
            QGraphicsPixmapItem.__init__(self, parent)
            self.setPixmap(QPixmap(tileText))
            self.setPos(x,y)
            self.walkable = False    
            self.death = False
            self.exit = False
            self.exitMap = False
            if tileText == settings.TILE_FLOOR:
                self.walkable = True
            
            elif tileText == settings.SPIKE_TRAP:
                self.death = True
                self.walkable = True

            elif tileText == settings.TILE_DOOR:
                self.exit = True
                self.walkable = True

            elif tileText == settings.MAP_EXIT:
                self.exitMap = True
                self.walkable = True
    
    def is_walkable(self):
        return self.walkable

    def is_death(self):
        return self.death

    def is_exit(self):
        return self.exit

    def is_map_exit(self):
        return self.exitMap