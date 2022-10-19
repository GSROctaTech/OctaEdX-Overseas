from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_fileProcessing(object):
    def setupUi(self, fileProcessing):
        if not fileProcessing.objectName():
            fileProcessing.setObjectName(u"fileProcessing")
        fileProcessing.resize(921, 584)
        self.buttonBox = QDialogButtonBox(fileProcessing)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 540, 621, 32))
        self.buttonBox.setFocusPolicy(Qt.TabFocus)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.recordsTableView = QTableView(fileProcessing)
        self.recordsTableView.setObjectName(u"recordsTableView")
        self.recordsTableView.setGeometry(QRect(10, 240, 901, 291))
        self.recordsTableView.setDragDropMode(QAbstractItemView.DragDrop)
        self.recordsTableView.setAlternatingRowColors(True)
        self.recordsTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.recordsTableView.setSortingEnabled(True)
        self.rows2Fetch = QComboBox(fileProcessing)
        self.rows2Fetch.setObjectName(u"rows2Fetch")
        self.rows2Fetch.setGeometry(QRect(130, 120, 111, 22))
        self.lineEdit = QLineEdit(fileProcessing)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 30, 181, 21))
        self.listWidget = QListWidget(fileProcessing)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(320, 30, 256, 192))
        self.pushButton = QPushButton(fileProcessing)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 60, 75, 23))
        self.pushButton_2 = QPushButton(fileProcessing)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 90, 75, 23))
        self.columnView = QColumnView(fileProcessing)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setGeometry(QRect(650, 30, 256, 192))

        self.retranslateUi(fileProcessing)
        self.buttonBox.accepted.connect(fileProcessing.accept)
        self.buttonBox.rejected.connect(fileProcessing.reject)

        self.rows2Fetch.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(fileProcessing)
    # setupUi

    def retranslateUi(self, fileProcessing):
        fileProcessing.setWindowTitle(QCoreApplication.translate("fileProcessing", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("fileProcessing", u"Select File(s)", None))
        self.pushButton_2.setText(QCoreApplication.translate("fileProcessing", u"Load", None))
    # retranslateUi