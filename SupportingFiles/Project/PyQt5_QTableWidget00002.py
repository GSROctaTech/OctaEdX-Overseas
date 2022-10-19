# Import necessary libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDesktopWidget
from PyQt5.QtCore import QSize

# Define class to create the table with static data
class SimpleTable(QMainWindow):
    def __init__(self):
        # Call the parent constructor
        super().__init__()

        # Set the size and title of the window
        self.setMinimumSize(QSize(420, 150))
        self.setWindowTitle("Simple Table with Static Data")

        # Create the table with necessary properties
        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(5)
        table.setMinimumWidth(500)
        table.setMinimumHeight(500)

        # Set the table headers
        table.setHorizontalHeaderLabels(["Header-1", "Header-2", "Header-3", "Header-4"])

        # Set the table values
        for i in range(5):
            for j in range(4) :
                table.setItem(i, j, QTableWidgetItem("Row-" + str(i+1) + " , Col-" + str(j+1)))

        # Resize of the rows and columns based on the content
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        # Display the table
        table.show()

        # Display the window in the center of the screen
        win = self.frameGeometry()
        pos = QDesktopWidget().availableGeometry().center()
        win.moveCenter(pos)
        self.move(win.topLeft())
        self.show()

# Create app object and execute the app
app = QApplication(sys.argv)
mw = SimpleTable()
mw.show()
app.exec()