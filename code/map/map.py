

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from map.movingTrap import MovingTrap
from map.tile import Tile
from map.coin import Coin

import settings

class Map(): 
    def __init__(self, i):  
        self.grid = []
        self.spikeballs = []
        self.coins = []
        self.readMap(i)

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
                    elif k==4:
                        tile = Tile(j,i, settings.TILE_WALL)
                        spikeball = MovingTrap(j,i)
                        self.spikeballs.append(spikeball)
                    elif k==3:
                        tile = Tile(j,i, settings.TILE_WALL)
                        coin = Coin(j,i)
                        self.coins.append(coin)
                    elif k==5:
                        tile = Tile(j,i, settings.TILE_DOOR)
                    elif k==6:
                        tile = Tile(j,i, settings.MAP_EXIT)
                    self.grid.append(tile)
                    j+=settings.TEXTURE_SIZE
                j=0
            except ValueError as e:
                print("Creation of map gone wrong")
        f.close()
                
