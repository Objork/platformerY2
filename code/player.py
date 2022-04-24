from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import settings
class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(settings.PLAYER_TEXTURE))
        self.jumping = False
        self.grounded = True
        self.jump_heigth = 0
        self.oldPos = 0
        self.setScale(1.2)
        self.setPos(settings.STARTING_POS_X, settings.STARTING_POS_Y)
        

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
        
        
        dy += 10
        
        if (self.jumping):
            dy -= 32
            self.jump_heigth += 1
            if self.jump_heigth > 10:
                self.jumping = False
                self.jump_heigth = 0
        
        
        self.setPos(self.x()+dx, self.y()+dy)
        
    
    
    def collided(self):
        if (self.grounded):
            self.setPos(self.x(), self.oldPos.y())
        else:
            self.setPos(self.oldPos)
        if not (self.jumping):
            self.grounded = True
        
    
    
    def death(self):
        self.setPos(settings.STARTING_POS_X, settings.STARTING_POS_Y)

    def set_jumping(self):
        self.jumping = True
        self.grounded = False
        

    