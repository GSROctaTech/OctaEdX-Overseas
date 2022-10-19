import sys
from PyQt5 import QtCore, QtWidgets

class Main(QtWidgets.QTableWidget):
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            row = self.currentRow()
            self.removeRow(row)
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()

    main.setColumnCount(3)
    for i in range(40):
        main.insertRow(main.rowCount())
        for j in range(main.columnCount()):
            main.setItem(i, j, QtWidgets.QTableWidgetItem(f'row {i}, column{j}'))

    main.show()
    sys.exit(app.exec_())