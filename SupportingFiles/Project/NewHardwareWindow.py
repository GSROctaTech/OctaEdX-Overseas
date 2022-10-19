from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import datetime


class Ui_NewHardwareWindow(object):
    def setupUi(self, NewHardwareWindow):
        super().__init__()
        NewHardwareWindow.setObjectName("NewHardwareWindow")
        NewHardwareWindow.resize(265, 167)
        NewHardwareWindow.setWindowTitle('NEW HARDWARE')
        NewHardwareWindow.setMinimumSize(265, 167)
        NewHardwareWindow.setMaximumSize(265, 167)

        font_label = QtGui.QFont()
        font_label.setFamily('MS UI Gothic')
        font_label.setPointSize(10)

        font_button = QtGui.QFont()
        font_button.setFamily('MS UI Gothic')
        font_button.setPointSize(9)

        self.centralwidget = QtWidgets.QWidget(NewHardwareWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_serialnumber = QtWidgets.QLabel(self.centralwidget)
        self.label_serialnumber.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.label_serialnumber.setText("SERIAL NUMBER")
        self.label_serialnumber.setFont(font_label)
        self.label_serialnumber.setObjectName("label_serialnumber")

        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_model.setText('MODEL')
        self.label_model.setFont(font_label)
        self.label_model.setObjectName("label_model")

        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_user.setText('USER')
        self.label_user.setFont(font_label)
        self.label_user.setObjectName("label_user")

        self.textbox_serialnumber = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_serialnumber.setGeometry(QtCore.QRect(110, 20, 121, 16))
        self.textbox_serialnumber.setObjectName("textbox_serialnumber")
        self.textbox_serialnumber.returnPressed.connect(self.EnterNewHardware)

        self.textbox_model = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_model.setGeometry(QtCore.QRect(110, 50, 121, 16))
        self.textbox_model.setObjectName("textbox_model")
        self.textbox_model.returnPressed.connect(self.EnterNewHardware)

        self.textbox_username = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_username.setGeometry(QtCore.QRect(110, 80, 121, 16))
        self.textbox_username.setObjectName("textbox_username")
        self.textbox_username.returnPressed.connect(self.EnterNewHardware)

        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(110, 110, 61, 31))
        self.button_clear.setText('CLEAR')
        self.button_clear.setFont(font_button)
        self.button_clear.setObjectName("button_clear")
        self.button_clear.clicked.connect(self.ClearTextBoxes)

        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(170, 110, 61, 31))
        self.button_enter.setText('ENTER')
        self.button_enter.setFont(font_button)
        self.button_enter.setObjectName("button_enter")
        self.button_enter.clicked.connect(self.EnterNewHardware)
        self.button_enter.setAutoDefault(True)

        self.statusbar = QtWidgets.QStatusBar(NewHardwareWindow)
        self.statusbar.setObjectName("statusbar")

        NewHardwareWindow.setCentralWidget(self.centralwidget)
        NewHardwareWindow.setStatusBar(self.statusbar)

    def EnterNewHardware(self):
        serial_number = self.textbox_serialnumber.text()
        model = self.textbox_model.text()
        user_name = self.textbox_username.text()
        creation_date = datetime.datetime.now().strftime('%m/%d/%y')
        modify_date = datetime.datetime.now().strftime('%m/%d/%y')

        print(creation_date)
        print(modify_date)
        print(serial_number)
        print(model)
        print(user_name)

        azure_server = 'pythonserver5874.database.windows.net'
        azure_db = 'inventoryDatabase'
        azure_username = ''
        password = ''
        driver = '{ODBC Driver 17 for SQL Server}'
        connection_string = f"DRIVER={driver};SERVER={azure_server};PORT=1433;DATABASE={azure_db};UID={azure_username};PWD={password}"

        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        sql_statement = 'INSERT INTO inventoryDatabase.dbo.Hardware(CreationDate, ModifyDate, SerialNumber, Model, Username) ' \
                        'VALUES (?, ?, ?, ?, ?)'

        sql_data = (creation_date, modify_date, serial_number, model, user_name)

        if self.textbox_serialnumber.text() == "":
            self.statusbar.showMessage("Enter serial number")
        elif self.textbox_model.text() == "":
            self.statusbar.showMessage("Enter model")
        elif self.textbox_username.text() == "":
            self.statusbar.showMessage("Enter username")
        else:
            cursor.execute(sql_statement, sql_data)
            conn.commit()
            cursor.commit()

            self.textbox_serialnumber.clear()
            self.textbox_model.clear()
            self.textbox_username.clear()
            self.statusbar.showMessage(serial_number + " has been entered")
            self.textbox_serialnumber.setFocus()

    def ClearTextBoxes(self):
        self.textbox_serialnumber.clear()
        self.textbox_model.clear()
        self.textbox_username.clear()