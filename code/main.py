
from gameLoop import GameLoop
from  PyQt5.QtWidgets import *

import sys

def main():
    app = QApplication(sys.argv)
     
    GameLoop()
    
    app.exec()

if __name__ == "__main__":
    main()