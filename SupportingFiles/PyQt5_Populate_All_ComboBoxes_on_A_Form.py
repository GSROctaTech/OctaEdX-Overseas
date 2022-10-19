from sys import exit as sys_exit

from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QHBoxLayout, QComboBox, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setGeometry(150, 150, 200, 100)
        self.cmb_items = ['1', '2', '3', '4']

        self.cmb_box_1 = QComboBox()
        self.cmb_box_2 = QComboBox()

        HBox = QHBoxLayout()
        HBox.addWidget(self.cmb_box_1)
        HBox.addStretch(1)
        HBox.addWidget(self.cmb_box_2)

        self.cw = QWidget()
        self.cw.setLayout(HBox)

        self.setCentralWidget(self.cw)

        for widget in self.cw.children():
            if isinstance(widget, QComboBox):
                widget.addItems(self.cmb_items)

if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys_exit(app.exec_())