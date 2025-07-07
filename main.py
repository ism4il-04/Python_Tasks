from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QDateEdit, QComboBox, QPushButton, QTableWidget, QApplication
from PyQt5.QtCore import QSize,QDate
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
        self.nom_tache.setPlaceholderText("nom de tache")
        self.nom_resp = QLineEdit()
        self.nom_resp.setPlaceholderText("nom de responsable de la tache")
        self.date_tache = QDateEdit()
        self.date_tache.setDate(QDate.currentDate())
        self.tache_diff = QComboBox()
        self.tache_diff.addItems(["easy","normal","hard"])
        self.tache_etat = QComboBox()
        self.tache_etat.addItems(["pas commencé","en cours","términé"])
        self.button_enregistrer = QPushButton("Enregistrer")
        self.button_save = QPushButton("save")
        self.button_load = QPushButton("load")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Responsable", "Date","difficulté","état"])

        self.data={
            "tache": ["job"],
            "respo": ["ismail"],
            "date": ["31/07/2004"]
        }
        self.df=pd.DataFrame()

        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout() #où on tape le nom de tache ...

        hbox.addWidget(self.nom_tache)
        hbox.addWidget(self.nom_resp)
        hbox.addWidget(self.date_tache)
        hbox.addWidget(self.tache_diff)
        hbox.addWidget(self.tache_etat)
        hbox.addWidget(self.button_enregistrer)
        vbox.addLayout(hbox)

        vbox.addWidget(self.table)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.button_save)
        hbox1.addWidget(self.button_load)

        vbox.addLayout(hbox1)

        central_widget.setLayout(vbox)

        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()