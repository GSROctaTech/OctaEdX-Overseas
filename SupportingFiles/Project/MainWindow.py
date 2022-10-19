# https://python-forum.io/thread-33067.html
# Other Module File : NewHardwareWindow.py
from PyQt5 import QtCore, QtGui, QtWidgets
from NewHardwareWindow import Ui_NewHardwareWindow
import sys
import pyodbc

class Ui_MainWindow(object):
    def SetupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Hardware Inventory")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(900, 350)
        MainWindow.setMaximumSize(QtCore.QSize(900, 350))
        MainWindow.setMinimumSize(QtCore.QSize(900, 350))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet('')
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(8)

        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")

        self.TableWidget = QtWidgets.QTableWidget(self.CentralWidget)
        self.TableWidget.setGeometry(QtCore.QRect(120, 10, 770, 340))
        self.TableWidget.setSortingEnabled(True)
        self.TableWidget.setRowCount(0)
        self.TableWidget.setColumnCount(5)
        self.TableWidget.setObjectName("TableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(4, item)
        item = self.TableWidget.horizontalHeaderItem(0)
        item.setText("Creation Date")
        item = self.TableWidget.horizontalHeaderItem(1)
        item.setText("Last Modified")
        item = self.TableWidget.horizontalHeaderItem(2)
        item.setText("Serial Number")
        item = self.TableWidget.horizontalHeaderItem(3)
        item.setText("Model")
        item = self.TableWidget.horizontalHeaderItem(4)
        item.setText("User")

        self.textbox_search = QtWidgets.QLineEdit(self.CentralWidget)
        self.textbox_search.setGeometry(QtCore.QRect(10, 10, 101, 15))
        self.textbox_search.setObjectName("textbox_model")
        self.textbox_search.setText('')
        self.textbox_search.setFocus()
        self.textbox_search.returnPressed.connect(self.SearchHardware)

        self.button_search = QtWidgets.QPushButton(self.CentralWidget)
        self.button_search.setText("SEARCH")
        self.button_search.setGeometry(QtCore.QRect(10, 30, 101, 18))
        self.button_search.setFont(font)
        self.button_search.setObjectName("button_search")
        self.button_search.clicked.connect(self.SearchHardware)
        self.button_search.setAutoDefault(True)

        self.button_new_hardware = QtWidgets.QPushButton(self.CentralWidget)
        self.button_new_hardware.setText("NEW HARDWARE")
        self.button_new_hardware.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.button_new_hardware.setFont(font)
        self.button_new_hardware.setObjectName("button_new_hardware")
        self.button_new_hardware.setAutoDefault(True)
        self.button_new_hardware.clicked.connect(self.EnterNewHardwareWindow)

        self.button_viewall = QtWidgets.QPushButton(self.CentralWidget)
        self.button_viewall.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.button_viewall.setFont(font)
        self.button_viewall.setObjectName("button_viewall")
        self.button_viewall.setText('VIEW ENTIRE DB')
        self.button_viewall.setAutoDefault(True)
        self.button_viewall.clicked.connect(self.ViewAll)

        self.button_export = QtWidgets.QPushButton(self.CentralWidget)
        self.button_export.setGeometry(QtCore.QRect(10, 140, 101, 31))
        self.button_export.setFont(font)
        self.button_export.setObjectName("button_export")
        self.button_export.setText('EXPORT')

        MainWindow.setCentralWidget(self.CentralWidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def EnterNewHardwareWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewHardwareWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def SearchHardware(self):
        user_search = self.textbox_search.text()
        azure_server = 'pythonserver5874.database.windows.net'
        azure_db = 'inventoryDatabase'
        azure_username = ''
        password = ''
        driver = '{ODBC Driver 17 for SQL Server}'
        connection_string = f"DRIVER={driver};SERVER={azure_server};PORT=1433;DATABASE={azure_db};UID={azure_username};PWD={password}"
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        sql_statement = '''SELECT CreationDate, ModifyDate, SerialNumber, Model, Username FROM inventoryDatabase.dbo.Hardware WHERE SerialNumber = (?) OR Model = (?) OR Username = (?);'''
        result = cursor.execute(sql_statement, user_search, user_search, user_search)

        self.TableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.TableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def ViewAll(self):
        azure_server = 'pythonserver5874.database.windows.net'
        azure_db = 'inventoryDatabase'
        azure_username = ''
        password = ''
        driver = '{ODBC Driver 17 for SQL Server}'
        connection_string = f"DRIVER={driver};SERVER={azure_server};PORT=1433;DATABASE={azure_db};UID={azure_username};PWD={password}"
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        sql_statement = '''SELECT CreationDate, ModifyDate, SerialNumber, Model, Username FROM inventoryDatabase.dbo.Hardware'''
        result = cursor.execute(sql_statement)

        self.TableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.TableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.SetupUi(window)
    window.show()
    sys.exit(app.exec_())