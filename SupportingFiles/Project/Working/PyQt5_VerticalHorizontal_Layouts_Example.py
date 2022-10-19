import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        filestable = QTableWidget()
        filestable.setGeometry(50,50,600,300)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(filestable)  # Table Adding to 3 Row on Form/Window
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)


        filestableColumns = ('File Name & Location', 'Delimiters', 'No. of Rows', 'File Analysis Summary',
                             'Full Report', 'Modify Specs..', 'View Data')
        filestable.setColumnCount(len(filestableColumns))
        filestable.setHorizontalHeaderLabels(filestableColumns)
        filestable.setColumnCount(7)
        filestable.setRowCount(0)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(50, 50, 680, 450)

        self.setWindowTitle('Box layout example, QHBoxLayout, QVBoxLayout')
        self.show()

if __name__ == '__main__':
 app = QApplication(sys.argv)
 ex = Example()
 sys.exit(app.exec_())