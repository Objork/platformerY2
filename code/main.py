from game import Game                 

from  PyQt5.QtWidgets import *
 
import sys

def main(): 
 
    app = QApplication(sys.argv) 
    
    Game()    
    
    app.exec()
 
if __name__ == "__main__":
    main() 