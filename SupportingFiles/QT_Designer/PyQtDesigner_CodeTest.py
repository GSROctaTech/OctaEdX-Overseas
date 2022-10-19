from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fileProcessing(object):
    def setupUi(self, fileProcessing):
        fileProcessing.setObjectName("fileProcessing")
        fileProcessing.setWindowModality(QtCore.Qt.ApplicationModal)
        fileProcessing.resize(944, 499)
        self.btnSelectFiles = QtWidgets.QPushButton(fileProcessing)
        self.btnSelectFiles.setGeometry(QtCore.QRect(20, 20, 901, 31))
        self.btnSelectFiles.setFlat(False)
        self.btnSelectFiles.setObjectName("btnSelectFiles")
        self.tableWidget = QtWidgets.QTableWidget(fileProcessing)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 901, 401))
        self.tableWidget.setMinimumSize(QtCore.QSize(661, 0))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)

        self.retranslateUi(fileProcessing)
        QtCore.QMetaObject.connectSlotsByName(fileProcessing)



    def retranslateUi(self, fileProcessing):
        _translate = QtCore.QCoreApplication.translate
        fileProcessing.setWindowTitle(_translate("fileProcessing", "Data File(s) Processing"))
        self.btnSelectFiles.setText(_translate("fileProcessing", "Select File(s)"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("fileProcessing", "File"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("fileProcessing", "No. of Row(s)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("fileProcessing", "Delimiter(s)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("fileProcessing", "File Analysis Summary"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("fileProcessing", "Modify Specifications"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("fileProcessing", "View Data"))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("1 - Ui_Form --> setupUi --> New Form")
        Form.resize(400, 300)
        self.openGLWidget = QtWidgets.QOpenGLWidget(Form)
        self.openGLWidget.setGeometry(QtCore.QRect(9, 9, 382, 282))
        self.openGLWidget.setObjectName("openGLWidget")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("New Form", "2 - Ui_Form --> retranslateUi --> New Form"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_fileProcessing()
    ui.setupUi(MainWindow)
    Form = QtWidgets.QWidget()
    f = Ui_Form()
    f.setupUi(Form)


    MainWindow.show()
    sys.exit(app.exec_())