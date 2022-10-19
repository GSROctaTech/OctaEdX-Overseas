import atexit
import sys
from PyQt5.QtGui import (QImage, QPainter, QIcon, QKeySequence, QTextCursor, QPalette,
                         QCursor, QDropEvent, QTextDocument, QTextTableFormat, QColor, QBrush, QMainWindow)

import os  # Libreria para manejar directorios del sistema operativo


def funcion(a):
    print("Hola mundo" + str(a))

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('c:/prueba gui/resource/logo.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        btn_brow_1 = QtGui.QPushButton('Browser...', self)
        btn_brow_1.resize(btn_brow_1.sizeHint())
        btn_brow_1.move(300, 50)
        btn_brow_1.clicked.connect(self.showDialog_points)

        btn_brow_2 = QtGui.QPushButton('Dir browser', self)
        btn_brow_2.resize(btn_brow_2.sizeHint())
        btn_brow_2.move(300, 80)
        btn_brow_2.clicked.connect(self.showDialog_indir_stl)

        btn_brow_3 = QtGui.QPushButton('Dir browser', self)
        btn_brow_3.resize(btn_brow_3.sizeHint())
        btn_brow_3.move(300, 110)
        btn_brow_3.clicked.connect(self.showDialog_outdir_stl)

        btn_brow_4 = QtGui.QPushButton('Crear soportes', self)
        btn_brow_4.setGeometry(20, 145, 250, 25)
        # btn_brow_4.clicked.connect(support.main(fname_points, self.fname_stl_indir, self.fname_stl_outdir))
        btn_brow_4.clicked.connect(funcion(12))  # HERE IS THE PROBLEM!

        self.le1 = QtGui.QLineEdit(self)
        self.le1.setGeometry(20, 50, 250, 21)

        self.le2 = QtGui.QLineEdit(self)
        self.le2.setGeometry(20, 80, 250, 21)

        self.le3 = QtGui.QLineEdit(self)
        self.le3.setGeometry(20, 110, 250, 21)

        self.statusBar().showMessage("Ready")

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Support from points generator')
        self.show()

    def showDialog_points(self):
        self.fname_points = QtGui.QFileDialog.getOpenFileName(self, 'Open points file', '/home')
        self.statusBar().showMessage(str(self.fname_points))
        self.le1.setText(str(self.fname_points))
        self.fname_points = str(self.le1.text())
        print(fname_points)

    def showDialog_indir_stl(self):
        self.fname_stl_indir = QtGui.QFileDialog.getExistingDirectory(self, 'Select STL INPUT directory', '/home')
        self.statusBar().showMessage(str(self.fname_stl_indir))
        self.le2.setText(str(self.fname_stl_indir))
        self.fname_stl_indir = str(self.le2.text())
        print(fname_stl_indir)

    def showDialog_outdir_stl(self):
        self.fname_stl_outdir = QtGui.QFileDialog.getExistingDirectory(self, 'Select STL OUTPUT directory', '/home')
        self.statusBar().showMessage(str(self.fname_stl_outdir))
        self.le3.setText(str(self.fname_stl_outdir))
        self.fname_stl_outdir = str(self.le3.text())
        print(fname_stl_outdir)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()