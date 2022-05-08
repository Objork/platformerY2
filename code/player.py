from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import settings
class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(settings.PLAYER_TEXTURE))
        self.jumping = False
        self.grounded = False
        self.jump_heigth = 0
        self.setScale(1.2)
        self.setPos(settings.STARTING_POS_X, settings.STARTING_POS_Y)
        self.oldPos = self.scenePos()
        

    def update(self, keys_pressed):
        dx = 0
        dy = 0
        self.oldPos = self.scenePos()
        if Qt.Key_A in keys_pressed:
            dx -= 6
        
        if Qt.Key_D in keys_pressed:
            dx += 6

        if Qt.Key_Space in keys_pressed and self.grounded == True:
            self.set_jumping()
        
        if not self.grounded:
            dy += 10
        else:
            dy = 0
        
        if (self.jumping):
            dy -= 32
            self.jump_heigth += 1
            if self.jump_heigth > 10:
                self.jumping = False
                self.jump_heigth = 0
        
        
        self.setPos(self.x()+dx, self.y()+dy) 
        
    
    
    def collided(self, tile):
    
        left = self.sceneBoundingRect().left() < tile.sceneBoundingRect().right() and self.sceneBoundingRect().left() > tile.sceneBoundingRect().left()
       
        right = self.sceneBoundingRect().right() > tile.sceneBoundingRect().left() and self.sceneBoundingRect().right() < tile.sceneBoundingRect().right()
  
        top = self.sceneBoundingRect().top() > tile.sceneBoundingRect().top() and self.sceneBoundingRect().top() < tile.sceneBoundingRect().bottom()
    
        bottom =  self.sceneBoundingRect().bottom() >  tile.sceneBoundingRect().top() and self.sceneBoundingRect().bottom() < tile.sceneBoundingRect().bottom()
      
        center = tile.sceneBoundingRect().contains(self.sceneBoundingRect().center())


        if (bottom):
            self.grounded = True
        
        if (((right or left) and not bottom and not self.grounded) or top):
            
            self.gravityTrue()
            self.setPos(self.oldPos)
  
        if center:
            self.setPos(self.oldPos)
       
     
    def death(self):
        self.setPos(settings.STARTING_POS_X, settings.STARTING_POS_Y)

    def set_jumping(self):
        self.jumping = True

    def gravityTrue(self):
        self.grounded = False

        
        

    