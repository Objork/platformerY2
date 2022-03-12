from re import T
from player import Player
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class GameLoop(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.keys_pressed = set()

        self.timer = QBasicTimer()
        
        self.timer.start(16, self)

        self.player = Player()
        
        self.addItem(self.player)

        self.setView()

        self.drawGrid()

    def setView(self):
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(800,600)
        self.setSceneRect(0,0,800,600)

    def drawGrid(self):
        
        for x in range(0, 600, 32):
            for y in range(0, 800, 32):
                tile = QPixmap("y2_2022_05868_platformer\code\content\walltile.png")
                self.addPixmap(tile)
                

        

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_loop()
        self.update()

    def game_loop(self):
        self.player.update(self.keys_pressed)



            