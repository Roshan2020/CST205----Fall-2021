##############################################################################################################
# Minimal Qt Example
##############################################################################################################
import sys

# import classes from PySide6.QtWidgets module
from PySide2.QtWidgets import QApplication, QLabel

# create a QApplication object
my_app = QApplication([])

# create a QLabel object (can include HTML)
my_label = QLabel('<br><p>Hello Everyone!</p><br>')

# display the label (once the main loop is running)
my_label.show()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec_())