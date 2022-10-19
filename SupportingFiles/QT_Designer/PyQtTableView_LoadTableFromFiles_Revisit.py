#!/usr/bin/python3
# -*- coding:utf-8 -*-
import csv, codecs
import os
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QFile, QAbstractTableModel, Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,QComboBox, QApplication, QTableView)

global fileName

# ---------------------------------------------------------------------------------------------------------------------
df = pd.read_csv(fileName) #'E:\GSReddy\PythonProjects\SampleData\FinancialsSampleData_Comma.csv')

class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
    def rowCount(self, parent=None):
        return self._data.shape[0]
    def columnCount(self, parnet=None):
        return self._data.shape[1]
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
# ---------------------------------------------------------------------------------------------------------------------

class MyWindow(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = ""
        self.fname = "Liste"
        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setStyleSheet(stylesheet(self))
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setShowGrid(True)
        self.tableView.setGeometry(10, 50, 200, 445)
        self.model.dataChanged.connect(self.finishedEdit)

        self.pushButtonLoad = QtWidgets.QPushButton(self)
        self.pushButtonLoad.setText("Load CSV")
        self.pushButtonLoad.clicked.connect(self.loadCsv)
        self.pushButtonLoad.setFixedWidth(80)
        self.pushButtonLoad.setStyleSheet(stylesheet(self))

        self.pushButtonWrite = QtWidgets.QPushButton(self)
        self.pushButtonWrite.setText("Save CSV")
        self.pushButtonWrite.clicked.connect(self.writeCsv)
        self.pushButtonWrite.setFixedWidth(80)
        self.pushButtonWrite.setStyleSheet(stylesheet(self))

        self.pushButtonPreview = QtWidgets.QPushButton(self)
        self.pushButtonPreview.setText("Print Preview")
        self.pushButtonPreview.clicked.connect(self.handlePreview)
        self.pushButtonPreview.setFixedWidth(80)
        self.pushButtonPreview.setStyleSheet(stylesheet(self))

        self.pushButtonPrint = QtWidgets.QPushButton(self)
        self.pushButtonPrint.setText("Print")
        self.pushButtonPrint.clicked.connect(self.handlePrint)
        self.pushButtonPrint.setFixedWidth(80)
        self.pushButtonPrint.setStyleSheet(stylesheet(self))

        self.pushAddRow = QtWidgets.QPushButton(self)
        self.pushAddRow.setText("Add Row")
        self.pushAddRow.clicked.connect(self.addRow)
        self.pushAddRow.setFixedWidth(80)
        self.pushAddRow.setStyleSheet(stylesheet(self))

        self.pushDeleteRow = QtWidgets.QPushButton(self)
        self.pushDeleteRow.setText("Delete Row")
        self.pushDeleteRow.clicked.connect(self.removeRow)
        self.pushDeleteRow.setFixedWidth(80)
        self.pushDeleteRow.setStyleSheet(stylesheet(self))

        self.pushAddColumn = QtWidgets.QPushButton(self)
        self.pushAddColumn.setText("Add Column")
        self.pushAddColumn.clicked.connect(self.addColumn)
        self.pushAddColumn.setFixedWidth(80)
        self.pushAddColumn.setStyleSheet(stylesheet(self))

        self.pushDeleteColumn = QtWidgets.QPushButton(self)
        self.pushDeleteColumn.setText("Delete Column")
        self.pushDeleteColumn.clicked.connect(self.removeColumn)
        self.pushDeleteColumn.setFixedWidth(86)
        self.pushDeleteColumn.setStyleSheet(stylesheet(self))

        self.pushClear = QtWidgets.QPushButton(self)
        self.pushClear.setText("Clear")
        self.pushClear.clicked.connect(self.clearList)
        self.pushClear.setFixedWidth(60)
        self.pushClear.setStyleSheet(stylesheet(self))

        self.CbxSelectDelimiter = QComboBox(self) # creating a combo box widget
        #self.CbxSelectDelimiter.setGeometry(20, 150, 120, 40) # setting geometry of combo box
        self.CbxSelectDelimiter.addItems(["5","10","20","50","100"]) # adding items to combo box
        self.CbxSelectDelimiter.setEditable(False)
        #self.CbxSelectDelimiter.setFixedWidth(50)
        #self.CbxSelectDelimiter.setFixedHeight(26)
        self.CbxSelectDelimiter.activated[str].connect(self.onSelected) # Call the custom method if any item is selected
        self.CbxSelectDelimiter.setStyleSheet(stylesheet(self))

        # Set the label after the ComboBox
        self.cbxDelimiterLabel = QLabel('Rows : ', self)
        self.cbxDelimiterLabel.adjustSize()

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.pushButtonLoad, 0, 0)
        grid.addWidget(self.pushButtonWrite, 0, 1)
        grid.addWidget(self.pushAddRow, 0, 2)
        grid.addWidget(self.pushDeleteRow, 0, 3)
        grid.addWidget(self.pushAddColumn, 0, 4)
        grid.addWidget(self.pushDeleteColumn, 0, 5)
        grid.addWidget(self.pushClear, 0, 6)
        grid.addWidget(self.pushButtonPreview, 0, 7)
        grid.addWidget(self.cbxDelimiterLabel,0, 8, QtCore.Qt.AlignRight)
        grid.addWidget(self.CbxSelectDelimiter, 0, 9)
        grid.addWidget(self.pushButtonPrint, 0, 10, 1, 1, QtCore.Qt.AlignRight)
        grid.addWidget(self.tableView, 2, 0, 1, 9)
        self.setLayout(grid)

        item = QtGui.QStandardItem()
        self.model.appendRow(item)
        self.model.setData(self.model.index(0, 0), "", 0)
        self.tableView.resizeColumnsToContents()

    def onSelected(self, txtVal):
        try:
            print("Selected Value/Rows to Be Fetched : " + txtVal)
            txtVal = "\nYou have selected: " + txtVal
            print("From onSelected Value : " + self.CbxSelectDelimiter.currentText())
            #self.cbxDelimiterLabel.setText(txtVal)
            index = self.CbxSelectDelimiter.currentIndex() # finding the current item index  in combo box
            print("From onSelected Index : " +  str(index)) # showing content on the screen though label
        except IndexError:
            print('Index Error')
        except ValueError:
            print('Value Error')
        except ZeroDivisionError:
            print("ZeroDivisionError Occurred and Handled")
        except NameError:
            print("NameError Occurred and Handled")
        else:
            print('This is else, sometimes executed')
        finally:
            print('This is finally, always executed')
            # raise NameError("Hi there")  # Raise Error

            # raise the ValueError
            # raise ValueError("Eg. please add money in your account")

    def loadCsv(self, fileName):
        dataFileDir = 'E:\GSReddy\PythonProjects\SampleData\Employee Sample Data.csv'
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File..",
                                                             dataFileDir, # (QtCore.QDir.homePath()),
                                                            "Tab Delimited (*.tsv);;Comma Separated (*.csv);;Excel Files (*.xls);;Excel Files (*.xlsx)"
                                                             )

        if fileName:
            print('From - loadCsv : '+ fileName + ' - FileExtension : ' + fileName[-3:])
            ff = open(fileName, 'r')
            mytext = ff.read()
            #            print(mytext)
            ff.close()
            f = open(fileName, 'r')
            with f:
                self.fname = os.path.splitext(str(fileName))[0].split("/")[-1]
                self.setWindowTitle(self.fname)
                print("';' Count : "+ str(mytext.count(';')) +
                      " - 'tab' Count : "+ str(mytext.count('\t')) +
                      " - '|' Count : " + str(mytext.count('|')) +
                      " - ',' Count : " + str(mytext.count(','))
                     )
                if (mytext.count('\t') > mytext.count('|')) or (mytext.count('\t') > mytext.count('|')):
                    print('Condition Block')
                    reader = csv.reader(f, delimiter='\t')
                    self.model.clear()
                    for row in reader:
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.tableView.resizeColumnsToContents()
                elif mytext.count(',') > mytext.count('|'):
                    print("Elif ',' Block")
                    reader = csv.reader(f, delimiter=',')
                    self.model.clear()
                    for row in reader:
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.tableView.resizeColumnsToContents()
                    #self.tableView.setVerticalHeader()
                elif mytext.count(',') < mytext.count('|'):
                    print("Elif '|' Block")
                    reader = csv.reader(f, delimiter='|')
                    self.model.clear()
                    for row in reader:
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.tableView.resizeColumnsToContents()
                else:
                    print("Else Block")
                    reader = csv.reader(f, delimiter=';')
                    self.model.clear()
                    for row in reader:
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.tableView.resizeColumnsToContents()

    def writeCsv(self, fileName):
        # find empty cells
        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                myitem = self.model.item(row, column)
                if myitem is None:
                    item = QtGui.QStandardItem("")
                    self.model.setItem(row, column, item)
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File",
                                                            (QtCore.QDir.homePath() + "/" + self.fname + ".csv"),
                                                            "CSV Files (*.csv);;Excel Files (*.xls);;Excel Files (*.xlsx)")
        if fileName:
            print(fileName)
            f = open(fileName, 'w')
            with f:
                writer = csv.writer(f, delimiter='\t')
                for rowNumber in range(self.model.rowCount()):
                    fields = [self.model.data(self.model.index(rowNumber, columnNumber),QtCore.Qt.DisplayRole)
                              for columnNumber in range(self.model.columnCount())]
                    writer.writerow(fields)
                self.fname = os.path.splitext(str(fileName))[0].split("/")[-1]
                self.setWindowTitle(self.fname)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.setFixedSize(1000, 700)
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        # find empty cells
        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                myitem = self.model.item(row, column)
                if myitem is None:
                    item = QtGui.QStandardItem("")
                    self.model.setItem(row, column, item)
        printer.setDocName(self.fname)
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        model = self.tableView.model()
        table = cursor.insertTable(model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)

    def removeRow(self):
        model = self.model
        indices = self.tableView.selectionModel().selectedRows()
        for index in sorted(indices):
            model.removeRow(index.row())

    def addRow(self):
        item = QtGui.QStandardItem("")
        self.model.appendRow(item)

    def clearList(self):
        self.model.clear()

    def removeColumn(self):
        model = self.model
        indices = self.tableView.selectionModel().selectedColumns()
        for index in sorted(indices):
            model.removeColumn(index.column())

    def addColumn(self):
        count = self.model.columnCount()
        print(count)
        self.model.setColumnCount(count + 1)
        self.model.setData(self.model.index(0, count), "", 0)
        self.tableView.resizeColumnsToContents()

    def finishedEdit(self):
        self.tableView.resizeColumnsToContents()

    def contextMenuEvent(self, event):
        self.menu = QtWidgets.QMenu(self)
        # copy
        copyAction = QtWidgets.QAction('Copy', self)
        copyAction.triggered.connect(lambda: self.copyByContext(event))
        # paste
        pasteAction = QtWidgets.QAction('Paste', self)
        pasteAction.triggered.connect(lambda: self.pasteByContext(event))
        # cut
        cutAction = QtWidgets.QAction('Cut', self)
        cutAction.triggered.connect(lambda: self.cutByContext(event))
        # delete selected Row
        removeAction = QtWidgets.QAction('delete Row', self)
        removeAction.triggered.connect(lambda: self.deleteRowByContext(event))
        # add Row after
        addAction = QtWidgets.QAction('insert new Row after', self)
        addAction.triggered.connect(lambda: self.addRowByContext(event))
        # add Row before
        addAction2 = QtWidgets.QAction('insert new Row before', self)
        addAction2.triggered.connect(lambda: self.addRowByContext2(event))
        # add Column before
        addColumnBeforeAction = QtWidgets.QAction('insert new Column before', self)
        addColumnBeforeAction.triggered.connect(lambda: self.addColumnBeforeByContext(event))
        # add Column after
        addColumnAfterAction = QtWidgets.QAction('insert new Column after', self)
        addColumnAfterAction.triggered.connect(lambda: self.addColumnAfterByContext(event))
        # delete Column
        deleteColumnAction = QtWidgets.QAction('delete Column', self)
        deleteColumnAction.triggered.connect(lambda: self.deleteColumnByContext(event))
        # add other required actions
        self.menu.addAction(copyAction)
        self.menu.addAction(pasteAction)
        self.menu.addAction(cutAction)
        self.menu.addSeparator()
        self.menu.addAction(addAction)
        self.menu.addAction(addAction2)
        self.menu.addSeparator()
        self.menu.addAction(addColumnBeforeAction)
        self.menu.addAction(addColumnAfterAction)
        self.menu.addSeparator()
        self.menu.addAction(removeAction)
        self.menu.addAction(deleteColumnAction)
        self.menu.popup(QtGui.QCursor.pos())

    def deleteRowByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            row = i.row()
            self.model.removeRow(row)
            print("Row " + str(row) + " deleted")
            self.tableView.selectRow(row)

    def addRowByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            row = i.row() + 1
            self.model.insertRow(row)
            print("Row at " + str(row) + " inserted")
            self.tableView.selectRow(row)

    def addRowByContext2(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            row = i.row()
            self.model.insertRow(row)
            print("Row at " + str(row) + " inserted")
            self.tableView.selectRow(row)

    def addColumnBeforeByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            col = i.column()
            self.model.insertColumn(col)
            print("Column at " + str(col) + " inserted")

    def addColumnAfterByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            col = i.column() + 1
            self.model.insertColumn(col)
            print("Column at " + str(col) + " inserted")

    def deleteColumnByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            col = i.column()
            self.model.removeColumn(col)
            print("Column at " + str(col) + " removed")

    def copyByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row, col)
            if myitem is not None:
                clip = QtWidgets.QApplication.clipboard()
                clip.setText(myitem.text())

    def pasteByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row, col)
            clip = QtWidgets.QApplication.clipboard()
            myitem.setText(clip.text())

    def cutByContext(self, event):
        for i in self.tableView.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row, col)
            if myitem is not None:
                clip = QtWidgets.QApplication.clipboard()
                clip.setText(myitem.text())
                myitem.setText("")

def stylesheet(self):
    return """
       QTableView
       {
            border: 2px solid grey;
            border-radius: 0px;
            font-size: 12px;
            background-color: #f8f8f8;
            selection-color: white;
            selection-background-color: #00ED56;
       }

        QTableView QTableCornerButton::section 
        {
            background: #D6D1D1;
            border: 1px outset black;
        }
        
        QPushButton
        {
            font-size: 11px;
            border: 1px inset grey;
            height: 24px;
            width: 80px;
            color: black;
            background-color: #e8e8e8;
            background-position: bottom-left;
        } 

        QComboBox
        {
            font-size: 14px;
            font-weight: bold;
            height: 25px;
            width: 60px;
            max-width: 40px;
            float: right;
            margin: 5px 0px;
            padding: 0px 0px;
            color: #333;
            background-color: #ffffff;
            background-image: none;
            border: 1px solid #cccccc;
            word-break: normal;
        } 
        
        QPushButton::hover
        {
            border: 2px inset goldenrod;
            font-weight: bold;
            color: #e8e8e8;
            background-color: green;
        } 
        
    """

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')
    main = MyWindow('')
    main.setMinimumSize(820, 300)
    main.setGeometry(0, 0, 1200, 680)
    main.setWindowTitle("Data File Processing")

    model = pandasModel(df)
    view = QTableView()
    view.setModel(model)
    view.resize(800, 600)
    view.show()

    main.show()

sys.exit(app.exec_())