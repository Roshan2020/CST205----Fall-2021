##############################################################################################################
# Spinbox and Dial example
##############################################################################################################
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
                                                  QSpinBox, QDial)
class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinbox = QSpinBox()
        layout = QHBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)
        self.setWindowTitle("Spinbox and Dial")
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)
        
app = QApplication([])
ex = Form()
ex.show()
app.exec_()
