from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import settings

class pauseMenu(QToolBar):
    def __init__(self, parent=None):
        QToolBar.__init__(self,parent)
        
        self.createPauseMenu()
    
    def createPauseMenu(self):
        toolButton1 = QAction("Scoreboard", self)
        toolButton1.triggered.connect(self.onButton1Click)
        toolButton1.setCheckable(True)
        self.addAction(toolButton1)
        
        self.addSeparator()

        toolButton2 = QAction("Exit Game", self)
        toolButton2.triggered.connect(self.onButton2Click)
        toolButton2.setCheckable(True)
        self.addAction(toolButton2)
        
        self.setMovable(False)
        self.setVisible(False)

    def onButton1Click(self):
        print("click")

    def onButton2Click(self):
        print("click2")
