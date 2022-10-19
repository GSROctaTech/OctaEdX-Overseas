import sys
from PyQt5 import QtWidgets, QtGui, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *


prev_day = "2020-10-15"
query_result = [(683, 18, 765, 1.73, '1 ring ruby ring', 685.71, 'vincent percy', 'john joseph croft'), (684, 14, 900, 4.48, '1 earring ear drop', 534.86, 'Ben Otten', 'Anne Cooksley Beltrame'), (684, 14, 900, 2.1, '1 ring cluster ring', 534.86, 'Ben Otten', 'Anne Cooksley Beltrame'), (684, 18, 900, 1.3, '1 ring eternity band', 685.71, 'Ben Otten', 'Anne Cooksley Beltrame'), (685, 14, 200, 3.26, '1 ring promise ring', 534.86, 'raymond bob', 'owen george taylor'), (686, 24, 450, 10.0, '1 bullion Gold bar', 914.28, 'vincent percy', 'owen george taylor'), (687, 14, 345, 4.75, '1 earring Dangles Earring', 534.86, 'Ben Otten', 'dan justin balmers'), (688, 18, 810, 3.1, '1 earring fish hookEarring', 677.14, 'raymond bob', 'jeff david steve'), (688, 21, 810, 2.6, '1 ring ANTIQUE RING', 790, 'raymond bob', 'jeff david steve')]


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mini_ui")
        self.setGeometry(300, 150, 800, 600)
        self.Ui()

    def Ui(self):
        vbox = QVBoxLayout()
        btn_show_table = QPushButton("view sample data")
        btn_show_table.clicked.connect(self.today_sales_table)
        self.viewTodayTable = QTableWidget()
        self.viewTodayTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.viewTodayTable.setObjectName("viewTodayTable")
        self.viewTodayTable.setColumnCount(8)
        self.viewTodayTable.setRowCount(0)
        self.viewTodayTable.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Order ID"))
        self.viewTodayTable.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Karat"))
        self.viewTodayTable.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Price"))
        self.viewTodayTable.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Weight"))
        self.viewTodayTable.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Description"))
        self.viewTodayTable.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Gram price"))
        self.viewTodayTable.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem("Employee"))
        self.viewTodayTable.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem("Client"))
        self.viewTodayTable.horizontalHeader().setDefaultSectionSize(130)
        self.viewTodayTable.horizontalHeader().setSortIndicatorShown(True)
        self.viewTodayTable.horizontalHeader().setStretchLastSection(True)

        vbox.addWidget(btn_show_table)
        vbox.addWidget(self.viewTodayTable)
        self.setLayout(vbox)

        self.show()

    def apply_span_to_sales_table(self, row, nrow):
        if nrow <= 1:
            return
        for c in (0, 2, 6, 7):
            self.viewTodayTable.setSpan(row, c, nrow, 1)
            for r in range(row + 1, row + nrow):
                t = self.viewTodayTable.takeItem(r, c)
                del t

    def today_sales_table(self):
        today_result = query_result
        self.viewTodayTable.setRowCount(0)

        last_id = -1
        start_row = 0
        for row_number, row_data in enumerate(today_result):
            self.viewTodayTable.insertRow(row_number)
            current_id, *other_values = row_data

            for column_number, data in enumerate(row_data):
                it = QtWidgets.QTableWidgetItem(str(data))

                self.viewTodayTable.setItem(row_number, column_number, it)

                if current_id % 2 == 1:
                    self.viewTodayTable.item(row_number, column_number).setBackground(QColor(185, 206, 172))
                    print("whats up")
                elif current_id % 2 == 0:
                    self.viewTodayTable.item(row_number, column_number).setBackground(QColor(193, 171, 206))
                    print("whats up 2")

                if last_id != current_id and last_id != -1:
                    self.apply_span_to_sales_table(start_row, row_number - start_row)
                    start_row = row_number

                last_id = current_id
                if start_row != row_number:
                    self.apply_span_to_sales_table(start_row, self.viewTodayTable.rowCount() - start_row)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()