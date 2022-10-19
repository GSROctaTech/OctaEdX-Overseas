# !/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import os
from PyQt5.QtGui import QKeySequence, QIcon, QTextCursor, QCursor,QDropEvent, QTextDocument, QTextTableFormat, QColor
from PyQt5.QtCore import QFile, QSettings, Qt, QFileInfo, QDir, QMetaObject
from PyQt5.QtWidgets import (QAction, QLineEdit, QMessageBox,
                             QAbstractItemView, QTableWidget, QTableWidgetItem, QGridLayout,
                             QFileDialog, QMenu, QInputDialog)
from PyQt5 import QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from scipy import stats
from sklearn import model_selection
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from PyQt5 import QtCore, QtGui, QtWidgets


class TableWidgetDragRows(QTableWidget):  # 설정
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 실햄 폼의 자동설정
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setDragDropMode(QAbstractItemView.InternalMove)

    def dropEvent(self, event: QDropEvent):  # drop 이벤트 설정 , 크롤 설정
        if not event.isAccepted() and event.source() == self:
            drop_row = self.drop_on(event)
            rows = sorted(set(item.row() for item in self.selectedItems()))
            rows_to_move = [[QTableWidgetItem(self.item(row_index, column_index)) for column_index in range(self.columnCount())]
            for row_index in rows]
            for row_index in reversed(rows): self.removeRow(row_index)
            if row_index < drop_row:
                    drop_row -= 1

            for row_index, data in enumerate(rows_to_move):
                row_index += drop_row
                self.insertRow(row_index)

            for column_index, column_data in enumerate(data):
                self.setItem(row_index, column_index, column_data)
                event.accept()

            for row_index in range(len(rows_to_move)):
                self.item(drop_row + row_index, 0).setSelected(True)
                self.item(drop_row + row_index, 1).setSelected(True)
                super().dropEvent(event)


    # 스크롤 설정
    def drop_on(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return self.rowCount()
            return index.row() + 1
            if self.is_below(event.pos(), index):
                print(' - ')   # Added by G.S.Reddy
            else:
                index.row()

    def is_below(self, pos, index):
        rect = self.visualRect(index)
        margin = 2
        if pos.y() - rect.top() < margin:
            return False
        elif rect.bottom() - pos.y() < margin:
            return True
        # noinspection PyTypeChecker
        return rect.contains(pos, True)
                # below commented by G.S.Reddy
               # and not (int(self.model().flags(index)) & Qt.ItemIsDropEnabled) and pos.y() >= rect.center().y()

class MyWindow(QMainWindow):  # 폼을 실제 디스플레이 해주는 설정들
    def __init__(self, aPath, parent=None):
        super(MyWindow, self).__init__(parent)
        # QIcon.setThemeName('gnome')
        QMetaObject.connectSlotsByName(self)
        self.delimit = '\t'
        self.mycolumn = 0
        self.MaxRecentFiles = 5
        self.windowList = []
        self.recentFileActs = []
        self.settings = QSettings('Axel Schneider', 'CSVEditor')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isChanged = False
        self.fileName = ""
        self.fname = "Liste"
        self.mytext = ""
        self.colored = False
        self.copiedRow = []
        self.copiedColumn = []
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 121, 41))
        self.textBrowser.setStyleSheet("background-color: rgb(8, 143,255);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\"\n"
                                            "http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><metaname=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space:pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400;font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-size:16pt; font-weight:600;color:#ffffff;\">AR-ANN</span></p></body></html>"))

        self.textBrowser_2 = QtWidgets.QTextBrowser(self)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 0, 611, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(43, 41,41);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setHtml(_translate("MWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\"\n"
                                              "http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><metaname=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space:pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400;font-style:normal;\">\n"
                                              "<p style=\"margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;font-weight:600; color:#ffffff;\"> Well level</span><span style=\" font-size:10pt; font-weight:600;color:#ffffff;\">V1.0</span></p></body></html>"))

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 40, 611,461))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        # 불러오기 버튼 pushload
        self.pushload = QtWidgets.QPushButton(self.page)
        self.pushload.setGeometry(QtCore.QRect(0, 0, 81, 31))
        self.pushload.setStyleSheet("background-color: rgb(8, 143,255);")
        self.pushload.setObjectName("pushButton")
        self.pushload.setText(_translate("MainWindow", "불러오기"))
        self.pushload.clicked.connect(self.loadCsv)
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 0, 31, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 350, 71, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(8, 143,255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setWhatsThis(_translate("MainWindow","<html><head/><body><p> 완료<br/></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "전체 선택"))
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 420, 71, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(8, 143,255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setWhatsThis(_translate("MainWindow","<html><head/><body><p>선택 완료<br/></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "선택 완료"))
        self.tableView = QtWidgets.QTableView(self.page)
        self.tableView.setGeometry(QtCore.QRect(0, 30, 541, 431))
        self.tableView.setStyleSheet("background-color: rgb(255, 255,255);")
        self.tableView.setObjectName("tableView")
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.textEdit = QtWidgets.QTextEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(80, 0, 461, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255,255);")
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 200, 31, 31))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 260, 31, 31))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.tableView_2 = QtWidgets.QTableView(self.page_2)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 281, 461))
        self.tableView_2.setStyleSheet("background-color: rgb(255, 255,255);")
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_3 = QtWidgets.QTableView(self.page_2)
        self.tableView_3.setGeometry(QtCore.QRect(330, 0, 281, 461))
        self.tableView_3.setStyleSheet("background-color: rgb(255, 255,255);")
        self.tableView_3.setObjectName("tableView_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(290, 0, 321, 461))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255,255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\"\n"
                                              "http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name =\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space:pre-wrap;}\n"
                                              "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt;font-weight: 400;font-style:normal;\">\n"
                                              "<p align=\"justify\"style =\" margin-top:0px; margin-bottom:0px; margin-left:0px;margin-right:0px;-qt-block-indent:0;text-indent:0px;\"><span style=\"font-weight:600;\">MLPRegressor 조건 설정</span></p>\n"
                                              "<p align=\"justify\" style =\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px;margin-left:0px;margin-right:0px;-qt-block-indent:0;text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_12 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_12.setGeometry(QtCore.QRect(480, 30, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setText(_translate("MainWindow","PushButton"))
        self.tableView_4 = QtWidgets.QTableView(self.page_3)
        self.tableView_4.setGeometry(QtCore.QRect(0, 0, 281, 461))
        self.tableView_4.setStyleSheet("background-color: rgb(255, 255,255);")
        self.tableView_4.setObjectName("tableView_4")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 40, 121, 461))
        self.textBrowser_4.setStyleSheet("background-color: rgb(43, 41,41);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 80, 121, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(8, 143,255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText(_translate("MainWindow", " 파 일 선택"))
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 150, 121, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(43, 41,41);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText(_translate("MainWindow", "변환"))
        self.pushButton_10 = QtWidgets.QPushButton(self)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 220, 121, 31))
        self.pushButton_10.setStyleSheet("background-color: rgb(43, 41,41);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setText(_translate("MainWindow", " 조건 설정"))
        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 290, 121, 31))
        self.pushButton_7.setStyleSheet("background-color: rgb(43, 41,41);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText(_translate("MainWindow", " ANN 모델링"))
        self.pushButton_9 = QtWidgets.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 360, 121, 31))
        self.pushButton_9.setStyleSheet("background-color: rgb(43, 41,41);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setText(_translate("MainWindow", " 최적 모델 확인"))
        self.pushButton_11 = QtWidgets.QPushButton(self)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 430, 121, 31))
        self.pushButton_11.setStyleSheet("background-color: rgb(43, 41,41);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setText(_translate("MainWindow", " 예측 적용 "))
        self.isChanged = False
        self.readSettings()
        if len(sys.argv) > 1:
            self.fileName = sys.argv[1]
            self.loadCsvOnOpen(self.fileName)
            self.msg(self.fileName + "loaded")
        else:
            self.msg("Ready")
            self.isChanged = False
            # 예측하기 버튼 누를시 - 실제 계산 부분


    def conten(self):
        # 텍스트로 받은 숫자를 정수로 변환
        num = self.textedit1.toPlainText()
        s = num
        n = float(s)
        for i in range(0, 1000):  # i의 변수 선언 0으로 시작하여 100회를 수행
            # 학슴용 데이터와 검증용 데이터를 분리한다.
            x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size=0.33)
            # 분리한 데이터를 표준화 변환
            x_train1 = (x_train - x_train.mean()) / x_train.std()
            x_test1 = (x_test - x_test.mean()) / x_test.std()
            # estimator가 많으면 많은 변수 활용, random_state가 일정해 야 결과도 동일하게 추출됨
            # 글로벌 변수 추가

            global estimator
            estimator = RandomForestRegressor(n_estimators=100,  criterion='mse', max_depth=None, min_samples_split=2,
                                    min_samples_leaf = 1,min_weight_fraction_leaf = 0.0, max_features = 'auto',
                                    max_leaf_nodes = None, min_impurity_decrease = 0.0, min_impurity_split = None,
                                    bootstrap = True,oob_score = False, n_jobs = 1, random_state = None, verbose = 0,
                                    warm_start = False)
            estimator.fit(x_train1, y_train.values.ravel())
            # 예측 계산 대입
            y_predict = estimator.predict(x_train1)
            score0 = metrics.r2_score(y_train, y_predict)
            mse1 = mean_squared_error(y_train, y_predict)
            y_predict = estimator.predict(x_test1)
            score1 = metrics.r2_score(y_test, y_predict)
            mse2 = mean_squared_error(y_test, y_predict)
            # 입력받은 검출 n 이상이 되면 break
            if score0 > n:
                # 문자열 변환 및 출력 첫단은 setText 추가는 append
                p1 = y_test
                p2 = str(p1)
                y1 = x_test
                y2 = str(y1)
                self.textedit2.append(' 선택된 y_test 데이터 \n' + p2)
                self.textedit2.append('')
                self.textedit2.append(' 선택된 w_data 데이터 \n' + y2)
                v1 = y_predict
                v2 = str(v1)
                self.textedit2.append('')
                self.textedit2.append('y-predict : ' + v2)
                self.textedit2.append('')
                a1 = score0
                a2 = str(a1)
                self.textedit2.append('train R2 : ' + a2)
                a3 = mse1
                a4 = str(a3)
                self.textedit2.append('train mse : ' + a4)
                c1 = score1
                c2 = str(c1)
                self.textedit2.append('')
                self.textedit2.append('test R2: ' + c2)
                c3 = mse2
                c4 = str(c3)
                self.textedit2.append('test mse: ' + c4)
                break


    # 적용할 파일 불러오기 버튼 클릭시
    def loadta(self):
        # 파일이 열려있는지 확인
        if self.isChanged == True:
            quit_msg = "<b>The Document was changed.<br>Do you want to save changes? < / b > "
            reply = QMessageBox.question(self, 'Save Confirmation',
                                         quit_msg, QMessageBox.Yes,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.saveOnQuit()
                # csv 파일만 불러오기 창에 표시
                fileName1, _ = QFileDialog.getOpenFileName(self, "Open CSV",
                                                           (QDir.homePath() +
                                                            "/Dokumente/CSV"), "CSV (*.csv *.tsv *.txt)")
                self.textedit3.setText(fileName1)  # 파일 네임 출력
                if fileName1:
                    self.loadCsvOnOpen(fileName1)
                    x_dat = pd.read_csv(fileName1, names=['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8'])
                    # 학슴용 데이터와 검증용 데이터를 분리한다.
                    x_train, x_test, = model_selection.train_test_split(x_dat,test_size=0.33)
                    # 분리한 데이터를 정규화 시킨다.
                    x_dat_scaled = (x_test - x_test.mean()) / x_test.std()
                    # 예측 데이터 적용
                    y_pre = estimator.predict(x_test)
                    # 정수를 문자열로 변환
                    s1 = x_test
                    s2 = str(s1)
                    s3 = x_dat_scaled
                    s4 = str(s3)
                    s5 = y_pre
                    s6 = str(s5)
                    # 출력 첫단은 setText 추가는 append
                    self.textedit4.setText(s2)
                    self.textedit4.append('')
                    self.textedit4.append(s4)
                    self.textedit4.append('')
                    self.textedit4.append(s6)

    # tableview 변경
    def changeSelection(self):
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)

    # tableview 검색 데이터 호출
    def updateCell(self):
        if self.tableView.selectionModel().hasSelection():
            row = self.selectedRow()
            column = self.selectedColumn()
            newtext = QTableWidgetItem(self.editLine.text())
            self.tableView.setItem(row, column, newtext)

    # tableview의 선택된 정보를 가져온다.
    def getItem(self):
        item = self.tableView.selectedItems()[0]
        row = self.selectedRow()
        column = self.selectedColumn()
        if not item == None:
            name = item.text()
        else:
            name = ""
            self.msg("'" + name + "' on Row " + str(row + 1) + " Column " + str(column + 1))
            self.editLine.setText(name)

    # tableview 선택된 행
    def selectedRow(self):
        if self.tableView.selectionModel().hasSelection():
            row =self.tableView.selectionModel().selectedIndexes()[0].row()
            return int(row)

    # tableview 선택된 열
    def selectedColumn(self):
        column = self.tableView.selectionModel().selectedIndexes()[0].column()
        return int(column)

    # 찾는 숫자 입력받음
    def findText(self):
        self.findTableItems()
        self.changeSelection()

    # tableview의 찾는 숫자를 찾는다.
    def findTableItems(self):
        #
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        findText = self.findBar.text()
        self.tableView.clearSelection()
        # if findText.isnumeric():
        # items = self.tableView.findItems(findText,Qt.MatchExactly)
        # else:
        items = self.tableView.findItems(findText, Qt.MatchContains)
        if items:
            self.colored = True
        self.makeAllWhite()
        for item in items:
            item.setBackground(Qt.yellow)
        self.colored = True
        self.isChanged = False
        # 찾은 데이터를 표시

    def findThis(self):
        #
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableView.clearSelection()
        items = self.tableView.findItems(self.mytext, Qt.MatchContains)
        if items:
            self.colored = True
            self.makeAllWhite()
            for item in items:
                item.setBackground(Qt.yellow)
                item.setForeground(Qt.blue)
                self.colored = True
                self.isChanged = False

    def msgbox(self, message):
        QMessageBox.warning(self, "Message", message)

    # 메뉴바
    def createMenuBar(self):
        # File 메뉴바
        bar = self.menuBar()
        self.filemenu = bar.addMenu("File")
        self.separatorAct = self.filemenu.addSeparator()
        self.filemenu.addAction(QIcon.fromTheme("document-open"), "Open", self.loadCsv, QKeySequence.Open)
        self.filemenu.addAction(QIcon.fromTheme("document-save"), "Save", self.saveOnQuit, QKeySequence.Save)
        self.filemenu.addSeparator()
        self.filemenu.addAction(QIcon.fromTheme("document-print-preview"), "Print Preview ", self.handlePreview, " Shift + Ctrl + P")
        self.filemenu.addSeparator()
        for i in range(self.MaxRecentFiles):
            self.filemenu.addAction(self.recentFileActs[i])
            self.updateRecentFileActions()
            self.filemenu.addSeparator()
            self.clearRecentAct = QAction("clear Recent Files List", self, triggered=self.clearRecentFiles)
            self.clearRecentAct.setIcon(QIcon.fromTheme("edit-clear"))
            self.filemenu.addAction(self.clearRecentAct)
            self.filemenu.addSeparator()
            self.filemenu.addAction(QIcon.fromTheme("application-exit"), "Exit", self.handleQuit, QKeySequence.Quit)
            # Edit
            self.editmenu = bar.addMenu("Edit")
            self.editmenu.addAction(QIcon.fromTheme("edit-copy"), "copy Cell", self.copyByContext, QKeySequence.Copy)
            self.editmenu.addAction(QIcon.fromTheme("edit-paste"), "paste Cell", self.pasteByContext, QKeySequence.Paste)
            self.editmenu.addAction(QIcon.fromTheme("edit-cut"), "cut Cell", self.cutByContext, QKeySequence.Cut)
            self.editmenu.addAction(QIcon.fromTheme("edit-delete"), "delete Cell", self.deleteCell, QKeySequence.Delete)
            self.editmenu.addSeparator()
            self.editmenu.addAction(QIcon.fromTheme("edit-copy"), "copy Row", self.copyRow)
            self.editmenu.addAction(QIcon.fromTheme("edit-paste"), "paste Row", self.pasteRow)
            self.editmenu.addSeparator()
            self.editmenu.addAction(QIcon.fromTheme("edit-copy"), "copy Column", self.copyColumn)
            self.editmenu.addAction(QIcon.fromTheme("edit-paste"), "paste Column", self.pasteColumn)
            self.editmenu.addSeparator()
            self.editmenu.addAction(QIcon.fromTheme("add"), "add Column", self.addColumn)
            self.editmenu.addAction(QIcon.fromTheme("edit-delete"), "remove Column", self.removeColumn)
            self.editmenu.addSeparator()
            self.editmenu.addAction(QIcon.fromTheme("edit"), "headers add",self.setHeadersToFirstRow)
            self.editmenu.addSeparator()
            self.editmenu.addAction(QIcon.fromTheme("edit-clear"), "clear List", self.clearList)
            self.editmenu.addSeparator()
            self.editmenu.addAction(QIcon.fromTheme("pane-show-symbolic"), "toggle horizontal Headers ", self.toggleHorizHeaders)
            self.editmenu.addAction(QIcon.fromTheme("pane-hide-symbolic"), "toggle vertical Headers", self.toggleVertHeaders)
            self.editmenu.addAction(self.whiteAction)
            # tableview row, col의 데이터 호출

    def deleteCell(self):
        row = self.selectedRow()
        col = self.selectedColumn()
        self.tableView.takeItem(row, col)

    def toggleHorizHeaders(self):
        if self.tableView.horizontalHeader().isVisible():
            self.tableView.horizontalHeader().setVisible(False)
        else:
            self.tableView.horizontalHeader().setVisible(True)

    def toggleVertHeaders(self):
        if self.tableView.verticalHeader().isVisible():
            self.tableView.verticalHeader().setVisible(False)
        else:
            self.tableView.verticalHeader().setVisible(True)

    # 메뉴바 셋팅
    def createActions(self):
        # all items white BG
        self.whiteAction = QAction(QIcon.fromTheme("pane-hide-symbolic"), "all items white background", self)
        self.whiteAction.triggered.connect(lambda: self.makeAllWhite())
        for i in range(self.MaxRecentFiles):
            self.recentFileActs.append(QAction(self, visible=False, triggered=self.openRecentFile))
                        # 새로 오픈할때 저장 할것인지 묻는 메세지 박스

    def openRecentFile(self):
        action = self.sender()
        if action:
            if self.isChanged == True:
                quit_msg = "<b>The Document was changed.<br>Do you want to save changes? </b>"
                reply = QMessageBox.question(self, 'Save Confirmation',quit_msg,QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.saveOnQuit()
                    file = action.data()
                if QFile.exists(file):
                    self.loadCsvOnOpen(file)
                else:
                    self.msg("File not exists")

    # 종료
    def handleQuit(self):
        quit()

    # csv 파일의 내용을 정렬 및 출력
    def loadCsvOnOpen(self, fileName):
        if fileName:
            f = open(fileName, 'r', encoding='utf-8')
            mystring = f.read()
            # csv 파일 특성상 ,를 구분하여 데이터를 재정렬
            if mystring.count(",") > mystring.count('\t'):
                if mystring.count(",") > mystring.count(';'):
                    self.delimit = ","
                elif mystring.count(";") > mystring.count(','):
                    self.delimit = ";"
                else:
                    self.delimit = "\t"
            elif mystring.count(";") > mystring.count('\t'):
                self.delimit = ';'
            else:
                self.delimit = "\t"
            f.close()
            f = open(fileName, 'r', encoding='utf-8')  # r = 읽기 설정 utf - 8 출력 설정
            self.tableView.setRowCount(0)
            self.tableView.setColumnCount(0)
            for rowdata in csv.reader(f, delimiter=self.delimit):
                row = self.tableView.rowCount()
            self.tableView.insertRow(row)
            if len(rowdata) == 0:
                self.tableView.setColumnCount(len(rowdata) + 1)
            else:
                self.tableView.setColumnCount(len(rowdata))
            for column, data in enumerate(rowdata):
                item = QTableWidgetItem(data)
                self.tableView.setItem(row, column, item)
                self.tableView.selectRow(0)
                self.isChanged = False
                self.setCurrentFile(fileName)
                self.tableView.resizeColumnsToContents()
                self.tableView.resizeRowsToContents()
                self.msg(fileName + " loaded")

    # csv 불러오기
    def loadCsv(self):

        # 기존에 파일이 열려있는지 확인
        if self.isChanged == True:
            quit_msg = "<b>The Document was changed.<br>Do you want to save changes? </b> "
            reply = QMessageBox.question(self, 'Save Confirmation', quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.saveOnQuit()

            # csv 파일만 불러오기 창에 표시
            fileName, _ = QFileDialog.getOpenFileName(self, "Open CSV",
                                                      (QDir.homePath() +
                                                       "/Dokumente/CSV"), "CSV (*.csv *.tsv *.txt)")
            self.textedit.setText(fileName)  # 파일 네임 출력
            if fileName:
                self.loadCsvOnOpen(fileName)
                datarows = fileName.count
                print(datarows)

                # 가져온 데이터에 헤더를 추가
                data = pd.read_csv(fileName, names=['w1', 'w2', 'w3', 'w4',
                                                    'w5', 'w6', 'w7', 'w8', 'y'])
                # 코드 전체 변수 설정
                global x_data, y_data
                # 파일의 행의 w1, w2, w3, w4, w5, w6, w7, w8를 x_data로 설 정
                x_data = data[["w1", "w2", "w3", "w4", "w5", "w6", "w7", "w8"]]
                y_data = data[["y"]]  # y행을 y_data로 설정


    # csv 파일 저장
    def writeCsv(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save File',
                                              QDir.homePath() + "/export.csv",
                                              "CSV Files(*.csv *.txt)")
        if path:
            with open(path, 'w') as stream:
                writer = csv.writer(stream, delimiter=self.delimit)
                for row in range(self.tableView.rowCount()):
                    for column in range(self.tableView.columnCount()):
                        item = self.tableView.item(row, column)
                        if item is not None:
                            rowdata.append(item.text())
                        else:
                            rowdata.append('')
                            writer.writerow(rowdata)
                            self.isChanged = False
                            self.setCurrentFile(path)


    # 출력 미리보기 기능 - 출력기능 포함
    def handlePreview(self):
        if self.tableView.rowCount() == 0:
            self.msg("no rows")
        else:
            dialog = QtPrintSupport.QPrintPreviewDialog()
            dialog.setFixedSize(1000, 700)
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec_()
            self.msg("Print Preview closed")

    # 출력 의뢰 - 출력기능 호출
    def handlePaintRequest(self, printer):
        printer.setDocName(self.fname)
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.tableView.model()
        tableFormat = QTextTableFormat()
        tableFormat.setBorder(0.2)
        tableFormat.setBorderStyle(3)
        tableFormat.setCellSpacing(0);
        tableFormat.setTopMargin(0);
        tableFormat.setCellPadding(4)
        table = cursor.insertTable(model.rowCount() + 1, model.columnCount(), tableFormat)
        model = self.tableView.model()

        ### get headers
        myheaders = []
        for i in range(0, model.columnCount()):
            myheader = model.headerData(i, Qt.Horizontal)
            cursor.insertText(str(myheader))
            cursor.movePosition(QTextCursor.NextCell)

            ### get cells
            for row in range(0, model.rowCount()):
                for col in range(0, model.columnCount()):
                    index = model.index(row, col)
                    cursor.insertText(str(index.data()))
                    cursor.movePosition(QTextCursor.NextCell)
                    document.print_(printer)

    # load 데이터 리스트를 제거
    def clearList(self):
        self.tableView.clear()
        self.isChanged = True

    # 백그라운드 하얀색
    def makeAllWhite(self):
        if self.colored == True:
            for row in range(self.tableView.rowCount()):
                for column in range(self.tableView.columnCount()):
                    item = self.tableView.item(row, column)
                    if item is not None:
                        item.setForeground(Qt.black)
                    item.setBackground(QColor("#fbfbfb"))
                    self.colored = False

    def finishedEdit(self):
        self.isChanged = True

# 메뉴바 이벤트
def contextMenuEvent(self, event):
    self.menu = QMenu(self)
    if self.tableView.selectionModel().hasSelection():
        # copy
        copyAction = QAction(QIcon.fromTheme("edit-copy"), 'Copy Cell', self)
        copyAction.triggered.connect(lambda: self.copyByContext())

        # paste
        pasteAction = QAction(QIcon.fromTheme("edit-paste"), 'Paste Cell', self)
        pasteAction.triggered.connect(lambda: self.pasteByContext())

        # cut
        cutAction = QAction(QIcon.fromTheme("edit-cut"), 'Cut Cell', self)
        cutAction.triggered.connect(lambda: self.cutByContext())

        # delete selected Row
        removeAction = QAction(QIcon.fromTheme("edit-delete"),'delete Row', self)
        removeAction.triggered.connect(lambda: self.deleteRowByContext(event)

        # replace all
        row = self.selectedRow()
        col = self.selectedColumn()
        myitem = self.tableView.item(row, col)

        if myitem is not None:
            self.mytext = myitem.text()
            replaceThisAction = QAction(QIcon.fromTheme("edit-find-and-replace"), "replace all occurrences of '" + self.mytext + "'", self)
            replaceThisAction.triggered.connect(lambda: self.replaceThis())

            # find all
            findThisAction = QAction(QIcon.fromTheme("edit-find"), "find all rows contains'" + self.mytext + "'", self)
            findThisAction.triggered.connect(lambda: self.findThis())
            ###
            self.menu.addAction(copyAction)
            self.menu.addAction(pasteAction)
            self.menu.addAction(cutAction)
            self.menu.addSeparator()
            self.menu.addAction(QIcon.fromTheme("edit-delete"),"delete", self.deleteCell, QKeySequence.Delete)
            self.menu.addSeparator()
            self.menu.addAction(QIcon.fromTheme("edit-copy"), "copy Row", self.copyRow)
            self.menu.addAction(QIcon.fromTheme("edit-paste"), "paste Row", self.pasteRow)
            self.menu.addSeparator()
            self.menu.addAction(QIcon.fromTheme("edit-copy"), "copy Column", self.copyColumn)
            self.menu.addAction(QIcon.fromTheme("edit-paste"), "paste Column", self.pasteColumn)
            self.menu.addSeparator()
            self.menu.addAction(addAction)
            self.menu.addAction(addAction2)
            self.menu.addSeparator()
            self.menu.addAction(addColumnBeforeAction)
            self.menu.addAction(addColumnAfterAction)
            self.menu.addSeparator()
            self.menu.addAction(removeAction)
            self.menu.addAction(deleteColumnAction)
            self.menu.addSeparator()
            self.menu.addAction(replaceThisAction)
            self.menu.addAction(findThisAction)
            self.menu.addSeparator()
            self.menu.addAction(self.whiteAction)
            self.menu.popup(QCursor.pos())

            # 값으로 교체
    def replaceThis(self):
        row = self.selectedRow()
        col = self.selectedColumn()
        myitem = self.tableView.item(row, col)
        if myitem is not None:
            mytext = myitem.text()
            dlg = QInputDialog()
            newtext, ok = dlg.getText(self, "Replace all", "replace all<b> " + mytext + " </b> with: ", QLineEdit.Normal, "", Qt.Dialog)
            if ok:
                items = self.tableView.findItems(mytext, Qt.MatchExactly)
                if items:
                    for item in items:
                        newItem = QTableWidgetItem(newtext)
                        self.tableView.setItem(item.row(), item.column(),newItem)

    # 선택된 데이터 복사하기
    def copyByContext(self):
        row = self.selectedRow()
        col = self.selectedColumn()
        myitem = self.tableView.item(row, col)
        if myitem is not None:
            clip = QApplication.clipboard()
            clip.setText(myitem.text())

    # 선택된 데이터 붙여넣기
    def pasteByContext(self):
        row = self.selectedRow()
        col = self.selectedColumn()
        clip = QApplication.clipboard()
        newItem = QTableWidgetItem(clip.text())
        self.tableView.setItem(row, col, newItem)
        self.tableView.resizeColumnsToContents()
        self.isChanged = True


    # 선택된 데이터 잘라내기
    def cutByContext(self):
        row = self.selectedRow()
        col = self.selectedColumn()
        myitem = self.tableView.item(row, col)
        if myitem is not None:
            clip = QApplication.clipboard()
            clip.setText(myitem.text())
            newItem = QTableWidgetItem("")
            self.tableView.setItem(row, col, newItem)
            self.isChanged = True

    # 닫기 이벤트 메세지박스 출력
    def closeEvent(self, event):
        if self.isChanged == True:
            quit_msg = "<b>The document was changed.<br>Do you want to save the changes? < / b > "
            reply = QMessageBox.question(self, 'Save Confirmation', quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                self.saveOnQuit()
                self.saveSettings()

    # load 셋팅
    def readSettings(self):
        if self.settings.contains("geometry"):
            self.setGeometry(self.settings.value('geometry'))
        if self.settings.contains("horHeader"):
            if self.settings.value('horHeader') == "true":
                self.tableView.horizontalHeader().setVisible(True)
            else:
                self.tableView.horizontalHeader().setVisible(False)
        if self.settings.contains("vertHeader"):
            if self.settings.value('vertHeader') == "true":
                self.tableView.verticalHeader().setVisible(True)
            else:
                self.tableView.verticalHeader().setVisible(False)

    # save 셋팅
    def saveSettings(self):
        self.settings.setValue('geometry', self.geometry())
        self.settings.setValue('horHeader',self.tableView.horizontalHeader().isVisible())
        self.settings.setValue('vertHeader',self.tableView.verticalHeader().isVisible())

    # 빠져나갈떄 저장
    def saveOnQuit(self):
        if self.fileName == "":
            self.writeCsv()
        else:
            path = self.fileName
            with open(path, 'w') as stream:
                writer = csv.writer(stream, delimiter=self.delimit)
                for row in range(self.tableView.rowCount()):
                    rowdata = []
                for column in range(self.tableView.columnCount()):
                    item = self.tableView.item(row, column)
                if item is not None:
                    rowdata.append(item.text())
                else:
                    rowdata.append('')
                writer.writerow(rowdata)
                self.isChanged = False

    # 현재 파일
    def setCurrentFile(self, fileName):
        self.fileName = fileName
        self.fname = os.path.splitext(str(fileName))[0].split("/")[-1]
        if self.fileName:
            self.setWindowTitle(self.strippedName(self.fileName) + "[*]")
        else:
            self.setWindowTitle("no File")
        files = self.settings.value('recentFileList', [])
        try:
            files.remove(fileName)
        except ValueError:
            pass
        files.insert(0, fileName)
        del files[self.MaxRecentFiles:]
        self.settings.setValue('recentFileList', files)
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, MyWindow):
                widget.updateRecentFileActions()

    # 최근 오픈된 파일 목록
    def updateRecentFileActions(self):
        files = self.settings.value('recentFileList', [])
        numRecentFiles = min(len(files), self.MaxRecentFiles)
        for i in range(numRecentFiles):
            text = "&%d %s" % (i + 1, self.strippedName(files[i]))
            self.recentFileActs[i].setText(text)
            self.recentFileActs[i].setData(files[i])
            self.recentFileActs[i].setVisible(True)
            self.recentFileActs[i].setIcon(QIcon.fromTheme("gnome-mime-text-x"))
            for j in range(numRecentFiles, self.MaxRecentFiles):
                self.recentFileActs[j].setVisible(False)
                self.separatorAct.setVisible((numRecentFiles > 0))

    # 파일 리스트 지움
    def clearRecentFiles(self, fileName):
        # self.settings.clear()
        mf = []
        self.settings.setValue('recentFileList', mf)
        self.updateRecentFileActions()

    # 파일 네임 셋팅
    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()

    # 메세지 박스
    def msg(self, message):
        self.statusBar().showMessage(message)

    # 헤더 추가
    def setHeadersToFirstRow(self):
        self.tableView.insertRow(0)
        for column in range(self.tableView.columnCount()):
            newItem = QTableWidgetItem(self.tableView.horizontalHeaderItem(column))
            ind = QTableWidgetItem(str(column + 1))
            self.tableView.setHorizontalHeaderItem(column, ind)
            self.tableView.setItem(0, column, newItem)

    # 열 삭제
    def removeColumn(self):
        self.tableView.removeColumn(self.selectedColumn())
        self.isChanged = True

    # 열 추가
    def addColumn(self):
        count = self.tableView.columnCount()
        self.tableView.setColumnCount(count + 1)
        self.tableView.resizeColumnsToContents()
        self.isChanged = True
        if self.tableView.rowCount() == 0:
            self.addRow()
            self.tableView.selectRow(0)

    # tableView 선택 행 데이터 복사
    def copyRow(self):
        row = self.selectedRow()
        for column in range(self.tableView.columnCount()):
            if not self.tableView.item(row, column) == None:
                self.copiedRow.append(self.tableView.item(row, column).text())

    # tableView 선택 행 데이터 복사
    def pasteRow(self):
        row = self.selectedRow()
        for column in range(self.tableView.columnCount()):
            newItem = QTableWidgetItem(self.copiedRow[column])
            self.tableView.setItem(row, column, newItem)

    # tableView 선택 열 데이터 복사
    def copyColumn(self):
        column = self.selectedColumn()
        for row in range(self.tableView.rowCount()):
            self.copiedColumn.append(self.tableView.item(row, column).text())

    # tableView 선택 열 데이터 붙여넣기
    def pasteColumn(self):
        column = self.selectedColumn()
        for row in range(self.tableView.rowCount()):
            newItem = QTableWidgetItem(self.copiedColumn[row])
            self.tableView.setItem(row, column, newItem)
            self.tableView.resizeColumnsToContents()
    # 스타일 시트 설정
    def stylesheet(self):
        return """
            QTableWidget
            {
            border: 0.5px solid lightgrey;
            border-radius: 0px;
            font-family: Noto Sans;
            font-size: 9pt;
            background-color: #fbfbfb;
            selection-color: #ffffff
            }
            QTableWidget::item:hover
            {
            color: black;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0
            #cfbb72, stop:1 #d3d7cf);
            }
            QTableWidget::item:selected
            {
            color: #F4F4F4;
            background: qlineargradient(x1:0, y1:0, x1:2, y1:2, stop:0
            #bfc3fb, stop:1 #324864);
            }
            QStatusBar
            {
            font-size: 7pt;
            color: #717171
            }
            QLineEdit
            {
            color: #484848;
            background-color: #fbfbfb;
            }
            """
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')
    main = MyWindow('')
    main.resize(734, 543)
    main.setStyleSheet("background-color: rgb(225, 238, 242);")
    main.setWindowTitle("CSV Viewer")
    main.show()
    sys.exit(app.exec_())
