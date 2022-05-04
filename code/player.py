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
        
        if dy or dx != 0:
            self.walking = True
        
        self.setPos(self.x()+dx, self.y()+dy) 
        
    
    
    def collided(self, tile):
   
        #print(self.grounded)

        #print(tile.x(), tile.y())
       
        
        left = self.sceneBoundingRect().bottomLeft().x() < tile.sceneBoundingRect().bottomRight().x()
       
        right = self.sceneBoundingRect().bottomRight().x() > tile.sceneBoundingRect().bottomLeft().x()
  
        top = self.sceneBoundingRect().top() < tile.sceneBoundingRect().bottom()
    
        bottom =  self.sceneBoundingRect().bottom() >  tile.sceneBoundingRect().top()
      
        topbottom = tile.sceneBoundingRect().top() < self.sceneBoundingRect().top()
        if (bottom):
            
            print("Player BOTTOM: ", self.sceneBoundingRect().bottom())
            print("TOP: ", tile.sceneBoundingRect().top())
            print("BOTTOM: ", tile.sceneBoundingRect().bottom())
            print("PLAYER TOP: ", self.sceneBoundingRect().top())
            print()

            self.grounded = True
            
        
        
                 
        
        
     
    def death(self):
        self.setPos(settings.STARTING_POS_X, settings.STARTING_POS_Y)

    def set_jumping(self):
        self.jumping = True

    def gravityTrue(self):

        self.grounded = False
        #print("GRAVITY ON")

        
        

    