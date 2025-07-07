from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from layout_colorwidget import Color

import sys
import pandas as pd
import openpyxl

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("To-do list")
        self.setFixedSize(QSize(800, 500))
        self.setWindowIcon(QIcon("icon.ico"))
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()