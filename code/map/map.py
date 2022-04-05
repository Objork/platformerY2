
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from map.tile import Tile

TILE_WALL = 'y2_2022_05868_platformer\code\content\MapTiles\walltile.png'
TILE_FLOOR = 'y2_2022_05868_platformer\code\content\MapTiles\platform'

class Map(): 
    def __init__(self):  
        self.grid = []
        self.readMap()

    def readMap(self):

        f = open("y2_2022_05868_platformer\code\map\mapSetting.txt", "r")
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
                        tile = Tile(j,i, TILE_FLOOR)
                    elif k==0:
                        tile = Tile(j,i, TILE_WALL)
                    print(j, i)
                    self.grid.append(tile)
                    j+=64
                j=0
            except:
                raise ValueError()
        f.close()

#960,640
                
