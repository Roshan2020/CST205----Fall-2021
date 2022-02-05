import sys
from PySide2.QtWidgets import (QApplication, QWidget, 
                                QLabel, QVBoxLayout)
from PySide2.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.x = QLabel()
        self.y = QLabel('Pretty Flowers')
        self.z = QPixmap('new_flowers.jpg')
        self.x.setPixmap(self.z)
        my_layout = QVBoxLayout()
        my_layout.addWidget(self.x)
        self.setLayout(my_layout)

app = QApplication([])
a = MyWindow()
a.show()
app.exec_()