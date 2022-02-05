##############################################################################################################
# Example for QLineEdit
##############################################################################################################
import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout)
from PySide2.QtCore import Slot

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.my_lineedit = QLineEdit("What's your favorite song?")
        self.my_lineedit.setMinimumWidth(250)
        self.my_lineedit.selectAll()
        self.my_btn = QPushButton("Submit")
        self.my_lbl = QLabel('')
        self.my_btn.clicked.connect(self.on_submit)
        self.my_lineedit.returnPressed.connect(self.on_submit)
        vbox.addWidget(self.my_lineedit)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_lbl)
        self.setLayout(vbox)

    @Slot()
    def on_submit(self):
        your_song = self.my_lineedit.text()
        self.my_lbl.setText(f'Your favorite song is {your_song}')


app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()