from PyQt5 import uic
import os
import sys
import PyQt5
from PyQt5.QtGui import * # QPalette, QLinearGradient, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
    QInputDialog, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox

class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("columna.ui", self)
        self.tabla.insertRow(self.tabla.rowCount())
        self.tabla.setItem(self.tabla.rowCount() - 1, 2, QTableWidgetItem("sdsd"))
        self.tabla.setItem(self.tabla.rowCount() - 1, 1, QTableWidgetItem("sdsd"))
        self.tabla.insertRow(self.tabla.rowCount())
        self.tabla.setItem(self.tabla.rowCount() - 1, 1, QTableWidgetItem("sdsd"))
        self.boton.clicked.connect(lambda: self.tabla.setShowGrid(False))  # Limpiar sin dejar la rejilla en la tabla
        # self.check.clicked.connect(lambda: self.tabla.selectedItems().clear())  # Función para eliminar solo una row
        self.check.clicked.connect(lambda: self.tabla.removeRow(self.tabla.currentRow()))

app = QApplication([])
p = Principal()
p.show()
app.exec_()
