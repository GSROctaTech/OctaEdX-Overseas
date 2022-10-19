from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtPrintSupport import *
import sys, sqlite3, time
import os


class UpdateDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Update")

        self.setWindowTitle("Update Query")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.updateQuery)

        layout = QVBoxLayout()

        self.idinput = QLineEdit()
        self.idinput.setPlaceholderText("Id")
        layout.addWidget(self.idinput)

        self.fnameinput = QLineEdit()
        self.fnameinput.setPlaceholderText("First name")
        layout.addWidget(self.fnameinput)

        self.lnameinput = QLineEdit()
        self.lnameinput.setPlaceholderText("Last name")
        layout.addWidget(self.lnameinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def updateQuery(self):

        fname = self.fnameinput.text()
        lname = self.lnameinput.text()
        id_ = self.idinput.text()
        try:
            self.conn = sqlite3.connect("people.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE people SET fname=?,lname=? WHERE id=?", (fname, lname, id_))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Database updated successfully.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not update the database.')


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.conn = sqlite3.connect("people.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS people(id INTEGER PRIMARY KEY AUTOINCREMENT ,fname TEXT,lname TEXT)")
        self.c.close()

        self.setWindowTitle("Table update example")

        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Id", "First name", "Last name"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_updateuser = QAction(QIcon("icon/refresh.png"), "Update Query", self)
        btn_ac_updateuser.triggered.connect(self.update)
        btn_ac_updateuser.triggered.connect(self.loaddata)
        btn_ac_updateuser.setStatusTip("Update Query")
        toolbar.addAction(btn_ac_updateuser)

    def loaddata(self):
        self.connection = sqlite3.connect("people.db")
        query = "SELECT * FROM people"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def update(self):
        dlg = UpdateDialog()
        dlg.exec_()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.loaddata()
sys.exit(app.exec())