import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CropWindow(QMainWindow):
    """This class creates a main window the observe the growth of a simulated crop""" 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")

if __name__ == "__main__":
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()
    
        
