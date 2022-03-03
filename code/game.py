
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import math
import sys

class Game:
   def __init__(self):

        self.app = QApplication(sys.argv)

        self.window = QWidget()

        self.window.setFixedSize(QSize(1600, 1200))

        self.player = Player(self.window)
        
        self.player.setFocus()

    
class Player(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 192, 192)
        self.setPixmap(QPixmap('y2_2022_05868_platformer\code\content\squidman.png'))

    def keyPressEvent(self, event):
        W = False
        A = False
        S = False
        D = False
        
        if event.key() == Qt.Key_W:
            W = True

        if event.key() == Qt.Key_A:
            A = True

        if event.key() == Qt.Key_S:
            S = True

        if event.key() == Qt.Key_D:
            D = True
        
        twoKeyInput = ((W or S) and (A or D))
        
        if (twoKeyInput):
            if(A):
                self.move((self.x() - 5) / math.sqrt(2), self.y())
            elif(D):
                self.move((self.x() + 5)/ math.sqrt(2), self.y())  
            
            if (W):
                self.move(self.x(), (self.y() - 5) / math.sqrt(2))
            elif (S):
                self.move(self.x(), (self.y() + 5) / math.sqrt(2)) 
        else:
            if(A):
                self.move(self.x() - 5, self.y())
            elif(D):
                self.move(self.x() + 5, self.y())  
            if (W):
                self.move(self.x(), self.y() - 5)
            elif (S):
                self.move(self.x(), self.y() + 5) 

               

        