##############################################################################################################
# Example for Group Box
##############################################################################################################
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, 
                                  QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel('QLineEdit: ')
        self.line_edit = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.line_edit)

        gbox1 = QGroupBox('Group Box 1')
        gbox1.setLayout(hbox1)

        self.label2 = QLabel('Here are some buttons:')
        b1 = QPushButton('button 1')
        b2 = QPushButton('button 2')

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(b1)
        hbox3.addWidget(b2)

        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox2)
        vbox2.addLayout(hbox3)

        gbox2 = QGroupBox("Group Box 2")
        gbox2.setLayout(vbox2)

        mbox = QVBoxLayout()
        mbox.addWidget(gbox1)
        mbox.addWidget(gbox2)

        self.setLayout(mbox)
        self.setWindowTitle("CST 205 App")

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()