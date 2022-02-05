import sys
import requests
from PySide2.QtWidgets import (QApplication, QWidget, QLabel)
from PySide2.QtGui import QPixmap, QImage

image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Amedeo_Modigliani_-_Portrait_of_Jeanne_Hebuterne%2C_Seated%2C_1918_-_Google_Art_Project.jpg/527px-Amedeo_Modigliani_-_Portrait_of_Jeanne_Hebuterne%2C_Seated%2C_1918_-_Google_Art_Project.jpg'

class MainWindow(QWidget):
    def __init__(self):
        self.my_image = QImage()
        self.my_image.loadFromData(requests.get(image_url).content)
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap(self.my_image))
        self.image_label.show()

app = QApplication([])
main = MainWindow()
app.exec_()