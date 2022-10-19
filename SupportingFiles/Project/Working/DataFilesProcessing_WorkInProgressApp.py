import os
import sqlite3
import sys
import PyQt5
import lxml
from PyQt5 import QtGui
from PyQt5.QtGui import * # QPalette, QLinearGradient, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
    QInputDialog, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QMenu

app = QApplication([])
window = QMainWindow()
widget = QWidget(window)
layout = QGridLayout()
widget.setLayout(layout)

app.setStyle('Fusion') # Options : ['windowsvista', 'Windows', 'Fusion']
print('Application Theme : ' + app.style().objectName())
window.setGeometry(30,30,1280,680)

# Setting MainWindow Background Color
p = QPalette()
gradient = QLinearGradient(0, 0, 0, 400)
gradient.setColorAt(0.0, QColor(240, 240, 240))
gradient.setColorAt(1.0, QColor(240, 160, 160))
p.setBrush(QPalette.Window, QBrush(gradient))
window.setPalette(p)

# label = QLabel()
# label.setText('Hello world!')
# layout.addWidget(label, 0, 0)

selFilesButton = QPushButton()
selFilesButton.setText('Select File(s)..')
# layout.addWidget(selFilesButton, 1, 0, 1, 2)
layout.addWidget(selFilesButton, 0, 0)   # Table Adding to 1 Row on Form/Window
selFilesButton.clicked.connect(lambda: selectFiles())

calcButton = QPushButton()
calcButton.setText('Calculator')
# layout.addWidget(calcButton, 2, 1, 1, 2)
layout.addWidget(calcButton,0,1)   # Table Adding to 1 Row on Form/Window
calcButton.clicked.connect(lambda: open_calculator())

getSelFilesButton = QPushButton()
getSelFilesButton.setText('Show Selected Files')
# layout.addWidget(getSelFilesButton, 2, 1, 1, 2)
layout.addWidget(getSelFilesButton,0,2)   # Table Adding to 1 Row on Form/Window
getSelFilesButton.clicked.connect(lambda: getSelectedFiles())

findSelectedItemButton = QPushButton()
findSelectedItemButton.setText('Find Selected Files')
# layout.addWidget(findSelectedItemButton, 2, 1, 1, 2)
layout.addWidget(findSelectedItemButton,0,3)   # Table Adding to 1 Row on Form/Window
findSelectedItemButton.clicked.connect(lambda: findSelectedItemIds())

viewTestData = QPushButton()
viewTestData.setText('Show Test Data')
# layout.addWidget(viewTestData, 2, 1, 1, 2)
layout.addWidget(viewTestData,3,1)   # Table Adding to 1 Row on Form/Window
viewTestData.clicked.connect(lambda: poplulateTestData())

viewDataOfSelFile = QPushButton()
viewDataOfSelFile.setText('Show Single File Data')
# layout.addWidget(findSelectedItemButton, 2, 1, 1, 2)
layout.addWidget(viewDataOfSelFile,3,2)   # Table Adding to 1 Row on Form/Window
viewDataOfSelFile.clicked.connect(lambda: showFileSingleSelection())

yearly_income = QLabel()
yearly_income.setText('Yearly Income: $0.00')
layout.addWidget(yearly_income, 1, 0)   # Table Adding to 2 Row on Form/Window

tax_rate = QLabel()
tax_rate.setText('Highest Marginal Tax Rate: 0%')
layout.addWidget(tax_rate, 1, 1)   # Table Adding to 2 Row on Form/Window

# setting background color to label when mouse hover over it
tax_rate.setStyleSheet("QLabel::hover"
                    "{"
                    "background-color : lightblue;"
                    "font-color : white;"
                    "}")
## ---------------------------------------------------------------------------------------------------------------------
filestable = QTableWidget()
#filestable.setColumnCount(len(columns))
#filestable.setHorizontalHeaderLabels(columns)
#filestable.setRowCount(len(table_data))

# layout.addWidget(filestable, 2, 0, 1, 2)
layout.addWidget(filestable, 2, 0)   # Table Adding to 3 Row on Form/Window

filestableColumns = ('File Name & Location', 'Delimiters', 'No. of Rows', 'File Analysis Summary',
                     'Full Report', 'Modify Specs..', 'View Data')
filestable.setColumnCount(len(filestableColumns))
filestable.setHorizontalHeaderLabels(filestableColumns)
filestable.setColumnCount(7)    # self.tableWidget.setColumnCount(7)
filestable.setRowCount(0)       # self.tableWidget.setRowCount(0)
filestable.setPalette(p)

# --------------------------------------------------------------------------------------------------------------
# Style Sheets for Look and Feel

# with open('styles.css', 'r') as f:
#     style = f.read()
#     # Set the stylesheet of the application
#     app.setStyleSheet(style)

# filestable.setAlternatingRowColors(True)

# p = QPalette()
# gradient = QLinearGradient(0, 0, 0, 400)
# gradient.setColorAt(0.0, QColor(240, 240, 240))
# gradient.setColorAt(1.0, QColor(240, 160, 160))
# p.setBrush(QPalette.Window, QBrush(gradient))
# window.setPalette(p)
#
#  QPalette selectedFilesPalette = filestable.palette();
#  p.setColor(QPalette::Base, color1);
#  p.setColor(QPalette::AlternateBase, color2);
#  filestable.setPalette(selectedFilesPalette);

# filestable.setStyleSheet("::item:hover{background-color:rgba(222,100,123,100);}"
#                          "::item:selected{background-color:rgba(100,200,100);}")

# tableHeaderCSS = "::section{Background-color:rgb(190,1,1);border-radius:10px;font-size:14pt}"
tableHeaderCSS = "::section{Background-color:#097579;border-radius:5px;font-size:10pt;font-color:white;}"

# filestable.setStyleSheet("QTableView::item:alternate { background-color: #bfffbf; } "
#                          "QTableView::item { background-color: #deffde; }")

filestable.horizontalHeader().setStyleSheet(tableHeaderCSS)

# filestable.setStyleSheet("QTableWidget{background-color:white;color:blue;font-size:11pt} "
#                          "QTableWidget::item{padding-left:0px;padding-right:0px}")

calcButton.setStyleSheet(
    #"background-color: #262626; "
    "font-family: times; "
    "font-size: 15px;"
    "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);"
    "border: 1px solid #bfcde4;"
)

# selFilesButton.setStyleSheet(
#     "background-color: #262626;"
#     "font-family: times; height:30px"
#     "font-size: 15px;"
#     "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);"
#     "border: 5px solid #bfcde4;"
#)

selFilesButton.setStyleSheet("QPushButton {background-color: blue; height: 40px; border-radius: 5px;}"
                             "QPushButton:pressed {background-color: red; border-radius: 15px;}"
                             "QPushButton:hover {background: yellow;border: 1px solid black;}"
                             )

# copy style parameters from below code to above one by one and test the app
#selFilesButton.setStyleSheet(
    #"QPushButton {width: 130px; height: 40px; color: #fff; border-radius: 5px; padding: 10px 25px;"
    #"font-family: 'Lato', sans-serif; font-weight: 500; background: transparent;"
    #"cursor: pointer; transition: all 0.3s ease; position: relative; display: inline-block;"
    #"box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5), 7px 7px 20px 0px rgba(0,0,0,.1),4px 4px 5px 0px rgba(0,0,0,.1); outline: none;}"
 #   "QPushButton:default {width: 130px; height: 60px; border-radius: 5px; padding: 10px 25px;}"
  #  "QPushButton:pressed {background: rgb(6,14,131);background: linear-gradient(0deg, rgba(6,14,131,1) 0%, rgba(12,25,180,1) 100%);border: none;}"
  #  "QPushButton:hover {background: rgb(0,3,255);background: linear-gradient(0deg, rgba(0,3,255,1) 0%, rgba(2,126,251,1) 100%);}")



filestable.setStyleSheet("::item:hover{background-color:rgba(222,100,123,100);}"
                          "::item:selected{background-color:rgba(100,200,100);}")


# --------------------------------------------------------------------------------------------------------------



# item = QTableWidgetItem()                               # self.item = PyQt5.QtWidgets.QTableWidgetItem()
# filestable.setHorizontalHeaderItem(0, item)             # self.tableWidget.setHorizontalHeaderItem(1, self.item)
# filestable.setHorizontalHeaderItem(1, item)
# filestable.setHorizontalHeaderItem(2, item)
# filestable.setHorizontalHeaderItem(3, item)
# filestable.setHorizontalHeaderItem(4, item)
# filestable.setHorizontalHeaderItem(5, item)
# filestable.setHorizontalHeaderItem(6, item)
# filestable.horizontalHeader().setStretchLastSection(True)
#
# item = filestable.horizontalHeaderItem(0)
# item.setText("File Name & Location")
# item = filestable.horizontalHeaderItem(1)
# item.setText("Delimiters")
# item = filestable.horizontalHeaderItem(2)
# item.setText("No. of Rows")
# item = filestable.horizontalHeaderItem(3)
# item.setText("File Analysis Summary")
# item = filestable.horizontalHeaderItem(4)
# item.setText("Full Report")
# item = filestable.horizontalHeaderItem(5)
# item.setText("Modify Specs..")
# item = filestable.horizontalHeaderItem(6)
# item.setText("View Data")
#
# # filestable.resizeColumnsToContents()
# # filestable.horizontalHeader().setVisible(True)
# # filestable.horizontalHeader().setCascadingSectionResizes(True)
# # filestable.horizontalHeader().setDefaultSectionSize(140)
# # filestable.horizontalHeader().setHighlightSections(True)
# # filestable.horizontalHeader().setMinimumSectionSize(100)
# # filestable.horizontalHeader().setSortIndicatorShown(False)
# # filestable.horizontalHeader().setStretchLastSection(False)
# # filestable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

header = filestable.horizontalHeader()
header.setSectionResizeMode(0, PyQt5.QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(1, PyQt5.QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(2, PyQt5.QtWidgets.QHeaderView.Fixed)
header.setSectionResizeMode(3, PyQt5.QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(4, PyQt5.QtWidgets.QHeaderView.Fixed)
header.setSectionResizeMode(5, PyQt5.QtWidgets.QHeaderView.Fixed)
header.setSectionResizeMode(6, PyQt5.QtWidgets.QHeaderView.Fixed)

filestable.setColumnWidth(0, 365)
filestable.setColumnWidth(3, 300)
filestable.setColumnWidth(4, 80)
filestable.setColumnWidth(5, 85)
filestable.setColumnWidth(6, 85)

filestable.verticalHeader().setDefaultSectionSize(25)
filestable.verticalHeader().setLineWidth(3)

## -----------------------------------------------------------------------------------------------------------------------

def selectFiles():
    try:
        filetypes = "Text files (*.txt);;CSV Files(*.csv);;Excel Files (*.xls);;Excel Files (*.xlsx);;JSON Files (*.json);;XML Files (*.xml);;All files( *.*)"

        fileNames, _ = QFileDialog.getOpenFileNames(widget, "Open CSV",
                                                    'E:/GSReddy/PythonProjects/SampleData',
                                                    # QDir.homePath()
                                                    # "CSV Files (*.csv);; Tab Delimted (*.tsv);; Text Files (*.txt);;"
                                                    filetypes)

        #print("Selected Files from selectFiles() 1 : " + str(fileNames))

        # In the main program, the data is read from the database.
        # data = ['This is CSV File.csv',
        #         'This is Excel File.xls',
        #         'This is TXT File.txt',
        #         'This is JSON File.json',
        #         'This is XML File.xml']
        #

        data = list(fileNames)

        if data:
            print('from selectFiles() - DATA Before : ' + str(type(data)))
            # print('fileNames Before : ' + str(type(fileNames)))
            filestable.setRowCount(len(data))
            print(*data, sep='-')

            for i, ii in enumerate(data):
                consoleMesg = []
                print("Entered selectFiles() loop")
                consoleMesg.append(" i.Type : " + str(type(i)) + " - ii.Type : " + str(type(ii)) + " - i.Value : " + str(i) + " -  ii.Value : " + ii)

                items = QTableWidgetItem()
                items = PyQt5.QtWidgets.QTableWidgetItem(ii)
                # Usage : ui.tableWidget.setItem(Row, Column, itm)
                filestable.setItem(i, 0, items)

                btnFullReport = PyQt5.QtWidgets.QPushButton("...")
                btnFullReport.setMaximumSize(PyQt5.QtCore.QSize(80, 25))
                modifySpecs = PyQt5.QtWidgets.QPushButton(" +/- ")
                modifySpecs.setMaximumSize(PyQt5.QtCore.QSize(80, 25))
                viewData = PyQt5.QtWidgets.QPushButton(" Abc1@#* ")
                viewData.setMaximumSize(PyQt5.QtCore.QSize(80, 25))
                filestable.setCellWidget(i, 4, btnFullReport)
                filestable.setCellWidget(i, 5, modifySpecs)
                filestable.setCellWidget(i, 6, viewData)
                mymesg = "This is a custom message to show on custom message box from btnOpenFileNameDialog"
                #btnFullReport.clicked.connect(lambda: showCustomMessage(mymesg))  # Full Report Form
                btnFullReport.clicked.connect(lambda: handleButtonClicked())
                mymesg = "This is a custom message to show on custom message box from btnOpenFileNameDialog"
                #modifySpecs.clicked.connect(lambda: showCustomMessage(mymesg))  # Full Modify Specifications Form
                modifySpecs.clicked.connect(lambda: handleButtonClicked())
                mymesg = "This is a custom message to show on custom message box from btnOpenFileNameDialog"
                #viewData.clicked.connect(lambda: showCustomMessage(mymesg))  # Full View Data Form
                viewData.clicked.connect(lambda: handleButtonClicked())

            print(str(consoleMesg))
        else:
            showException("Select file Operation Cancelled")
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

    except Exception as error:
        print("From selectFiles() Method")
        showException('\n' + " Occured in selectFiles() : " + str(error))
        #exc_type, exc_obj, exc_tb = sys.exc_info()
        #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #print(exc_type, fname, exc_tb.tb_lineno)

# ----------------------------------------------------------------------------------------------------------------------
def showCustomMessage(mesg):
    print('Start showCustomMessage - mesg : ' + mesg)
    try:
        buttonReply = QMessageBox.question(widget, 'PyQt5 message', mesg,
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                           QMessageBox.Cancel)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        if buttonReply == QMessageBox.Cancel:
            print('Cancel')
    except Exception as e:
        mesg ="Exeception Occured in showCustomMessage Block"
        showException(mesg)

def showMessage(mesg):
    print('From showMessage()')
    QMessageBox.information(widget, "Information", mesg)

def showException():
    print("From showException() Method")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    exceptionMesg = (str(exc_type) + '\n' + str(fname) + '\n' + str(exc_tb.tb_lineno))
    QMessageBox.information(widget, "Information", exceptionMesg)

def showException(mesg):
    print("From showException(mesg) Method")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    if mesg:
        exceptionMesg = (str(exc_type) + '\n' + str(fname) + '\n' + str(exc_tb.tb_lineno) + '\n' + mesg)
    else:
        exceptionMesg = (str(exc_type) + '\n' + str(fname) + '\n' + str(exc_tb.tb_lineno))

    # QMessageBox.information(widget, "Information", exceptionMesg)
    QMessageBox.critical(widget, "Error", exceptionMesg,QMessageBox.Ok,QMessageBox.Ok)

def contextMenuEvent(event):
    """Open context menu for selected items."""
    selected_items = filestable.selectedItems()

    if selected_items:

        menu = QMenu()
        menu.setStyleSheet("""
            QMenu {border: 1px inset grey; background-color: #fff; color: #000; padding: 0;}
            QMenu:selected {background-color: #ddf; color: #000;}"""
        )
        # File submenu
        file_menu = QMenu("File")
        delete_action = file_menu.addAction("Delete")
        menu.addMenu(file_menu)

        # Format sub_menu
        format_menu = QMenu("Format")
        format_split_action = format_menu.addAction("Split address")
        format_title_case_action = format_menu.addAction("Title Case")
        menu.addMenu(format_menu)

        menu.addSeparator()

        # Quick links
        menu.addAction("Split address")
        menu.addAction("Title Case")

        action = menu.exec_(mapToGlobal(event.pos()))
        if action:
            if action == format_title_case_action:
                format_title_case()
            elif action == format_split_action:
                split_address()
            elif action == delete_action:
                remove_selected_rows()

def mapToGlobal(event):
    showMessage("From mapToGlobal")
def format_title_case():
    showMessage("From format_title_case")
def split_address():
    showMessage("From split_address")
def remove_selected_rows():
    showMessage("From remove_selected_rows")

def getSelectedFiles1():
    print('Entered getSelectedFiles()')
    mesgSel = ''
    results= []
    selected_items = filestable.selectedItems()

    # selectedRanges(), would give you the second cell from each selected row, for example:
    indexes = []
    for selectionRange in filestable.selectedRanges():
        indexes.extend(range(selectionRange.topRow(), selectionRange.bottomRow()+1))
        print("Selected Indexes", indexes)      # indexes is a list like [0, 2] of selected rows

    for i in indexes:
        print("specific item", filestable.item(i, 1).text())
        #mesgSel = "specific item", filestable.item(i, 1).text() + '\n'
        #results.append( str(filestable.item(i, 1).text()) )

        # liste = []
        # for i in range(34):
        #     liste.append(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), i).text())

    # selectedItems()
    for item in filestable.selectedItems():
        print("selectedItems", item.text())
        mesgSel = mesgSel + "selectedItems", item.text() + '\n'

    # selectedIndexes()
    for item in filestable.selectedIndexes():
        print("selectedIndexes", item.row(), item.column())
        mesgSel = mesgSel + "selectedIndexes", item.row(), item.column() + '\n'

    # indexes = filestable.selectionModel().selectedRows()
    # mesgSel=''
    # for index in sorted(indexes):
    #     mesgSel += str(index.row()) + '\n'
    #     print('Row %d is selected' % index.row())

    showMessage(mesgSel + '\n' + results)

def getSelectedFiles():
    selectedList=[]
    print('Entered getSelectedFiles()')
    try:
        selected = filestable.selectedItems()
        if selected:
            for item in selected:
                if item.column() == 0:
                    print(item.data(0))
                    selectedList.append(item.data(0))
        mesg = 'Selected Files : ' + '\n'+ str(selectedList)
        print(mesg)
        QMessageBox.information(widget, "Selected File from the list ", mesg)

    # For Single & Current Selection Use the below
    # row = self.tableWidget.currentRow()
    # path = (self.tableWidget.item(row, 3).text())

    except Exception as error:
        print("From getSelectedFiles() Method")
        showException(" Occured in getSelectedFiles()")

def showFileSingleSelection():
    print('Entered showFileSingleSelection()')
    try:
        # For Single & Current Selection Use the below
        row = filestable.currentRow()
        path = (filestable.item(row, 0).text())
        mesg = path
        # selectedFileToView =''
        # selItems = filestable.selectedItems()
        # selectedFileToView = filestable.item(selItemsRows[i], 0).text()

        dotIndex = path.index(".") + 1
        fileExtension = filestable.item(row, 0).text()[dotIndex:].upper()

        showMessage(fileExtension)

        confimReply = QMessageBox.question(widget, fileExtension + " File View",
                                   "Do you want to view " + mesg + " file data ",
                                   QMessageBox.Ok | QMessageBox.No, defaultButton=QMessageBox.Ok)
        if confimReply == QMessageBox.Ok:
            # Call respective method based on the file extension
            if fileExtension == 'CSV':
                readCSV(mesg)
            elif fileExtension in ('XLSX','XLS'):
                readExcel(mesg)
            elif fileExtension == 'XML':
                readXML(mesg)
            else:
                showMessage("Selected fileExtension : " + fileExtension)
        else:
            QMessageBox.information(widget, "CSV File View",
                                 "You selected not to view " + mesg + " file data ",
                                 QMessageBox.Ok, defaultButton=QMessageBox.Ok)
    except Exception as error:
        print("From showFileSingleSelection(mesg) Method")
        showException(" Occured in showFileSingleSelection")

def findSelectedItemIds():
    try:
        selItems = filestable.selectedItems()
        selItemsRows = []
        for i in range(len(selItems)):
            selItemsRows.append(selItems[i].row())
        #selItemsRows = unique(selItemsRows)
        selItemsIds = []
        for i in range(len(selItemsRows)):
            selItemsIds.append(str(filestable.item(selItemsRows[i], 0).text()))
        # return selItemsIds
        mesg = 'Selected Files : ' + '\n' + str(selItemsIds)
        print(mesg)
        QMessageBox.information(widget, "Selected File from the list ", mesg)
    except Exception as error:
        print(str(error) + " Occured in findSelectedItemIds Method")
        showException(" Occured in findSelectedItemIds")

def handleButtonClicked():
    print("Entered handleButtonClicked() - 1")
    try:
        buttonClicked = filestable.sender() # detects the widget that sends the signal
        postitionOfWidget = buttonClicked.pos() # gets the x,y coordinate of this sender
        index = filestable.indexAt(postitionOfWidget) # item in the QTableWidget with that coordinate
        if index.isValid():
            print(index.row(), index.column())
            showMessage("Index : " + str(index.row()) + '\n' +
                        "Column : " + str(index.column()) +  '\n' +
                        "Value : " + filestable.item(index.row(), 0).text())
    except Exception as error:
        showMessage(" Exception Occured in selectFile(s) Function : " +
              str(error) + '\n' +
              str(error.__doc__) + '\n' +
              str(error.__traceback__)  + '\n' +
              #traceback.print_exc() + '\n' +
              str(type(error).__name__) + '\n' +
              str(sys.exc_info()[0]) + "occurred." + '\n'
              #traceback.format_exc()
              )
        print('\n\n\n Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(error).__name__, error)

def open_calculator():
    value, ok = QInputDialog.getDouble(
        window, # parent widget
        'Tax Calculator', # window title
        'Yearly Income:', # entry label
        min=0.0,
        max=1000000.0,
    )
    if not ok:
        return
    yearly_income.setText('Yearly Income: ${:,.2f}'.format(value))
    if value <= 9700:
        rate = 10.0
    elif value <= 39475:
        rate = 12.0
    elif value <= 84200:
        rate = 22.0
    elif value <= 160725:
        rate = 24.0
    elif value <= 204100:
        rate = 32.0
    tax_rate.setText('Highest Marginal Tax Rate: {}%'.format(rate))

def poplulateTestData():

    columns = ('Week', 'Hours Worked', 'Hourly Rate', 'Earned Income')

    table_data = [[7, 40.0, 100.0],
                  [8, 37.5, 85.0],
                  [9, 65, 150.0],]

    table = QTableWidget()
    table.setColumnCount(len(columns))
    table.setHorizontalHeaderLabels(columns)
    table.setRowCount(len(table_data))
    # layout.addWidget(table, 2, 0, 1, 2)

    layout.addWidget(table, 3, 0)  # Table Adding to 4 Row on Form/Window

    for row_index, row in enumerate(table_data):
        # Set each column value in the table
        for column_index, value in enumerate(row):
            item = QTableWidgetItem(str(value))
            table.setItem(row_index, column_index, item)
        # Calculate the total and add it as another column
        table.setItem(row_index, 3, QTableWidgetItem(str(row[1] * row[2])))


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


def readSQLLiteDB(
        self):  # ---------------------------- SQLLite Database -------------------------------------------
    # https://pythonspot.com/python-database/
    # https://pythonspot.com/python-database-programming-sqlite-tutorial/
    import pandas as pd
    import sqlite3

    conn = sqlite3.connect('population.db')
    query = "SELECT country FROM Population WHERE population > 50000000;"

    df = pd.read_sql_query(query, conn)

    for country in df['country']:
        print(country)


def readMySQLDB(
        self):  # ---------------------------- MySQL Database -----------------------------------------------
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


def readExcel(excelFileName):  # -------------------------- Excel Files  -----------------------------------------------
    # https://pythonspot.com/read-xls-with-pandas/
    import pandas as pd
    import openpyxl

    try:
        #file = r'data/Presidents.xls'
        # df = pd.read_excel(file)
        showMessage("File Name : " + str(excelFileName) + "From readExcel")
        #wb = openpyxl.load_workbook(excelFileName)
        #showMessage(wb.sheetnames)

        #def read_excel_sheets(xls_path):
        """Read all sheets of an Excel workbook and return a single DataFrame"""
        showMessage(f'Loading {excelFileName} into pandas')
        xl = pd.ExcelFile(excelFileName)
        df = pd.DataFrame()
        columns = None
        for idx, name in enumerate(xl.sheet_names):
            showMessage(f'Reading sheet #{idx}: {name}')
            sheet = xl.parse(name)
            if idx == 0:
                # Save column names from the first sheet to match for append
                columns = sheet.columns
            sheet.columns = columns
            # Add sheet name as column
            sheet['sheet'] = name.split(" ")[-1]
            # Assume index of existing data frame when appended
            df = df.append(sheet, ignore_index=True)
        #    return df

        print(df)

    # df = pd.read_excel(excelFileName, sheetname='Elected presidents')
    #
    # # remove messy data
    # df = df[df['Years in office'] != 'n/a']
  #------------------------ Copied Code Start Here ---------------------------------
        header = df.iloc[0]
        print("Dataframe Details : " + '\n\n' + str(header))

        tableColumns= df.columns
        print("Header2 Row : " + '\n\n' + str(tableColumns))

        ### ask for header
        ret = QMessageBox.question(widget, "Excel File View",
                                   "Do you wish to populate first row as Header?\n\n" + str(header.values),
                                   QMessageBox.Ok | QMessageBox.No, defaultButton=QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            df = df[1:]

            selFiletable = QTableWidget()
            selFiletable.setHorizontalHeaderLabels(df.columns)
            # layout.addWidget(table, 2, 0, 1, 2)
            layout.addWidget(selFiletable, 3, 0)  # Table Adding to 4 Row on Form/Window
            selFiletable.setColumnCount(len(df.columns))
            selFiletable.setRowCount(len(df.index))

            for row_index, row in enumerate(df):
                # Set each column value in the table
                for column_index, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    print("Row : " + str(row_index) + " - Column : " + str(column_index))
                    selFiletable.setItem(row_index, column_index, item)
                    # Derived Columns, Calculate the total and add it as another column
                    #selFiletable.setItem(row_index, 3, QTableWidgetItem(str(row[1] * row[2])))

            # for i in range(len(df.index)):
            #     for j in range(len(df.columns)):
            #         selFiletable.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

            # Populate Table Columns Headers
            for j in range(len(df.columns)):
                m = QTableWidgetItem(tableColumns[j])
                selFiletable.setHorizontalHeaderItem(j, m)
        else:
            selFiletable = QTableWidget()
            selFiletable.setColumnCount(len(df.columns))
            selFiletable.setRowCount(len(df.index))
            selFiletable.setHorizontalHeaderLabels(df.columns)

            # layout.addWidget(table, 2, 0, 1, 2)
            layout.addWidget(selFiletable, 3, 0)  # Table Adding to 4 Row on Form/Window

            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    selFiletable.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

            # Populate Table Columns Headers programatically
            # for j in range(len(df.columns)):
            #     m = QTableWidgetItem(tableColumns[j])
            #     selFiletable.setHorizontalHeaderItem(j, m)

        selFiletable.selectRow(0)
        selFiletable.resizeColumnsToContents()
        selFiletable.resizeRowsToContents()

        showMessage(excelFileName + " loaded")
    # ------------------------ Copied Code Ends Here ---------------------------------

    except Exception as error:
        print(str(error) + " Occured in readExcel Method")
        showException(" Occured in readExcel")

def readXML(xmlFileName): # ------------------------------------------- Read XML File --------------------------------
    from lxml import objectify
    import pandas as pd
    try:
        xml_data = objectify.parse(xmlFileName)  # Parse XML data
        root = xml_data.getroot()  # Root element

        data = []
        cols = []
        for i in range(len(root.getchildren())):
            child = root.getchildren()[i]
            data.append([subchild.text for subchild in child.getchildren()])
            cols.append(child.tag)

        df = pd.DataFrame(data).T  # Create DataFrame and transpose it
        df.columns = cols  # Update column names
        print(df)

        header = df.iloc[0]
        print("Dataframe Details : " + '\n\n' + str(header))

        tableColumns= df.columns
        print("Header2 Row : " + '\n\n' + str(tableColumns))

        ### ask for header
        ret = QMessageBox.question(widget, "XML File View",
                                   "Do you wish to populate first row as Header?\n\n" + str(header.values),
                                   QMessageBox.Ok | QMessageBox.No, defaultButton=QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            df = df[1:]

            selFiletable = QTableWidget()
            selFiletable.setHorizontalHeaderLabels(df.columns)
            # layout.addWidget(table, 2, 0, 1, 2)
            layout.addWidget(selFiletable, 3, 0)  # Table Adding to 4 Row on Form/Window
            selFiletable.setColumnCount(len(df.columns))
            selFiletable.setRowCount(len(df.index))

            for row_index, row in enumerate(df):
                # Set each column value in the table
                for column_index, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    print("Row : " + str(row_index) + " - Column : " + str(column_index))
                    selFiletable.setItem(row_index, column_index, item)
                    # Derived Columns, Calculate the total and add it as another column
                    #selFiletable.setItem(row_index, 3, QTableWidgetItem(str(row[1] * row[2])))

            # for i in range(len(df.index)):
            #     for j in range(len(df.columns)):
            #         selFiletable.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

            # Populate Table Columns Headers
            for j in range(len(df.columns)):
                m = QTableWidgetItem(tableColumns[j])
                selFiletable.setHorizontalHeaderItem(j, m)
        else:
            selFiletable = QTableWidget()
            selFiletable.setColumnCount(len(df.columns))
            selFiletable.setRowCount(len(df.index))
            selFiletable.setHorizontalHeaderLabels(df.columns)

            # layout.addWidget(table, 2, 0, 1, 2)
            layout.addWidget(selFiletable, 3, 0)  # Table Adding to 4 Row on Form/Window

            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    selFiletable.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

            # Populate Table Columns Headers programatically
            # for j in range(len(df.columns)):
            #     m = QTableWidgetItem(tableColumns[j])
            #     selFiletable.setHorizontalHeaderItem(j, m)

        selFiletable.selectRow(0)
        selFiletable.resizeColumnsToContents()
        selFiletable.resizeRowsToContents()

        showMessage(xmlFileName + " loaded")
    except Exception as error:
        print(str(error) + " Occured in readXML Method")
        showException(" Occured in readXML")

def readCSV(csvfilename):  # ---------------------------------- CSV Files  -----------------------------------------------
    # https://pythonspot.com/pandas-read-csv/
    import pandas as pd

    try:
        file = csvfilename
        if csvfilename:
            df = pd.read_csv(csvfilename,
                             #header=None,
                             delimiter=','
                             #, keep_default_na=False
                             )  # , error_bad_lines=False)
            # print(df.shape)
            header = df.iloc[0]
            print("Dataframe Details : " + '\n\n' + str(header))

            tableColumns= df.columns
            print("Header2 Row : " + '\n\n' + str(tableColumns))

            ### ask for header
            ret = QMessageBox.question(widget, "CSV File View",
                                       "Do you wish to populate first row as Header?\n\n" + str(header.values),
                                       QMessageBox.Ok | QMessageBox.No, defaultButton=QMessageBox.Ok)
            if ret == QMessageBox.Ok:
                df = df[1:]

                selFiletable = QTableWidget()
                selFiletable.setHorizontalHeaderLabels(df.columns)
                # layout.addWidget(table, 2, 0, 1, 2)
                layout.addWidget(selFiletable, 3, 0)  # Table Adding to 4 Row on Form/Window
                selFiletable.setColumnCount(len(df.columns))
                selFiletable.setRowCount(len(df.index))

                for row_index, row in enumerate(df):
                    # Set each column value in the table
                    for column_index, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        print("Row : " + str(row_index) + " - Column : " + str(column_index))
                        selFiletable.setItem(row_index, column_index, item)
                        # Derived Columns, Calculate the total and add it as another column
                        #selFiletable.setItem(row_index, 3, QTableWidgetItem(str(row[1] * row[2])))

                # for i in range(len(df.index)):
                #     for j in range(len(df.columns)):
                #         selFiletable.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

                # Populate Table Columns Headers
                for j in range(len(df.columns)):
                    m = QTableWidgetItem(tableColumns[j])
                    selFiletable.setHorizontalHeaderItem(j, m)
            else:
                selFiletable = QTableWidget()
                selFiletable.setColumnCount(len(df.columns))
                selFiletable.setRowCount(len(df.index))
                selFiletable.setHorizontalHeaderLabels(df.columns)

                # layout.addWidget(table, 2, 0, 1, 2)
                layout.addWidget(selFiletable, 3, 0)  # Table Adding to 4 Row on Form/Window

                for i in range(len(df.index)):
                    for j in range(len(df.columns)):
                        selFiletable.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

                # Populate Table Columns Headers programatically
                # for j in range(len(df.columns)):
                #     m = QTableWidgetItem(tableColumns[j])
                #     selFiletable.setHorizontalHeaderItem(j, m)

            selFiletable.selectRow(0)
            selFiletable.resizeColumnsToContents()
            selFiletable.resizeRowsToContents()

        showMessage(csvfilename + " loaded")
    except Exception as error:
        print(str(error) + " Occured in readCSV Method")
        showException(" Occured in readCSV")

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


def showReport(self):  # ---------------------------------- Analytics -------------------------------------------
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


def logMessage(logMsg):  # ---------------------------------- Logging Module ------------------------------------
    print(logMsg)


def showMessage1(self):  # ---------------------------------- Show Info Module -----------------------------------
    buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if buttonReply == QMessageBox.Yes:
        print('Yes clicked.')
    else:
        print('No clicked.')


def showCustomMessage1(self, mesg):
    print('Start showCustomMessage - mesg : ' + mesg)
    try:
        buttonReply = QMessageBox.question(self, 'PyQt5 message', mesg,
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                           QMessageBox.Cancel)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        if buttonReply == QMessageBox.Cancel:
            print('Cancel')
    except Exception as e:
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


window.setCentralWidget(widget)
window.show()
app.exec_()