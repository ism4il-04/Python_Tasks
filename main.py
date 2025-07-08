from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget,QFileDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QDateEdit, QComboBox, QPushButton, QTableWidget, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QSize, QDate, Qt
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
        self.date_tache.setCalendarPopup(True)
        self.tache_diff = QComboBox()
        self.tache_diff.addItems(["easy","normal","hard"])
        self.tache_etat = QComboBox()
        self.tache_etat.addItems(["pas commencé","en cours","términé"])
        self.button_enregistrer = QPushButton("Enregistrer")
        self.button_enregistrer.clicked.connect(self.enregistrer)
        self.button_save = QPushButton("save")
        self.button_save.clicked.connect(self.save)
        self.button_load = QPushButton("load")
        self.button_load.clicked.connect(self.load)
        self.button_clear = QPushButton("clear tasks")
        self.button_clear.clicked.connect(self.clear_all)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Responsable", "Date","difficulté","état"])

        self.df=pd.DataFrame(columns=["Name", "Responsable", "Date","difficulté","état"])

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
        hbox1.addWidget(self.button_clear)

        vbox.addLayout(hbox1)

        central_widget.setLayout(vbox)
        
    def enregistrer(self):
        nom = self.nom_tache.text()
        resp = self.nom_resp.text()
        date = self.date_tache.text()
        diff = self.tache_diff.currentText()
        etat = self.tache_etat.currentText()

        d = {
            "Name": nom,
            "Responsable": resp,
            "Date": date,
            "difficulté": diff,
            "état": etat
        }

        temp = pd.DataFrame([d])
        self.df=pd.concat([self.df,temp],ignore_index=True)
        print("Vous avez ajouté la tache ci dessous")
        print("<====================================================================>")
        print(temp)
        print("<====================================================================>")
        self.clear()
        row = self.table.rowCount()
        self.table.insertRow(row)
        na = QTableWidgetItem(nom)
        re = QTableWidgetItem(resp)
        da = QTableWidgetItem(date)
        df = QTableWidgetItem(diff)
        et = QTableWidgetItem(etat)
        na.setFlags(na.flags() | Qt.ItemIsEditable)
        re.setFlags(re.flags() | Qt.ItemIsEditable)
        da.setFlags(da.flags() | Qt.ItemIsEditable)
        df.setFlags(df.flags() | Qt.ItemIsEditable)
        et.setFlags(et.flags() | Qt.ItemIsEditable)
        self.table.setItem(row,0,na)
        self.table.setItem(row,1,re)
        self.table.setItem(row,2,da)
        self.table.setItem(row,3,df)
        self.table.setItem(row,4,et)



    def clear(self):
        self.nom_tache.clear()
        self.nom_resp.clear()
        self.tache_diff.setCurrentText("easy")
        self.tache_etat.setCurrentText("pas commencé")
        self.date_tache.setDate(QDate.currentDate())

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save to Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            self.df.to_excel(file_path,index=False)
            QMessageBox.information(self, "Succès", "saved successfully")

    def load(self):
        """_summary_
        """        
        file_path, _ = QFileDialog.getSaveFileName(self, "Save to Excel", "", "Excel Files (*.xlsx)")
        self.table.setRowCount(0)
        if file_path:
            try:
                temp = pd.read_excel(file_path)


            except:
                pass

    def clear_all(self):
        # Clear QTableWidget
        self.table.setRowCount(0)

        # Clear DataFrame
        self.df = pd.DataFrame(columns=["Name", "Responsable", "Date","difficulté","état"])

        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()