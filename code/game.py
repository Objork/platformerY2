from player import Player
from scoreSystem import ScoreSystem
from pauseMenu import pauseMenu
from map.coin import Coin
import settings

from map.map import Map

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Game(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self,parent)
        self.keys_pressed = set()
        self.timer = QBasicTimer()
        self.paused = False
        self.mapSet = True
        self.maps = []
        self.currentMap = 0
        for i in settings.MAP_FILES:
            map = Map(i)
            self.maps.append(map)
        
        self.setView() 

        self.setMap()
        
        self.scoreBoard = ScoreSystem()

        self.timer.start(16, self)

        self.view.centerOn(settings.WINDOW_WIDTH/2, self.player.y())
        
        self.pauseMenu = pauseMenu()

        self.pauseMenu.addScore(self.scoreBoard)
 
        self.addWidget(self.pauseMenu)
        
        self.pauseMenu.move(self.view.x()/2, self.view.y()/2)

        self.endingScreen = QPixmap(settings.ENDING_SCREEN)

        self.setBackgroundBrush(QBrush(QColor(24,36,68)))

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())
        if Qt.Key_Escape in self.keys_pressed:
            self.paused = not self.paused

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.gameLoop()
        self.update()
           
    def gameLoop(self):
        self.scoreBoard.timerCounter()
        if not self.paused:
            self.pauseMenu.setVisible(False)
            self.view.centerOn(self.player)
            self.player.update(self.keys_pressed)
            for i in self.maps[self.currentMap].spikeballs:
                i.update()
            self.collision()
        else:
            self.pauseMenu.move(self.player.x(), self.player.y()-settings.TEXTURE_SIZE)
            self.pauseMenu.setVisible(True)

    def setView(self):
            self.view = QGraphicsView(self)
            self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.show()
            self.view.setFixedSize(settings.WINDOW_HEIGHT,settings.WINDOW_WIDTH)
            
    
    def collision(self):
        tilesInBounds = self.get_tile_on_player(self.player.sceneBoundingRect())
        for  j in self.maps[self.currentMap].spikeballs:
            if j.sceneBoundingRect().intersects(self.player.sceneBoundingRect()):
                self.player.death()
                self.scoreBoard.playerDeath()
                self.spawnCoins()
        for k in self.maps[self.currentMap].coins:
            if k.sceneBoundingRect().intersects(self.player.sceneBoundingRect()):
                if isinstance(self.itemAt(k.scenePos().x(), k.scenePos().y(), QTransform()), Coin):
                    self.removeItem(k)
                    self.scoreBoard.coinCollected()
        c= 0
        if len(tilesInBounds) == 0:
            self.player.gravityTrue()
        else:
            for i in tilesInBounds:
                c += 1
                self.player.collided(i)
                if (i.is_death()):
                    self.player.death()
                    self.scoreBoard.playerDeath()
                    self.spawnCoins()                
                if (i.is_map_exit()):
                    self.player.setPos(settings.STARTING_POS_X, settings.STARTING_POS_Y)
                    self.exitMap()
                if (i.is_exit()):
                    self.gameEnded()
                

    def get_tile_on_player(self, playerBoundry):
        tilesInBounds = []
        for tile in self.maps[self.currentMap].grid:
            if tile.is_walkable():
                if tile.sceneBoundingRect().intersects(playerBoundry):
                    tilesInBounds.append(tile)           
        return tilesInBounds


    def setMap(self):
        for i in self.maps[self.currentMap].grid:
            self.addItem(i)
        self.spawnSpikeBalls()
        self.spawnCoins()
        self.player = Player()
        self.addItem(self.player)
        self.player.setPos(settings.STARTING_POS_X, settings.STARTING_POS_Y)
        self.paused = False

    def spawnCoins(self):
        for k in self.maps[self.currentMap].coins:
            self.addItem(k)

    def spawnSpikeBalls(self):
        for j in self.maps[self.currentMap].spikeballs:
            self.addItem(j)

    def exitMap(self):
        self.scoreBoard.saveCoins()
        self.scoreBoard.coins = 0
        if self.mapSet == False:
            self.paused = True
            self.currentMap += 1
            self.setMap()
        else:
            self.mapSet = False
    
    def gameEnded(self):
        w, h = self.endingScreen.size().width(), self.endingScreen.size().height()
        self.addPixmap(self.endingScreen)
        self.view.fitInView(QRectF(0,0, w,h), Qt.KeepAspectRatioByExpanding)
        self.update()
        self.paused = True
        self.scoreBoard.writeScores()