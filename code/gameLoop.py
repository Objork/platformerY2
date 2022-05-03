from player import Player
from scoreSystem import ScoreSystem
from pauseMenu import pauseMenu
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
        
        self.scoreBoard = ScoreSystem()

        self.timer.start(16, self)

        self.player = Player()

        self.addItem(self.player)

        self.view.centerOn(settings.WINDOW_WIDTH/2, self.player.y())
        
        self.pauseMenu = pauseMenu()
 
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
        self.game_loop()
        self.update()
           
    def game_loop(self):
        self.scoreBoard.timerCounter()
        if not self.paused:
            self.pauseMenu.setVisible(False)
            self.view.centerOn(self.player)
            self.player.update(self.keys_pressed)
            for i in self.map.spikeballs:
                i.update()
            self.collision()
        
        else:
            self.pauseMenu.move(self.player.x(), self.player.y()-settings.TEXTURE_SIZE)
            self.pauseMenu.setVisible(True)
        score = self.scoreBoard.getScore()
        #print(score)

    def setView(self):
            self.view = QGraphicsView(self)
            self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.show()
            self.view.setFixedSize(settings.WINDOW_HEIGHT,settings.WINDOW_WIDTH)
            
    
    def collision(self):
        tilesInBounds = self.get_tile_on_player(self.player.sceneBoundingRect())
        for  j in self.map.spikeballs:
            if j.sceneBoundingRect().intersects(self.player.sceneBoundingRect()):
                self.player.death()
                self.spawnCoins()
        for  k in self.map.coins:
            if k.sceneBoundingRect().intersects(self.player.sceneBoundingRect()):
                self.scoreBoard.coinCollected()
                self.removeItem(k)
        c= 0
        if len(tilesInBounds) == 0:
            self.player.gravityTrue()
        
        else:
            for i in tilesInBounds:
                c += 1
                print("THE TILE:", c , i.scenePos().x(), i.scenePos().y())
                left, right, bottom, top = self.collidingWhere(i)
                self.player.collided(left, right, top, bottom, i)
                
                if (i.is_death()):
                    self.player.death()
                    self.spawnCoins()                
                if (i.is_exit()):
                    self.gameEnded()

    def get_tile_on_player(self, playerBoundry):
        tilesInBounds = []
        for tile in self.map.grid:
            if tile.is_walkable():
                if tile.sceneBoundingRect().intersects(playerBoundry):
                    tilesInBounds.append(tile)           
        return tilesInBounds

    def collidingWhere(self, tile):
        left = self.player.scenePos().x() < tile.x() + settings.TEXTURE_SIZE
     
        right = self.player.scenePos().x()  + self.player.sceneBoundingRect().width() > tile.x() 
        
        top = self.player.scenePos().y() < tile.y() + settings.TEXTURE_SIZE 
       
        bottom = self.player.scenePos().y() + self.player.sceneBoundingRect().height() > tile.y()
        
        return left, right, top, bottom

    def setMap(self):
        for i in self.map.grid:
            self.addItem(i)
        self.spawnSpikeBalls()
        self.spawnCoins()

    def spawnCoins(self):
        for k in self.map.coins:
            self.addItem(k)

    def spawnSpikeBalls(self):
        for j in self.map.spikeballs:
            self.addItem(j)


    def gameEnded(self):
        self.paused = True
        self.addPixmap(self.endingScreen)
        self.scoreBoard.writeScores()