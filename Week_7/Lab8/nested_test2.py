##############################################################################################################
# Test #2 for Layout Nested
##############################################################################################################
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Slot
from PySide2 import QtCore


my_qt_app = QApplication(sys.argv)
my_window = QWidget()
my_window.setGeometry(0, 0, 400, 300)
my_window.setWindowTitle('Lab 8 Task 2')
my_label = QLabel(my_window)
my_label.setGeometry(QtCore.QRect(0, 0, 300, 50))
my_label.setText('Test is Ready!')
button1 = QPushButton("Button 1", my_window)
button1.move(100, 70)
button2 = QPushButton("Button 2", my_window)
button2.move(150, 200)
my_window.show()
sys.exit(my_qt_app.exec_())