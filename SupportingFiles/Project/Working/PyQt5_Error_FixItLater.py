# https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import pandas as pd


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    # def data(self, index, role):
    #     if role == Qt.DisplayRole:
    #         value = self._data.iloc[index.row(), index.column()]
    #         return str(value)

    # ticks and crosses for `bool`values
    def data(self, index, role):
        # existing `if role == Qt.DisplayRole:` block hidden
        # hidden for clarity.

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon('tick.png')
                return QtGui.QIcon('cross.png')

        # color blocks
        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if (isinstance(value, int) or isinstance(value, float)):
                value = int(value)
                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)  # valaues > +5 become +5
                value = value + 5  # -5 becomes 0, +5 becomes + 10

                return QtGui.QColor(COLORS[value])

    # #  icons indicating data type
    # def data(self, index, role):
    #     if role == Qt.DisplayRole:
    #         value = self._data[index.row()][index.column()]
    #         if isinstance(value, datetime):
    #             return value.strftime('%Y-%m-%d')
    #         return value
    #     if role == Qt.DecorationRole:
    #         value = self._data[index.row()][index.column()]
    #         if isinstance(value, datetime):
    #             return QtGui.QIcon('calendar.png')

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = pd.DataFrame([
          [1, 9, 2],
          [1, 0, -1],
          [3, 5, 2],
          [3, 3, 2],
          [5, 8, 9],
        ], columns = ['A', 'B', 'C'], index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()