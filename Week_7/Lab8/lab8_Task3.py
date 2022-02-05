# Lab 8 Task 3
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
############################################################################################################

import sys
from PySide2.QtWidgets import (QApplication, QPushButton,
                                QHBoxLayout, QVBoxLayout, QWidget, QLabel)
from PySide2.QtCore import Slot
from PySide2 import QtCore

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        #self.setGeometry(0, 0, 400, 300)
        # window title
        self.setWindowTitle("Lab 8 Task 3")

        # outer layer
        main_layout = QVBoxLayout()


        # x2 buttons in the 2nd line of the Window
        b2 = QPushButton(":)")
        b3 = QPushButton(":(")
        b2.move(150, 70)
        b3.move(150, 140)
        b2.clicked.connect(self.b2_on_click)
        b3.clicked.connect(self.b3_on_click)

        # add the label of status
        self.my_label = QLabel()
        self.my_label.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.my_label.setText('Test is Ready!')

        main_layout.addWidget(b2)
        main_layout.addWidget(b3)
        main_layout.addWidget(self.my_label)

        # set outer layout as a main layout of the widget
        self.setLayout(main_layout)
        self.show()
    
    @Slot()
    def b2_on_click(self):
        self.my_label.setText('User clicked Button 1st meaning he/she is HAPPY!')
        self.repaint()
    
    @Slot()
    def b3_on_click(self):
        self.my_label.setText('User clicked Button 2nd meaning he/she is SAD!')
        self.repaint()

app = QApplication([])

# create an instance of MyWindow
w = MyWindow()

sys.exit(app.exec_())
