# Lab 9
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
# Note: This file will have a combination of both task 1 & 2
############################################################################################################
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton)
from PySide2.QtGui import QPixmap, QColor
from PySide2.QtCore import Qt, Slot

colors = {
    'Pick A Color': ['',''],
    'Apple Green': [(141, 182, 0), '#8DB600'],
    'Almond': [(238, 217, 196), '#EFDECD'],
    'Aqua': [(0, 255, 255), '#00FFFF']
}

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Colors!")

    self.title = QLabel('CST 205 Color Exchange!')
    self.combo = QComboBox()
    self.combo.addItems(colors)
    self.rgb = QLabel('RGB: ')
    self.hex = QLabel('HEX: ')
    self.displayColor = QPushButton('See The Choosen Color!')

    vbox = QVBoxLayout()
    vbox.addWidget(self.title)
    vbox.addWidget(self.combo)
    vbox.addWidget(self.rgb)
    vbox.addWidget(self.hex)
    vbox.addWidget(self.displayColor)

    self.setLayout(vbox)
    self.combo.currentIndexChanged.connect(self.update_win)
    self.displayColor.clicked.connect(self.open_new_win)

  @Slot()
  def open_new_win(self):
    my_text = self.combo.currentText()
    self.new_win = NewWindow()
    self.new_win.setAutoFillBackground(True)
    backgroundColor = self.new_win.palette()
    backgroundColor.setColor(self.new_win.backgroundRole(), QColor(colors[my_text][0][0], colors[my_text][0][1], colors[my_text][0][2]))
    self.new_win.setPalette(backgroundColor)
    self.new_win.show()


  @Slot() 
  def update_win(self):
    my_text = self.combo.currentText()
    self.rgb.setText(f'RGB: {colors[my_text][0]}')
    self.hex.setText(f'Hex: {colors[my_text][1]}')


app = QApplication(sys.argv)
main = MyWindow()
main.show()
sys.exit(app.exec_())
