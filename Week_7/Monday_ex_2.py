##############################################################################################################
# Minimal Qt example using OOP
##############################################################################################################
import sys
from PySide2 import QtCore, QtWidgets

class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text = QtWidgets.QLabel("Hello World")
        # use vertical box layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

# create the Qt Application
app = QtWidgets.QApplication([])

# create and show the example
ex = Example()
ex.show()

# run the main Qt loop
sys.exit(app.exec_())