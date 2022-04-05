from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap('y2_2022_05868_platformer\code\content\squidman.png'))
        self.jumping = False
        self.height = 64
        self.width = 64
        self.grounded = True
        self.jump_heigth = 0
        self.jumpCooldown = 0
        self.setScale(2.0)
        

    def update(self, keys_pressed):
        dx = 0
        dy = 0
        
        if Qt.Key_A in keys_pressed:
            dx -= 5
        
        if Qt.Key_D in keys_pressed:
            dx += 5 
            
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
        self.setPos(self.x(), self.y() - 5)
        self.grounded = True

    def set_jumping(self):
        self.jumping = True
        self.grounded = False
        


    