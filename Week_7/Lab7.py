# Lab 7
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
############################################################################################################
# ----------------------------------- Task 2 ---------------------------------------------------------------
# QtWidget      : QMessageBox
# Description   : This allows the file to create a message box in order to alert or inform the user of any 
#                 current status

# ----------------------------------- Task 3 ---------------------------------------------------------------
import sys

# import classes from PySide6.QtWidgets module
from PySide2.QtWidgets import QApplication, QLabel

# create a QApplication object
my_app = QApplication([])

# create a QLabel object (can include HTML)
my_label = QLabel('<br><p>Hi My Name is Roshan Indika Menik Arachchi Menik Arachchige</p><br>')

# display the label (once the main loop is running)
my_label.show()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec_())