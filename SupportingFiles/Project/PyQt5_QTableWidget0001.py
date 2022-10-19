import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDropEvent
from PyQt5.QtWidgets import (QTableWidget, QAbstractItemView, QTableWidgetItem,
                             QHBoxLayout, QApplication, QMainWindow)


class TableWidgetDragRows(QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)

        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setDragDropMode(QAbstractItemView.InternalMove)

    def dropEvent(self, event: QDropEvent):
        if not event.isAccepted() and event.source() == self:
            drop_row = self.drop_on(event)

            rows = sorted(set(item.row() for item in self.selectedItems()))
            rows_to_move = [
                [QTableWidgetItem(self.item(row_index, column_index)) for column_index in range(self.columnCount())]
                for row_index in rows]
            for row_index in reversed(rows):
                self.removeRow(row_index)
                if row_index < drop_row:
                    drop_row -= 1

            for row_index, data in enumerate(rows_to_move):
                row_index += drop_row
                self.insertRow(row_index)
                for column_index, column_data in enumerate(data):
                    self.setItem(row_index, column_index, column_data)
            event.accept()
            for row_index in range(len(rows_to_move)):
                self.item(drop_row + row_index, 0).setSelected(True)
                self.item(drop_row + row_index, 1).setSelected(True)
        super().dropEvent(event)

    def drop_on(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return self.rowCount()

        return index.row() + 1 if self.is_below(event.pos(), index) else index.row()

    def is_below(self, pos, index):
        rect = self.visualRect(index)
        margin = 2
        if pos.y() - rect.top() < margin:
            return False
        elif rect.bottom() - pos.y() < margin:
            return True
        # noinspection PyTypeChecker
        return rect.contains(pos, True) and not (
                    int(self.model().flags(index)) & Qt.ItemIsDropEnabled) and pos.y() >= rect.center().y()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.table_widget = TableWidgetDragRows()
        self.table_widget.itemClicked.connect(self.get_item)
        self.setCentralWidget(self.table_widget)

        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Type', 'Name'])

        items = [('Red', 'Toyota'), ('Blue', 'RV'), ('Green', 'Beetle'), ('Silver', 'Chevy'), ('Black', 'BMW')]
        self.table_widget.setRowCount(len(items))
        for i, (color, model) in enumerate(items):
            self.table_widget.setItem(i, 0, QTableWidgetItem(color))
            self.table_widget.setItem(i, 1, QTableWidgetItem(model))

        self.statusBar().showMessage("Ready", 0)
        self.resize(400, 400)
        self.show()

    def get_item(self):
        selItems=[]
        item = self.table_widget.selectedItems()[0]
        if not item == None:
            name = item.text()
        else:
            name = ""
        print(name)
        self.statusBar().showMessage(name, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())