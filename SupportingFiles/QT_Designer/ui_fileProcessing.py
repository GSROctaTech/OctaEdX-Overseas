# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileProcessinguoWyHV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_fileProcessing(object):
    def setupUi(self, fileProcessing):
        if not fileProcessing.objectName():
            fileProcessing.setObjectName(u"fileProcessing")
        fileProcessing.setWindowModality(Qt.ApplicationModal)
        fileProcessing.resize(944, 499)
        self.btnSelectFiles = QPushButton(fileProcessing)
        self.btnSelectFiles.setObjectName(u"btnSelectFiles")
        self.btnSelectFiles.setGeometry(QRect(20, 20, 901, 31))
        self.btnSelectFiles.setFlat(False)
        self.tableWidget = QTableWidget(fileProcessing)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font = QFont()
        font.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 901, 401))
        self.tableWidget.setMinimumSize(QSize(661, 0))
        self.tableWidget.setFrameShape(QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)

        self.retranslateUi(fileProcessing)

        QMetaObject.connectSlotsByName(fileProcessing)
    # setupUi

    def retranslateUi(self, fileProcessing):
        fileProcessing.setWindowTitle(QCoreApplication.translate("fileProcessing", u"Data File(s) Processing", None))
        self.btnSelectFiles.setText(QCoreApplication.translate("fileProcessing", u"Select File(s)", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("fileProcessing", u"File", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("fileProcessing", u"No. of Row(s)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("fileProcessing", u"Delimiter(s)", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("fileProcessing", u"File Analysis Summary", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("fileProcessing", u"Modify Specifications", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("fileProcessing", u"View Data", None));
    # retranslateUi

