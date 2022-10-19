import os
import sys
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtGui import * # QPalette, QLinearGradient, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
    QInputDialog, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QMenu


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.table = QtGui.QTableWidget()
        self.table.setColumnCount(3)
        self.setCentralWidget(self.table)
        data1 = ['row1','row2','row3','row4']
        data2 = ['1','2.0','3.00000001','3.9999999']

        self.table.setRowCount(4)

        for index in range(4):
            item1 = QtGui.QTableWidgetItem(data1[index])
            self.table.setItem(index,0,item1)
            item2 = QtGui.QTableWidgetItem(data2[index])
            self.table.setItem(index,1,item2)
            self.btn_sell = QtGui.QPushButton('Edit')
            self.btn_sell.clicked.connect(self.handleButtonClicked)
            self.table.setCellWidget(index,2,self.btn_sell)

    def handleButtonClicked(self):
        button = QtGui.qApp.focusWidget()
        # or button = self.sender()
        index = self.table.indexAt(button.pos())
        if index.isValid():
            print(index.row(), index.column())

