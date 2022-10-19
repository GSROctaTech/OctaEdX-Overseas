from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QLineEdit, QMessageBox, QAbstractItemView, QApplication,
                             QTableWidget, QTableWidgetItem, QGridLayout, QFileDialog, QMenu, QInputDialog, QPushButton)
from PyQt5.QtGui import (QImage, QPainter, QIcon, QKeySequence, QTextCursor, QPalette,
                         QCursor, QDropEvent, QTextDocument, QTextTableFormat, QColor, QBrush)
from PyQt5.QtCore import (QFile, QSettings, Qt, QFileInfo, QItemSelectionModel, QDir,
                          QMetaObject, QAbstractTableModel, QModelIndex, QVariant)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        #self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)    *** Commented to Remove Tab ***
        #self.tabWidget.setObjectName("tabWidget")    *** Commented to Remove Tab ***
        #self.tab = QtWidgets.QWidget()    *** Commented to Remove Tab ***
        #self.tab.setObjectName("tab")   *** Commented to Remove Tab ***

        # --------------------------------------------------------------------------------------------------------------
        button1 = QtWidgets.QPushButton(self.centralwidget)
        button1.setText("Button1")
        button1.move(1, 32)
        #button1.clicked.connect(self.)
        # --------------------------------------------------------------------------------------------------------------

        # self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)    *** Commented to Remove Tab ***
        # self.gridLayout_2.setObjectName("gridLayout_2")   *** Commented to Remove Tab ***
        # self.tableWidget = QtWidgets.QTableWidget(self.tab)   *** Commented to Remove Tab ***

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.tableWidget.horizontalHeader().setStretchLastSection(False) # it was True before

        #self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1) *** Commented to Remove Tab ***
        #self.tabWidget.addTab(self.tab, "") *** Commented to Remove Tab ***
        #self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1) *** Commented to Remove Tab ***

        self.gridLayout.addWidget(self.tableWidget, 0, 60, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.tabWidget.setCurrentIndex(2) *** Commented to Remove Tab ***
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name & Locaton"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Delimiters"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "No. of Rows"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "File Analysis Summary"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Full Report"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Modify Specs.."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "View Data"))
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.horizontalHeader().setVisible(True)
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        # self.tableWidget.horizontalHeader().setHighlightSections(True)
        # self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        # self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        # self.tableWidget.horizontalHeader().setStretchLastSection(False)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget.setStyleSheet("QTableWidget{background-color:white;color:blue;font-size:11pt}QTableWidget::item{padding-left:0px;padding-right:0px}")
        header = self.tableWidget.horizontalHeader()
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Fixed)

        self.tableWidget.setColumnWidth(0, 765)
        self.tableWidget.setColumnWidth(3, 300)
        self.tableWidget.setColumnWidth(4, 80)
        self.tableWidget.setColumnWidth(5, 85)
        self.tableWidget.setColumnWidth(6, 85)

        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setLineWidth(3)

        # ** *Commented to Remove Tab ** *
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Tab"))

    #def buttonClicked(self, MainWindow):
     #       self.selectFiles()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("1 - Ui_Form --> setupUi --> New Form")
        Form.resize(800, 500)
        self.openGLWidget = QtWidgets.QOpenGLWidget(Form)
        self.openGLWidget.setGeometry(QtCore.QRect(9, 9, 382, 282))
        self.openGLWidget.setObjectName("openGLWidget")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("New Form", "2 - Ui_Form --> retranslateUi --> New Form"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    Form = QtWidgets.QWidget()
    f = Ui_Form()
    f.setupUi(Form)

    def selectFiles(self, Form):
        fileNames, _ = QFileDialog.getOpenFileNames(MainWindow, "Open CSV",
                                                    'E:/GSReddy/PythonProjects/SampleData',
                                                    # QDir.homePath() + "/Dokumente/CSV"
                                                    "CSV (*.csv *.tsv *.txt)")

        print(fileNames)

        # In the main program, the data is read from the database.
        data = ['This is CSV File.csv',
                'This is Excel File.xls',
                'This is TXT File.txt',
                'This is JSON File.json',
                'This is XML File.xml']

        data = list(fileNames)

        print('DATA Before : ' + str(type(data)))
        # print('CDATA Before : ' + str(type(cdata)))
        print('fileNames Before : ' + str(type(fileNames)))

        ui.tableWidget.setRowCount(len(data))
        print(*data, sep='-')
        for i, ii in enumerate(data):
            print('i.Type : ' + str(type(i)) + ' - ii.Type : ' + str(type(ii)) + ' - i.Value : ' + str(i) + ' -  ii.Value : ' + ii)
            itm = QtWidgets.QTableWidgetItem(ii)
            # Usage : ui.tableWidget.setItem(Row, Column, itm)
            ui.tableWidget.setItem(i, 0, itm)
            ui.btnFullReport = QtWidgets.QPushButton("...")
            ui.btnFullReport.setMaximumSize(QtCore.QSize(80, 25))

            ui.modifySpecs = QtWidgets.QPushButton(" +/- ")
            ui.modifySpecs.setMaximumSize(QtCore.QSize(80, 25))

            ui.viewData = QtWidgets.QPushButton(" Abc1@#* ")
            ui.viewData.setMaximumSize(QtCore.QSize(80, 25))

            ui.tableWidget.setCellWidget(i, 4, ui.btnFullReport)
            ui.tableWidget.setCellWidget(i, 5, ui.modifySpecs)
            ui.tableWidget.setCellWidget(i, 6, ui.viewData)

            ui.btnFullReport.clicked.connect(Form.show)  # Full Report Form
            ui.modifySpecs.clicked.connect(Form.show)  # Full Modify Specifications Form
            ui.viewData.clicked.connect(Form.show)  # Full View Data Form

    MainWindow.show()
    sys.exit(app.exec_())