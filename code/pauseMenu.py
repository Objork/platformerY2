from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class pauseMenu(QToolBar):
    def __init__(self, parent=None):
        QToolBar.__init__(self,parent)
        
        self.createPauseMenu()
        self.scoreBoard = object()
        self.popWindow = QMessageBox()
        
        self.popWindow.setWindowTitle("SCORES")

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
        self.popWindow.show()
        self.popWindow.setText(self.scoreBoard.messageBoxLine)
       

    def onButton2Click(self):
        print("DOESN'T WORK YOU GOT TO EXIT FROM THE WINDOW")

    def addScore(self, scoreBoard):
        self.scoreBoard = scoreBoard
