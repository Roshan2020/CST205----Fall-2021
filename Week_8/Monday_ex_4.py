##############################################################################################################
# Example for QComboBox
##############################################################################################################
import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PySide2.QtCore import Slot


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_list = ["Pick a value", "vanilla", "chocolate", "raspberry", "coconut"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(self.my_list)
        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.addWidget(self.my_combo_box)
        vbox.addWidget(self.my_label)

        self.setLayout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_label.setText(f'You chose {self.my_list[my_index]}.')


app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()