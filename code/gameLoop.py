
from player import Player
import settings
from map.map import Map
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class GameLoop(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self,parent)

        self.keys_pressed = set()

        self.timer = QBasicTimer()
        
        self.paused = False

        self.map = Map()
        
        self.setView() 

        self.setMap()

        self.timer.start(16, self)

        self.player = Player()

        self.addItem(self.player)

        self.view.centerOn(settings.WINDOW_WIDTH/2, self.player.y())
        
        self.pauseMenu = QToolBar()

        self.createPauseMenu()
        
        self.addWidget(self.pauseMenu)

        self.pauseMenu.move(self.view.x()/2, self.view.y()/2)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())
        if Qt.Key_Escape in self.keys_pressed:
            self.paused = not self.paused

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

   
    def timerEvent(self, event):
        self.game_loop()
        self.update()
        
        

    def game_loop(self):
        if not self.paused:
            self.pauseMenu.setVisible(False)
            self.view.centerOn(self.player)
            self.player.update(self.keys_pressed)
            self.collision()
        
        else:
            self.pauseMenu.move(self.player.x(), self.player.y()-settings.TEXTURE_SIZE)
            self.pauseMenu.setVisible(True)

    def setView(self):
            self.view = QGraphicsView(self)
            self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.show()
            self.view.setFixedSize(960,640)
            
    
    def collision(self):
        tilesInBounds = self.get_tile_on_player(self.player.sceneBoundingRect())
        for i in tilesInBounds:
            if (i.is_walkable()):
                self.player.collided()

    def get_tile_on_player(self, playerBoundry):
        tilesInBounds = []
        for tile in self.map.grid:
            if tile.sceneBoundingRect().intersects(playerBoundry):
                tilesInBounds.append(tile)
        return tilesInBounds
            
    def setMap(self):
        for i in self.map.grid:
            self.addItem(i)


    def createPauseMenu(self):
        toolButton = QToolButton()
        toolButton.setText("Scoreboard")
        toolButton.setCheckable(True)
        toolButton.setAutoExclusive(True)
        self.pauseMenu.addWidget(toolButton)
        toolButton = QToolButton()
        toolButton.setText("Exit Game")
        toolButton.setCheckable(True)
        toolButton.setAutoExclusive(True)
        self.pauseMenu.addWidget(toolButton)
        self.pauseMenu.setMovable(False)
        self.pauseMenu.setVisible(False)