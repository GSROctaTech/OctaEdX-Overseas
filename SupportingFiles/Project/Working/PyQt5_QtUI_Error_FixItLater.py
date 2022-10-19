import sys
from PyQt5 import QtCore, QtWidgets, uic
import pandas as pd
import numpy as np

form_class = uic.loadUiType("DataProcessing.ui")[0]

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df = pd.DataFrame(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        return super(PandasModel, self).headerData(section, orientation, role)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if not index.isValid():
            return QtCore.QVariant()
        if index.row() == 0:
            return QtCore.QVariant(self._df.columns.values[index.column()])
        return QtCore.QVariant(str(self._df.iloc[index.row()-1, index.column()]))

    def setData(self, index, value, role):
        if index.row() == 0:
            if isinstance(value, QtCore.QVariant):
                value = value.value()
            if hasattr(value, 'toPyObject'):
                value = value.toPyObject()
            self._df.columns.values[index.column()] = value
            self.headerDataChanged.emit(QtCore.Qt.Horizontal, index.column(), index.column())
        else:
            col = self._df.columns[index.column()]
            row = self._df.index[index.row()-1]
            if isinstance(value, QtCore.QVariant):
                value = value.value()
            if hasattr(value, 'toPyObject'):
                value = value.toPyObject()
            else:
                dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
                self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.index) +1

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        value = index.data()
        options = [value, 'Option 1','Option 2','Option 3','Option 4','Default']
        editor.addItems(options)
        editor.currentTextChanged.connect(self.commitAndCloseEditor)
        return editor

    @QtCore.pyqtSlot()
    def commitAndCloseEditor(self):
        editor = self.sender()
        self.commitData.emit(editor)


class MyWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.PushButtonDisplay.clicked.connect(self.IP_Data_Display)
        self.PushButtonImport.clicked.connect(self.IP_File_Import)
        delegate = ComboBoxDelegate(self.TView)
        self.TView.setItemDelegateForRow(0, delegate)

    def IP_Data_Display(self):
        DT_Disp = self.CBdisplay.currentText()
        data = pd.read_csv('Example.csv')
        data = data.sort_index()
        model = PandasModel(data)
        self.TView.setModel(model)
        for i in range(model.columnCount()):
            ix = model.index(0, i)
            self.TView.openPersistentEditor(ix)

    def IP_File_Import(self):
        newModel = self.TView.model()
        dataFrame = newModel._df.copy()
        dataFrame.to_csv('Test.csv') #, index=False, header=False)


if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))
    main = MyWindowClass(None)
    main.show()

    sys.exit(app.exec_())