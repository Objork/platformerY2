import math
from player import Player

from map.map import Map
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

TILE_WALL = 'y2_2022_05868_platformer\code\content\MapTiles\walltile.png'
TILE_FLOOR = 'y2_2022_05868_platformer\code\content\MapTiles\platform'
class GameLoop(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self,parent)

        self.keys_pressed = set()

        self.timer = QBasicTimer()

        self.map = Map()

        self.setView() 

        self.setMap()

        self.timer.start(16, self)

        self.player = Player()

        self.addItem(self.player)

        self.view.centerOn(self.player.scenePos())


       

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

   
    def timerEvent(self, event):
        self.game_loop()
        self.update()
        

    def game_loop(self):
        self.player.update(self.keys_pressed)
        self.collision()

    def setView(self):
            self.view = QGraphicsView(self)
            self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.show()
            self.view.setFixedSize(960,640)
            self.setSceneRect(0,0,960,640)
    
    def collision(self):
        for i in self.map.grid:
            if i.is_walkable():
                if self.is_colliding(i):
                    self.player.collided()

    def is_colliding(self, other):
        x_collision = (math.fabs(self.player.x() - other.x()) * 1.5) < (self.player.width + other.width)
        y_collision = (math.fabs(self.player.y() - other.y()) * 1.5) < (self.player.height + other.height)
        return (x_collision and y_collision)
            
    def setMap(self):
        for i in self.map.grid:
            self.addItem(i)