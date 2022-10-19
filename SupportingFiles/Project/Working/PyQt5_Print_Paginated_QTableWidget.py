# https://gist.github.com/chris-marsh/351febf755c05a4e57cf4dc2b625aab1

from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.table = QtWidgets.QTableWidget(200, 5, self)

        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QtWidgets.QTableWidgetItem('(%d, %d)' % (row, col))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row, col, item)
        self.table.setHorizontalHeaderLabels(
            'SKU #|NAME|DESCRIPTION|QUANTITY|PRICE'.split('|'))
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    # Commented - G.S.Reddy - Commented below & Added modified below method to add more functionality
    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        table = cursor.insertTable(
            self.table.rowCount(), self.table.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.table.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)

    # # Added - G.S.Reddy - Commented Above & Added modified below method to add more functionality
    # def handlePaintRequest(self, printer):
    #     document = QtGui.QTextDocument()
    #     cursor = QtGui.QTextCursor(document)
    #     rows = self.tableData.rowCount()
    #     columns = self.tableData.columnCount()
    #     tableData = cursor.insertTable(rows + 1, columns)
    #     format = tableData.format()
    #     ### style
    #     format.setBorder(1)
    #     format.setBorderStyle(3)
    #     format.setCellSpacing(0);
    #     format.setTopMargin(0);
    #     format.setCellPadding(4)
    #     ###
    #     format.setHeaderRowCount(1)
    #     tableData.setFormat(format)
    #     format = cursor.blockCharFormat()
    #     for column in range(columns):
    #         cursor.setCharFormat(format)
    #         cursor.insertText(self.tableData.horizontalHeaderItem(column).text())
    #         cursor.movePosition(QtGui.QTextCursor.NextCell)
    #     for row in range(rows):
    #         for column in range(columns):
    #             cursor.insertText(self.tableData.item(row, column).text())
    #             cursor.movePosition(QtGui.QTextCursor.NextCell)
    #     document.print_(printer)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())