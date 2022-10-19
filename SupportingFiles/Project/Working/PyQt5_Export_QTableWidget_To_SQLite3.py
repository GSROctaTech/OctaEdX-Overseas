# https://stackoverflow.com/questions/53035570/export-qtablewidgets-data-columns-rows-everything-to-sqlite3
import sqlite3
import pandas as pd
from PyQt5 import QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.table_widget = QtWidgets.QTableWidget()
        self.create_data()
        button = QtWidgets.QPushButton("Export")
        button.clicked.connect(self.on_clicked)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.table_widget)
        lay.addWidget(button)

    def create_data(self):
        self.table_widget.setColumnCount(4)
        self.table_widget.setRowCount(10)
        self.table_widget.setHorizontalHeaderLabels(["A", "B", "C", "D"])

        import random
        for i in range(self.table_widget.rowCount()):
            for j in range(self.table_widget.columnCount()):
                it = QtWidgets.QTableWidgetItem(str(random.randint(0, 100)))
                self.table_widget.setItem(i, j, it)

    def on_clicked(self):
        proceed = QtWidgets.QMessageBox.question(self,
            'Information',
            'Have you Verified your Data?',
            QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if proceed != QtWidgets.QMessageBox.Yes:
            return

        filename, ok = QtWidgets.QInputDialog.getText(self, 'Almost Done !', 'name your file :')
        if ok:
            self.saveToDb(filename, "table_name")

    def saveToDb(self, db_filename, tablename):
        d = {}
        for i in range(self.table_widget.columnCount()):
            l = []
            for j in range(self.table_widget.rowCount()):
                it = self.table_widget.item(j, i)
                l.append(it.text() if it is not None else "")
            h_item = self.table_widget.horizontalHeaderItem(i)
            n_column = str(i) if h_item is None else h_item.text()
            d[n_column] = l

        df = pd.DataFrame(data=d)
        engine = sqlite3.connect(db_filename)
        df.to_sql(tablename, con=engine)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())