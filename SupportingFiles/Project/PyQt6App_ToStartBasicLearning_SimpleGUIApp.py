from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.setGeometry(50,50,400,200)

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)
        button.setGeometry(70,50,60,30)

        self.setCentralWidget(button)
        self.show()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()