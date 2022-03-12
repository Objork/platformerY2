from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap('y2_2022_05868_platformer\code\content\squidman.png'))

    def update(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_A in keys_pressed:
            dx -= 5
        if Qt.Key_D in keys_pressed:
            dx += 5 
        if Qt.Key_W in keys_pressed:
            dy -= 5
        if Qt.Key_S in keys_pressed:
            dy += 5
        self.setPos(self.x()+dx, self.y()+dy)