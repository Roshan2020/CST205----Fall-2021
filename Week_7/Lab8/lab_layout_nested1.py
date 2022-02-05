# Lab 8 Task 2
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
        
        self.setGeometry(0, 0, 400, 300)
        # window title
        self.setWindowTitle("Lab 8 Task 2")

        # outer layer
        main_layout = QVBoxLayout()

        # x1 button in the 1st line of the Window
        v_layout = QVBoxLayout()
        b1 = QPushButton(":)")
        b2 = QPushButton(":(")
        v_layout.addWidget(b1)
        v_layout.addWidget(b2)

        # x2 buttons in the 2nd line of the Window
        h_layout = QHBoxLayout()
        b3 = QPushButton("3:)")
        b4 = QPushButton("O:)")
        h_layout.addWidget(b3)
        h_layout.addWidget(b4)

        # x1 button in the 3rd line of the Window
        v1_layout = QVBoxLayout()
        b5 = QPushButton("B-)")
        b6 = QPushButton("B|")
        v1_layout.addWidget(b5)
        v1_layout.addWidget(b6)

        # add the label of status
        self.my_label = QLabel()
        self.my_label.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.my_label.setText('Test is Ready!')

        # add previous two inner layouts
        main_layout.addLayout(v_layout)
        main_layout.addLayout(h_layout)
        main_layout.addLayout(v1_layout)
        main_layout.addWidget(self.my_label)

        # set outer layout as a main layout of the widget
        self.setLayout(main_layout)
        self.show()

app = QApplication([])

# create an instance of MyWindow
w = MyWindow()

sys.exit(app.exec_())
