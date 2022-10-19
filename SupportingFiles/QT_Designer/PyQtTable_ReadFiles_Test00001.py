import csv
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import (QWidget, QLabel, QDialog, QHBoxLayout, QComboBox, QApplication)

data = []

with open('E:\GSReddy\PythonProjects\SampleData\Employee Sample Data.csv', 'r') as stream:
    for rowdata in csv.reader(stream):
        data.append(rowdata)

labels = data[0]

del data[0]

class Dlg(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.layout = QGridLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()

        self.tabs.addTab(self.tab1, "Tab1")

        nb_row = len(data)
        nb_col = len(data[0])

        self.tab1.layout = QVBoxLayout(self)

        self.table = QTableWidget()
        self.table.setRowCount(nb_row)
        self.table.setColumnCount(nb_col)
        self.table.setHorizontalHeaderLabels(labels)

        for row in range(nb_row):
            for col in range(nb_col):
                item = QTableWidgetItem(str(data[row][col]))
                self.table.setItem(row, col, item)

        self.tab1.layout.addWidget(self.table)
        self.tab1.setLayout(self.tab1.layout)
        self.layout.addWidget(self.tabs, 0, 0)

w = Dlg()
w.resize(600, 400)
w.setWindowTitle('Populating QTableWidget with CSV file')
w.setWindowFlags(Qt.WindowStaysOnTopHint)
w.show()