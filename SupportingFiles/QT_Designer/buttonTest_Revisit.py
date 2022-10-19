import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    btnSelectFiles = QPushButton(widget)
    btnSelectFiles.setText("Select File(s)..")
    # btnSelectFiles.move(64, 32)
    btnSelectFiles.setGeometry(50, 150, 100, 30)
    btnSelectFiles.clicked.connect(uploadfiles)

    btnGenMetadata = QPushButton(widget)
    btnGenMetadata.setText("Execute Function")
    # btnGenMetadata.move(64, 64)
    btnGenMetadata.setGeometry(160, 150, 100, 30)
    btnGenMetadata.clicked.connect(generateMetadata)

    btnGenMetadata = QPushButton(widget)
    btnGenMetadata.setText("Execute Function")
    # btnGenMetadata.move(64, 64)
    btnGenMetadata.setGeometry(270, 150, 100, 30)
    btnGenMetadata.clicked.connect(selectFiles)

    widget.setGeometry(30, 50, 1300, 660)
    widget.setWindowTitle("Files Processing..")
    widget.show()
    sys.exit(app.exec_())


def selectFiles():
    try:
        fileTypes = "Text Files (*.txt);;CSV Files (*.csv);;Excel Files (*.xls);;Excel Files (*.xlsx);;JSON Files (*.json);;XML Files (.xml);; All Files (*.*)"

        logMessage("Log Message - From selectFiles")

        # fileNames, _ = QFileDialog.getOpenFileNames(widget, "Open CSV",
        #                                             'E:/GSReddy/PythonProjects/SampleData',
        #                                             # QDir.homePath() + "/Dokumente/CSV"
        #                                             fileTypes)

        # filter = "TXT (*.txt);;PDF (*.pdf)"
        # file_name = QtGui.QFileDialog()
        # file_name.setFileMode(QFileDialog.ExistingFiles)
        # names = file_name.getOpenFileNamesAndFilter(self, "Open files", "C\\Desktop", filter)
        # print(names)

    except:
        print("An error occurred")
    else:
        print("An error occurred")
    finally:
        # this block is always executed regardless of exception generation.
        print('finally executed')

    # print(fileNames)


def uploadfiles():
    try:

        # files = QtWidgets.QFileDialog.getOpenFileNames(QWidget,
        #                                                 "Select 7z or image files to open",
        #                                                 os.getcwd(),
        #                                                 "files (*.7z *.png *.bmp *.jpg)")[0]
        # self.files += files
        # files = [os.path.basename(f) for f in self.files[::-1]]
        # self.fileListSignal.emit(files)

        logMessage("Log Message - From uploadfiles - Try ")

    except:
        print("An error occurred in uploadfiles() - except")
    else:
        print("An error occurred - uploadfiles() - else")
    finally:
        # this block is always executed regardless of exception generation.
        print("finally executed in uploadfiles()")


def generateMetadata():
    '''
    dlg = CustomDialog()
    if dlg.exec():
        print("Success!")
    else:
        print("Cancel!")
    '''

    logMessage("Log Message - From generateMetadata")


def logMessage(logMsg):
    print(logMsg)


if __name__ == '__main__':
    window()

'''

Convert Above Program to Class based Program as below

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

'''
