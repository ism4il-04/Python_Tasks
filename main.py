from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import pandas as pd
import openpyxl

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("To-do list")

        self.setFixedSize(QSize(800, 500))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()