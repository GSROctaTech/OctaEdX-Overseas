import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QLineEdit, QMessageBox, QAbstractItemView, QApplication,
                             QTableWidget, QTableWidgetItem, QGridLayout, QFileDialog, QMenu, QInputDialog, QPushButton)
from PyQt5.QtGui import (QImage, QPainter, QIcon, QKeySequence, QTextCursor, QPalette,
                         QCursor, QDropEvent, QTextDocument, QTextTableFormat, QColor, QBrush)
from PyQt5.QtCore import (QFile, QSettings, Qt, QFileInfo, QItemSelectionModel, QDir,
                          QMetaObject, QAbstractTableModel, QModelIndex, QVariant)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Files Processing..'
        self.left = 50
        self.top = 50
        self.width = 1140
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        btnSelectFiles = QPushButton(self)
        btnSelectFiles.setText("Select File(s)..")
        btnSelectFiles.setGeometry(50, 50, 100, 30) # x, y, w, h
        btnSelectFiles.clicked.connect(self.openFileNamesDialog)

        btnOpenFileNameDialog = QPushButton(self)
        btnOpenFileNameDialog.setText("File Name Dialog")
        btnOpenFileNameDialog.setGeometry(160, 50, 100, 30)
        btnOpenFileNameDialog.clicked.connect(self.openFileNameDialog)

        btnSaveFileDialog = QPushButton(self)
        btnSaveFileDialog.setText("Save File Dialog")
        btnSaveFileDialog.setGeometry(270, 50, 100, 30)
        btnSaveFileDialog.clicked.connect(self.saveFileDialog)

        btnGenMetadata = QPushButton(self)
        btnGenMetadata.setText("Generate Metadata")
        btnGenMetadata.setGeometry(380, 50, 100, 30)
        #btnGenMetadata.clicked.connect(self.generateMetadata)
        btnGenMetadata.clicked.connect(self.showMessage)

        btnMesgDialog = QPushButton(self)
        btnMesgDialog.setText("Mesg Dialog")
        btnMesgDialog.setGeometry(490, 50, 100, 30)
        btnMesgDialog.clicked.connect(self.mesgDialog)

        btnCustomMesgDialog = QPushButton(self)
        btnCustomMesgDialog.setText("Custom Mesg Dialog")
        btnCustomMesgDialog.setGeometry(610, 50, 100, 30)
        mymesg = "This is a custom message to show on custom message box from btnCustomMesgDialog"
        btnCustomMesgDialog.clicked.connect(lambda: self.showCustomMessage(mymesg))

        '''
            # Logic to implement to Call functions from click of button 
            btn_brow_4.clicked.connect(wrapper) # Use some wrapper function in button clicked.connect
            def wrapper():      # This is a wrapper function to call actual function
                function(12)
            def function(a):    # This is Actual function called from wrapper function
                print("Hola mundo" + str(a))
        '''

        '''
        Add other components here
        '''
        # --------------------------------------------------------------------------------------------------------------

        # self.setWindowTitle(self,"MainWindow")

        tableWidget = QtWidgets.QTableWidget(self)
        tableWidget.setObjectName("tableWidget")

        tableWidget.setGeometry(30, 100, 1000, 400)

        tableWidget.setColumnCount(7)
        tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(6, item)

        tableWidget.horizontalHeader().setStretchLastSection(False) # it was True before

        item = tableWidget.horizontalHeaderItem(0)
        item.setText("File Name & Location")
        item = tableWidget.horizontalHeaderItem(1)
        item.setText("Delimiters")
        item = tableWidget.horizontalHeaderItem(2)
        item.setText("No. of Rows")
        item = tableWidget.horizontalHeaderItem(3)
        item.setText("File Analysis Summary")
        item = tableWidget.horizontalHeaderItem(4)
        item.setText("Full Report")
        item = tableWidget.horizontalHeaderItem(5)
        item.setText("Modify Specs..")
        item = tableWidget.horizontalHeaderItem(6)
        item.setText("View Data")

        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.horizontalHeader().setVisible(True)
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        # self.tableWidget.horizontalHeader().setHighlightSections(True)
        # self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        # self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        # self.tableWidget.horizontalHeader().setStretchLastSection(False)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        tableWidget.setStyleSheet("QTableWidget{background-color:white;color:blue;font-size:11pt}"
                                       "QTableWidget::item{padding-left:0px;padding-right:0px}")
        header = tableWidget.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Fixed)

        tableWidget.setColumnWidth(0, 365)
        tableWidget.setColumnWidth(3, 300)
        tableWidget.setColumnWidth(4, 80)
        tableWidget.setColumnWidth(5, 85)
        tableWidget.setColumnWidth(6, 85)

        tableWidget.verticalHeader().setDefaultSectionSize(25)
        tableWidget.verticalHeader().setLineWidth(3)

        # --------------------------------------------------------------------------------------------------------------

        # Invoking Functions
        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()

        self.show()
        sys.exit(app.exec_())

        '''
        def __init__(self, parent=None):
            super(WidgetGallery, self).__init__(parent)
            self.table = QtWidgets.QTableWidget(10, 3)
            col_1 = QtWidgets.QTableWidgetItem("first_col")
            col_2 = QtWidgets.QTableWidgetItem("second_col")
            deleteButton = QtWidgets.QPushButton("delete_this_row")
            deleteButton.clicked.connect(self.deleteClicked)
            self.table.setItem(0, 0, col_1)
            self.table.setItem(0, 1, col_2)
            self.table.setCellWidget(0, 2, deleteButton)
            self.mainLayout = QtWidgets.QGridLayout(self)
            self.mainLayout.addWidget(self.table)
    
        @QtCore.pyqtSlot()
        def deleteClicked(self):
            button = self.sender()
            if button:
                row = self.table.indexAt(button.pos()).row()
                self.table.removeRow(row)
        '''

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        fileTypes = "Text Files (*.txt);;CSV Files (*.csv);;Excel Files (*.xls);;Excel Files (*.xlsx);;JSON Files (*.json);;XML Files (.xml);; All Files (*.*)"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                fileTypes, options=options)

        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def generateMetadata(self):

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Create Database")
        dlg.setText("Do you want to create a demo database")

        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore)
        ''' 
            Other Options :
            QMessageBox.Ok      QMessageBox.Open    QMessageBox.Save        QMessageBox.Cancel          QMessageBox.Close 
            QMessageBox.Discard QMessageBox.Apply   QMessageBox.Reset       QMessageBox.RestoreDefaults QMessageBox.Help
            QMessageBox.SaveAll QMessageBox.Yes     QMessageBox.YesToAll    QMessageBox.No              QMessageBox.NoToAll
            QMessageBox.Abort   QMessageBox.Retry   QMessageBox.Ignore      QMessageBox.NoButton
        '''

        dlg.setIcon(QMessageBox.Question)
        ''' 
            Other Options :
            QMessageBox.NoIcon	    The message box does not have an icon.
            QMessageBox.Question	The message is asking a question.
            QMessageBox.Information	The message is informational only.
            QMessageBox.Warning	    The message is warning.
            QMessageBox.Critical	The message indicates a critical problem.
        '''

        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")

        logMessage("Log Message - From generateMetadata")

    def createDemoDb(self):  # ---------------------------- Create SQLLite Demo Database -------------------------------
        # https://pythonspot.com/python-database/
        # https://pythonspot.com/python-database-programming-sqlite-tutorial/
        # https://pythonspot.com/sqlite-database-with-pandas/
        import sqlite3 as lite
        import sys

        con = lite.connect('population.db')

        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Population(id INTEGER PRIMARY KEY, country TEXT, population INT)")
            cur.execute("INSERT INTO Population VALUES(NULL,'Germany',81197537)")
            cur.execute("INSERT INTO Population VALUES(NULL,'France', 66415161)")
            cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")
            cur.execute("INSERT INTO Population VALUES(NULL,'Italy', 60795612)")
            cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")

    def readSQLLiteDB(self): # ---------------------------- SQLLite Database -------------------------------------------
        # https://pythonspot.com/python-database/
        # https://pythonspot.com/python-database-programming-sqlite-tutorial/
        import pandas as pd
        import sqlite3

        conn = sqlite3.connect('population.db')
        query = "SELECT country FROM Population WHERE population > 50000000;"

        df = pd.read_sql_query(query, conn)

        for country in df['country']:
            print(country)

    def readMySQLDB(self): # ---------------------------- MySQL Database -----------------------------------------------
        # https://pythonspot.com/python-database/
        # https://pythonspot.com/mysql-with-python/
        import MySQLdb

        db = MySQLdb.connect(host="localhost",  # your host
                             user="root",  # username
                             passwd="root",  # password
                             db="pythonspot")  # name of the database

        # Create a Cursor object to execute queries.
        cur = db.cursor()

        # Select data from table using SQL query.
        cur.execute("SELECT * FROM examples")

        # print the first and second columns
        for row in cur.fetchall():
            print(row[0], " ", row[1])

    def readExcel(self): # -------------------------------- Excel Files  -----------------------------------------------
        # https://pythonspot.com/read-xls-with-pandas/
        from pandas import DataFrame, read_csv
        import matplotlib.pyplot as plt
        import pandas as pd

        file = r'data/Presidents.xls'
        df = pd.read_excel(file)
        # df = pd.read_excel(file, sheetname='Elected presidents')

        # remove messy data
        df = df[df['Years in office'] != 'n/a']

        # show data
        print('Min: ', df['Years in office'].min())
        print('Max: ', df['Years in office'].max())
        print('Sum: ', df['Years in office'].sum())

    def readCSV(self): # ---------------------------------- CSV Files  -------------------------------------------------
        # https://pythonspot.com/pandas-read-csv/
        from pandas import DataFrame, read_csv
        import matplotlib.pyplot as plt
        import pandas as pd

        file = r'highscore.csv'
        df = pd.read_csv(file)
        print('Max', df['Highscore'].max())
        print('Min', df['Highscore'].min())

    def mesgDialog(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")

        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore)
        ''' 
            Other Options :
            QMessageBox.Ok      QMessageBox.Open    QMessageBox.Save        QMessageBox.Cancel          QMessageBox.Close 
            QMessageBox.Discard QMessageBox.Apply   QMessageBox.Reset       QMessageBox.RestoreDefaults QMessageBox.Help
            QMessageBox.SaveAll QMessageBox.Yes     QMessageBox.YesToAll    QMessageBox.No              QMessageBox.NoToAll
            QMessageBox.Abort   QMessageBox.Retry   QMessageBox.Ignore      QMessageBox.NoButton
        '''

        dlg.setIcon(QMessageBox.Question)
        ''' 
            Other Options :
            QMessageBox.NoIcon	    The message box does not have an icon.
            QMessageBox.Question	The message is asking a question.
            QMessageBox.Information	The message is informational only.
            QMessageBox.Warning	    The message is warning.
            QMessageBox.Critical	The message indicates a critical problem.
        '''

        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")
    def showReport(self): # ---------------------------------- Analytics -----------------------------------------------
        # https://pythonspot.com/visualize-data-with-pandas/
        from pandas import DataFrame, read_csv
        import matplotlib.pyplot as plt
        import pandas as pd

        file = r'data/Presidents.xls'
        df = pd.read_excel(file)

        # plot data
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'green', 'blue', 'orange', 'white',
                  'brown']
        df['Occupation'].value_counts().plot(kind='pie', title='Occupation by President', colors=colors)
        plt.show()

    def logMessage(logMsg): # ---------------------------------- Logging Module ----------------------------------------
        print(logMsg)

    def showMessage(self): # ---------------------------------- Show Info Module ----------------------------------------
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')

    def showCustomMessage(self, mesg):
        print('Start showCustomMessage - mesg : ' + mesg)
        try:
            buttonReply = QMessageBox.question(self, 'PyQt5 message', mesg, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            print(int(buttonReply))
            if buttonReply == QMessageBox.Yes:
                print('Yes clicked.')
            if buttonReply == QMessageBox.No:
                print('No clicked.')
            if buttonReply == QMessageBox.Cancel:
                print('Cancel')
        except Error as e:
            print(e + " Exeception Occured in showCustomMessage Block")
            buttonReply = QMessageBox.question(self, 'Exception', mesg, QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                print('Yes clicked.')
                print(e + " Exeception Occured in showCustomMessage Block")

    def TestDBConnection(self):

        try:
            # Making a connection between sqlite3 database and Python Program
            sqliteConnection = sqlite3.connect('SQLite_Retrieving_data.db')
            # If sqlite3 makes a connection with python program then it will print "Connected to SQLite"
            # Otherwise it will show errors
            print("Connected to SQLite")
        except sqlite3.Error as error:
            print("Failed to connect with sqlite3 database", error)
        finally:
            # Inside Finally Block, If connection is open, we need to close it
            if sqliteConnection:
                # using close() method, we will close the connection
                sqliteConnection.close()
                # After closing connection object, we will print "the sqlite connection is closed"
                print("the sqlite connection is closed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())