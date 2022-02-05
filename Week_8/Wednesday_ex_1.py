##############################################################################################################
# Quiz 2 of Week 8
##############################################################################################################
import sys
from PySide2.QtWidgets import (QApplication, QWidget, 
                                QLabel, QVBoxLayout)
from PySide2.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.x = QLabel()
        self.y = QLabel("Jeanne")
        pmap = QPixmap("images/jeanne.jpg")
        self.x.setPixmap(pmap)
        my_layout = QVBoxLayout()
        my_layout.addWidget(self.x)
        self.setLayout(my_layout)

app = QApplication([])
a = MyWindow()
a.show()
sys.exit(app.exec_())