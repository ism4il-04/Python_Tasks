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
        self.nom_tache = QLineEdit()
        self.nom_resp = QLineEdit()
        self.date_tache = QLineEdit()
        self.button_enregistrer = QPushButton("Enregistrer")

        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout() #où on tape le nom de tache ...

        hbox.addWidget(self.nom_tache)
        hbox.addWidget(self.nom_resp)
        hbox.addWidget(self.date_tache)
        hbox.addWidget(self.button_enregistrer)
        vbox.addLayout(hbox)

        central_widget.setLayout(vbox)

        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()