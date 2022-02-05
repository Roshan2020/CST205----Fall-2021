# importing the required libraries
from PySide2.QtWidgets import (QApplication, QPushButton,
                                QHBoxLayout, QVBoxLayout, QWidget, QLabel)
from PySide2.QtCore import Slot
from PySide2 import QtCore
import sys
  
class Window(QWidget):
    def __init__(self):
        super().__init__()
  
        # set the title
        self.setWindowTitle("Move")
  
        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)
  
        # x1 button in the 1st line of the Window
        self.h_layout = QHBoxLayout()
        self.b1 = QPushButton("A")
        self.h_layout.addWidget(self.b1)
  
        # moving the widget
        # move(left, top)
        self.b1.move(300, 200)

        main_layout = QHBoxLayout()
        main_layout.addLayout(self.h_layout)
  
        self.setLayout(main_layout)
        # show all the widgets
        self.show()
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec_())