import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 440, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 160, 591, 341))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 121, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 130, 81, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 500, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 110, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 50, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 111, 16))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(460, 70, 221, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 80, 111, 16))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.widget.close)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_2.clicked.connect(self.textBrowser.clear)
        self.pushButton.clicked.connect(self.gauss)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lay = QHBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.lay.addWidget(self.canvas)
        self.widget.setLayout(self.lay)
        self.widget.setFixedWidth(591)
        self.widget.setFixedHeight(341)

    def gauss(self):
        import numpy as np
        import sys
        import pandas as pd
        dataset = pd.read_csv(self.lineEdit_3.text())
        x = dataset.iloc[0:21].values
        y = dataset.iloc[22:43].values

        n = int(self.lineEdit_2.text())
        X = np.zeros(n)
        a = np.zeros((n, n))
        b = np.zeros(n)
        z = np.zeros(n + 2)
        z[0] = int(self.lineEdit.text())

        for j in range(1, n + 2):
            for i in range(1, 21):
                z[j] += np.power(float(x[i]), j)
            # print(z[j])

        for j in range(0, n):
            for r in range(n):
                a[r][j] = z[j + r]

        # for i in range(0,n):
        #    for j in range(0,n):
        # print(a[i][j])

        for i in range(n):
            if a[i][i] == 0.0:
                sys.exit('Divide by zero detected!')

            for j in range(i + 1, n):
                ratio = a[j][i] / a[i][i]
                b[j] = b[j] - ratio * b[i]

                for k in range(n):
                    a[j][k] = a[j][k] - ratio * a[i][k]

                    # for i in range(n):
        # for j in range(n):
        # print(a[i][j])

        # for i in range(n):
        # print(b[i])

        # Back Substitution
        X[n - 1] = b[n - 1] / a[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            Sum = 0

            for j in range(i, n):
                Sum = Sum + a[i][j] * X[j]

            X[i] = (b[i] - Sum) / a[i][i]

        self.textBrowser.setText(str(X))

        plt.grid()
        # x = np.linspace(0,1,n)
        # for i in matrix(x,y):
        #  plt.plot(i[0], i[1], 'b')

        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Polynomial Regression")
        # visualize data
        plt.plot(x, y, 'r')
        plt.axis('auto')
        plt.xlim((-0.05, 1.05))
        plt.ylim((-0.10, 0.10))
        self.figure.tight_layout()
        self.canvas.draw()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Polynomial Regression Method"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "Number of data, N :"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "Save file"))
        self.label_2.setText(_translate("MainWindow", "Number of unknown, m :"))
        self.label_4.setText(_translate("MainWindow", "Enter file name :"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())