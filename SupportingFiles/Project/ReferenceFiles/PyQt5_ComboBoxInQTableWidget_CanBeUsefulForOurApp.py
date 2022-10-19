import sys
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle('PyQt Tuts')
        self.table()


    def table(self):

        comboBox = QtWidgets.QComboBox()

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(220, 100, 411, 392))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.tableWidget.show()

        # attr = ['one', 'two', 'three', 'four', 'five']
        # i = 0
        # for j in attr:
        #     self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(j))
        #     self.tableWidget.setCellWidget(i, 1, comboBox)
        #     i += 1

        attr = ['one', 'two', 'three', 'four', 'five']
        i = 0
        for j in attr:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(j))
            comboBox = QtWidgets.QComboBox()
            self.tableWidget.setCellWidget(i, 1, comboBox)
            i += 1

        for r in range(self.tableWidget.rowCount()):
            for c in range(self.tableWidget.columnCount()):
                widget = self.tableWidget.cellWidget(r, c)
                if isinstance(widget, QtWidgets.QComboBox):
                    current_value = widget.currentText()
                    print(current_value)


def run():
    app = QtWidgets.QApplication(sys.argv)      
    w = Window()
    sys.exit(app.exec_())      

run()