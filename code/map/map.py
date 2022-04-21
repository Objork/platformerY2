
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from map.tile import Tile

import settings
class Map(): 
    def __init__(self):  
        self.grid = []
        self.readMap(settings.MAP_FILE)

    def readMap(self, map):

        f = open(map, "r")
        i = 640
        j = 0
        lines = f.readlines()
        for line in reversed(lines):
            try:
                i -= 64
                line = line.rstrip().split(",")
                for k in line:
                    k.strip()
                    k = int(k)
                    if k==1:
                        tile = Tile(j,i, settings.TILE_FLOOR)
                    elif k==0:
                        tile = Tile(j,i, settings.TILE_WALL)
                    elif k==2:
                        tile = Tile(j,i, settings.SPIKE_TRAP)
                    self.grid.append(tile)
                    j+=settings.TEXTURE_SIZE
                j=0
            except:
                raise ValueError()
        f.close()

#960,640
                
