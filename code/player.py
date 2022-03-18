from sre_constants import JUMP
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap('y2_2022_05868_platformer\code\content\squidman.png'))
        self.jumping = False
        self.height = 32
        self.width = 32
        self.jump_heigth = 0

    def update(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_A in keys_pressed:
            dx -= 5
        if Qt.Key_D in keys_pressed:
            dx += 5 
        if Qt.Key_S in keys_pressed:
            dy += 5
        if Qt.Key_Space in keys_pressed:
            if not (self.jumping):
                self.set_jumping()

        if not (self.jumping):
            dy += 10
        
        if (self.jumping):
            dy -= 15
            self.jump_heigth += 1
            if self.jump_heigth > 10:
                self.jumping = False
        
        self.setPos(self.x()+dx, self.y()+dy)


    def collided(self):
        self.setPos(self.x(), self.y() - 5)

    def set_jumping(self):
        self.jumping = True