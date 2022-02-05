##############################################################################################################
# Example for Displaying images with Qt
##############################################################################################################
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        pixmap = QPixmap('images/jeanne_small.jpg')
        pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
   
app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()