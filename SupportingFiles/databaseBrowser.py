import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * # QPalette, QLinearGradient, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
    QInputDialog, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QMenu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 141, 401, 191))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.treeView.setFont(font)
        self.treeView.setObjectName("treeView")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(440, 140, 251, 192))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(720, 140, 251, 192))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.listView_2.setFont(font)
        self.listView_2.setObjectName("listView_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 350, 951, 192))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(370, 60, 201, 31))
        self.comboBox.setObjectName("comboBox")

        self.databasesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.databasesComboBox.setGeometry(QtCore.QRect(770, 60, 201, 31))
        self.databasesComboBox.setObjectName("databasesComboBox")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 60, 151, 31))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(lambda: self.connectDataSource())
        self.pushButton_2.clicked.connect(lambda: self.connectDataSource())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 40, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Populate"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "SQLite DB"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "MySQL DB"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Oracle DB"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Excel File(s)"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "JSON File(s)"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "XML File(s)"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "CSV File(s)"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Tab Delimited File(s)"))
        self.pushButton_2.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Data Source"))
        self.label_2.setText(_translate("MainWindow", "Database"))
        self.label_3.setText(_translate("MainWindow", "Tables"))
        self.comboBox.currentIndexChanged.connect(self.combo_index_changed)
        self.databasesComboBox.currentIndexChanged.connect(self.databasesComboBox_changed)

    def connectDataSource(self):
        try:
            filetypes = self.comboBox_2.currentText()
            if self.comboBox_2.currentText() == "SQLite DB":
                filetypes = "SQLite DB Files (*.db)"
                print(self.comboBox_2.currentText() + ' - ' + filetypes)
                #self.showMessage(self.comboBox_2.currentText() + ' - ' + filetypes)
            else:
                self.showMessage(self.comboBox_2.currentText() + ' - ' + filetypes)
            # filetypes = "Text files (*.txt);;CSV Files(*.csv);;Excel Files (*.xls);;Excel Files (*.xlsx);;JSON Files (*.json);;XML Files (*.xml);;All files( *.*)"
            #
            fileNames, _ = QFileDialog.getOpenFileNames(MainWindow, "Open " + filetypes + " Files",
                                                        'E:/GSReddy/PythonProjects',
                                                       # QDir.homePath()
                                                         filetypes)

            print("Selected Files from connectDataSource() 1 : " + str(fileNames) + " No of Files :" + str(len(fileNames)))
            #self.showMessage("Selected Files from connectDataSource() 1 : " + str(fileNames) + " No of Files :" + str(len(fileNames)))
            print(("Selected Files from connectDataSource() 1 : " + str(fileNames) + " No of Files :" + str(len(fileNames))))
            self.comboBox.addItems(fileNames)

            #dotIndex = fileNames[0].index("/") --> Get Slash position
            lastSlashPosition = fileNames[0].rfind("/")
            print('File Names : ' + fileNames[0])

            # print("/".join(fileNames[0].split("/")[0:-1]))  --> Get File Path Only
            selectedFile = self.comboBox.currentText()

            #self.showMessage("Selected file selectedFile : " + selectedFile
            #                 + " - Index : " + str(lastSlashPosition)
            #                 + " - Just File : " + fileNames[0][lastSlashPosition + 1:])

            print("Selected file selectedFile : " + selectedFile
                             + " - Index : " + str(lastSlashPosition)
                             + " - Just File : " + fileNames[0][lastSlashPosition + 1:])

            fileWithPath =[]
            fileWithOutPath =[]
            for i in range(len(fileNames)):
                print("fileNames[lastSlashPosition + 1:][" + str(i) + "] : " + fileNames[i][lastSlashPosition + 1:])
                #self.databasesComboBox.addItem(fileNames[i][lastSlashPosition + 1:])
                fileWithPath.append(fileNames[i])
                fileWithOutPath.append(fileNames[i][lastSlashPosition + 1:])
                #fileWithOutPath[i] =fileNames[i][lastSlashPosition + 1:]
            print(fileWithPath)
            print(fileWithOutPath)

                # for i in range(fileNames):
                #     dotIndex = fileNames.index(".") - 1
                #     justFileName = fileNames[dotIndex:].upper()

            self.df = pd.DataFrame(list(zip(fileWithPath, fileWithOutPath)),
                              columns=['PATH', 'FILENAME'])

            print(self.df)

            print("Before iteration")

            # for each row in dataframe, add item with value in 'PATH' column as text and value in 'FILENAME' column as data
            for row in self.df.itertuples():
                #print("Inside Iteration - Row : "+str(row))
                print("Row :" + row.PATH + ' - ' + row.FILENAME)
                self.databasesComboBox.addItem(row.FILENAME.upper(), row.PATH)
            print("after iteration")

        except Exception as error:
            print("From selectFiles() Method")
            self.showException('\n' + " Occured in selectFiles() : " + str(error))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    def combo_index_changed(self, index):
        # retrieve user data of an item in combo box via QComboBox.itemData()
        print(f'index {index}, text {self.comboBox.itemText(index)}, uid {self.comboBox.itemData(index)}')

    def databasesComboBox_changed(self, index):
        # retrieve user data of an item in combo box via QComboBox.itemData()
        print(f'index {index}, text {self.databasesComboBox.itemText(index)}, uid {self.databasesComboBox.itemData(index)}')

    def populateTables(self):
        pass
        # # In the main program, the data is read from the database.
        # # data = ['This is CSV File.csv',
        # #         'This is Excel File.xls',
        # #         'This is TXT File.txt',
        # #         'This is JSON File.json',
        # #         'This is XML File.xml']
        # #
        #
        # data = list(fileNames)
        #
        # if data:
        #     print('from selectFiles() - DATA Before : ' + str(type(data)))
        #     #filestable.setRowCount(len(data))
        #     print(*data, sep='-')
        #
        #     for i, ii in enumerate(data):
        #         consoleMesg = []
        #         print("Entered selectFiles() loop")
        #         consoleMesg.append(" i.Type : " + str(type(i)) + " - ii.Type : " + str(type(ii)) + " - i.Value : " + str(i) + " -  ii.Value : " + ii)
        #
        #         items = QTableWidgetItem()
        #         items = PyQt5.QtWidgets.QTableWidgetItem(ii)
        #         # Usage : ui.tableWidget.setItem(Row, Column, itm)
        #         filestable.setItem(i, 0, items)
        #
        #         btnFullReport = PyQt5.QtWidgets.QPushButton("...")
        #         btnFullReport.setMaximumSize(PyQt5.QtCore.QSize(80, 25))
        #         modifySpecs = PyQt5.QtWidgets.QPushButton(" +/- ")
        #         modifySpecs.setMaximumSize(PyQt5.QtCore.QSize(80, 25))
        #         viewData = PyQt5.QtWidgets.QPushButton(" Abc1@#* ")
        #         viewData.setMaximumSize(PyQt5.QtCore.QSize(80, 25))
        #         filestable.setCellWidget(i, 4, btnFullReport)
        #         filestable.setCellWidget(i, 5, modifySpecs)
        #         filestable.setCellWidget(i, 6, viewData)
        #         mymesg = "This is a custom message to show on custom message box from btnOpenFileNameDialog"
        #         #btnFullReport.clicked.connect(lambda: showCustomMessage(mymesg))  # Full Report Form
        #         btnFullReport.clicked.connect(lambda: handleButtonClicked())
        #         mymesg = "This is a custom message to show on custom message box from btnOpenFileNameDialog"
        #         #modifySpecs.clicked.connect(lambda: showCustomMessage(mymesg))  # Full Modify Specifications Form
        #         modifySpecs.clicked.connect(lambda: handleButtonClicked())
        #         mymesg = "This is a custom message to show on custom message box from btnOpenFileNameDialog"
        #         #viewData.clicked.connect(lambda: showCustomMessage(mymesg))  # Full View Data Form
        #         viewData.clicked.connect(lambda: handleButtonClicked())

        #    print(str(consoleMesg))
        # else
        #    showException("Select file Operation Cancelled")

        # except Exception as error:
        #     print(" Exception Occured in selectFile(s) Function : " +
        #           str(error) + '\n' +
        #           str(error.__doc__) + '\n' +
        #           str(error.__traceback__)  + '\n' +
        #           #traceback.print_exc() + '\n' +
        #           str(type(error).__name__) + '\n' +
        #           str(sys.exc_info()[0]) + "occurred." + '\n'
        #           #traceback.format_exc()
        #           )
        #     print('\n\n\n Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(error).__name__, error)

    def showMessage(self, mesg):
        print('From showMessage()')
        QMessageBox.information(MainWindow, "Information", mesg)

    def showException(self):
        print("From showException() Method")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        exceptionMesg = (str(exc_type) + '\n' + str(fname) + '\n' + str(exc_tb.tb_lineno))
        QMessageBox.information(MainWindow, "Information", exceptionMesg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
