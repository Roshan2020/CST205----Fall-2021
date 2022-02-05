##############################################################################################################
# QMainWindowclass
##############################################################################################################
import sys
from PySide2 import QtCore, QtWidgets

app = QtWidgets.QApplication([])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CST 205 Main Window')

mainWin = MainWindow()
mainWin.show()
app.exec_()