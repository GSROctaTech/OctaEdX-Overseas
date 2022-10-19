import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class ReadOnlyDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, *args, **kwargs):
        return

class Table(QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTableWidget.__init__(self, *args, **kwargs)
        self.setItemDelegate(ReadOnlyDelegate(self))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            it = self.itemAt(event.pos())
            new_text = round(float(it.text()) + 1,2)
            it.setText(str(new_text))

        elif event.button() == QtCore.Qt.RightButton:
            it = self.itemAt(event.pos())
            new_text = round(float(it.text()) - 1,2)
            it.setText(str(new_text))
        QtWidgets.QTableWidget.mousePressEvent(self, event)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        table = Table(15, 15)
        self.setCentralWidget(table)
        for i in range(15):
            for j in range(15):
                item = QtWidgets.QTableWidgetItem("{}".format(i*j))
                table.setItem(i, j, item)

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())