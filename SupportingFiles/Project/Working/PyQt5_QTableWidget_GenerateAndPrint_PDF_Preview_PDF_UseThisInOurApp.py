# https://stackoverflow.com/questions/53475944/printing-the-table-from-qtablewidget
# https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe?rq=1
# https://www.google.com/search?q=print+qtablewidget+content+into+pdf+pyqt5&rlz=1C1OKWM_enIN1004IN1004&oq=Print+QTableWidget+content+into+Pdf+pyqt&aqs=chrome.1.69i57j33i160l2.5016j0j4&sourceid=chrome&ie=UTF-8
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui

from PyQt5.QtWidgets import *

list_a =['word_a 1', 'word_a 2']
list_b =['word_b 1 ', 'word_b 2']
list_c =['word_c 1', 'word_c 2']
combo_box_options = ["Option 1","Option 2","Option 3"]
list_d = ['good','bad']
data = {'Wort A':list_a, 'Wort B':list_b, 'Wort C': list_c, 'Dropdown': [], 'Word D': list_d}


class Window(QTabWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super().__init__()
        self.setWindowTitle(self.tr('Document Printer'))
        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(5)

        horHeaders = []
        for col, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for row, item in enumerate(data[key]):
                newitem = QTableWidgetItem(item)
                newitem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row, col, newitem)


        combo_attr = ['bad word', 'good word', 'very nice word', 'delet']
        i = 0
        for j in horHeaders:
            comboBox = QtWidgets.QComboBox()
            for t in combo_attr:
                comboBox.addItem(t)
            self.table.setCellWidget(i,3,comboBox)
            i += 1


        self.table.setHorizontalHeaderLabels(
            'Word A|Word B|Word C|Dropdown|Word D'.split('|'))
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

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        table = cursor.insertTable(self.table.rowCount(), self.table.columnCount())

        for row in range(table.rows()):
            for col in range(table.columns()):
                w = self.table.cellWidget(row, col)
                it = self.table.item(row, col)
                if w is not None:
                    cursor.insertText(get_text_from_widget(w))
                elif it is not None:
                    cursor.insertText(it.text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)

def get_text_from_widget(w):
    t = ""
    if isinstance(w, QtWidgets.QComboBox):
        t = w.currentText()

    # if isinstance(w, another_widget):
    # t = w.some_method()

    return t

    # def handlePaintRequest(self, printer):
    #     document = QtGui.QTextDocument()
    #     cursor = QtGui.QTextCursor(document)
    #     table = cursor.insertTable(
    #         self.table.rowCount(), self.table.columnCount())
    #
    #     for row in range(table.rows()):
    #         print(row)
    #         for col in range(table.columns()):
    #             print(col)
    #             cursor.insertText(self.table.newitem(row, col).text())
    #             cursor.movePosition(QtGui.QTextCursor.NextCell)
    #     document.print_(printer)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())