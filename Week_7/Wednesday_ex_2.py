##############################################################################################################
# Review
##############################################################################################################
import sys
from PySide2 import QtCore, QtWidgets

app = QtWidgets.QApplication([])

class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show()

ex = Example()
app.exec_()