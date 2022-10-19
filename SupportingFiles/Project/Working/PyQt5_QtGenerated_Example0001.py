from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class RandomWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RandomWidget, self).__init__(parent)
        #self.layout = QtWidgets.QVBoxLayout()
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.ui()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.table2)
        self.layout.addWidget(self.selectFiles)
        self.layout.addWidget(self.selectFiles1)
        self.layout.addWidget(self.selectFiles2)
        self.layout.addWidget(self.selectFiles3)
        self.layout.addWidget(self.selectFiles4)

    def ui(self):
        self.table = QtWidgets.QTableView()
        #self.table.setMinimumSize(800, 200)
        self.table2 = QtWidgets.QTableView()

        self.selectFiles = QtWidgets.QPushButton("Select File(s)..")
        #self.selectFiles.setGeometry(50,50,90,30)
        self.selectFiles1 = QtWidgets.QPushButton("Get File(s)..")
        self.selectFiles2 = QtWidgets.QPushButton("Edit File(s)..")
        self.selectFiles3 = QtWidgets.QPushButton("View File(s)..")
        self.selectFiles4 = QtWidgets.QPushButton("Remove File(s)..")


class Mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        self.widget = None
        super(Mainwindow, self).__init__()
        self.setWindowTitle('test')

    def ui(self):
        self.setCentralWidget(self.widget)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = Mainwindow()
    Window.widget = RandomWidget(Window)
    Window.ui()
    sys.exit(app.exec_())