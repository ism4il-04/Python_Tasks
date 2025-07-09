from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget,QFileDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QDateEdit, QComboBox, QPushButton, QTableWidget, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QSize, QDate, Qt
from styles import *
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

        self.temp = self.date_tache

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

        self.setStyleSheet(STYLE_SHEET)
        
    def enregistrer(self,dd):
        nom = self.nom_tache.text()
        resp = self.nom_resp.text()
        date = dd
        date.setCalendarPopup(True)
        diff = QComboBox()
        diff.addItems(["easy","normal","hard"])
        diff.setCurrentText(self.tache_diff.currentText())
        etat = self.tache_etat.currentText()
        etat = QComboBox()
        etat.addItems(["pas commencé","en cours","términé"])
        etat.setCurrentText(self.tache_etat.currentText())

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
        na.setFlags(na.flags() | Qt.ItemIsEditable)
        re.setFlags(re.flags() | Qt.ItemIsEditable)
        self.table.setItem(row,0,na)
        self.table.setItem(row,1,re)
        self.table.setCellWidget(row,2,date)
        self.table.setCellWidget(row,3,diff)
        self.table.setCellWidget(row,4,etat)



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
        try:
            # Load from Excel
            file_path, _ = QFileDialog.getSaveFileName(self, "Save to Excel", "", "Excel Files (*.xlsx)")
            self.df = pd.read_excel(file_path)

            # Update table size
            self.table.setRowCount(len(self.df))
            self.table.setColumnCount(len(self.df.columns))
            self.table.setHorizontalHeaderLabels(self.df.columns)

            # Fill the table
            for row in range(len(self.df)):
                # Name & Responsable (text)
                self.table.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row]["Name"])))
                self.table.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row]["Responsable"])))

                # Date (QDateEdit)
                date_str = str(self.df.iloc[row]["Date"])
                date_qt = QDate.fromString(date_str[:10], "yyyy-MM-dd")
                date_edit = QDateEdit()
                date_edit.setDate(date_qt if date_qt.isValid() else QDate.currentDate())
                date_edit.setCalendarPopup(True)
                self.table.setCellWidget(row, 2, date_edit)

                # Difficulté (QComboBox)
                combo_diff = QComboBox()
                combo_diff.addItems(["Facile", "Moyen", "Difficile"])
                combo_diff.setCurrentText(str(self.df.iloc[row]["difficulté"]))
                self.table.setCellWidget(row, 3, combo_diff)

                # État (QComboBox)
                combo_etat = QComboBox()
                combo_etat.addItems(["Non fait", "En cours", "Fait"])
                combo_etat.setCurrentText(str(self.df.iloc[row]["état"]))
                self.table.setCellWidget(row, 4, combo_etat)

        except Exception as e:
            print("Error loading Excel file:", e)

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