import sys
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QTableView
from PyQt6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlTableModel
from PyQt6.QtSql import QSqlRelation, QSqlRelationalDelegate


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("PyQt & Relational Databases")

        # Create and setup simple relational table model
        relational_model = QSqlRelationalTableModel()
        relational_model.setTable('orders')
        relational_model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        relational_model.setRelation(2, QSqlRelation('customers', 'id', 'name'))
        relational_model.setRelation(3, QSqlRelation('products', 'id', 'name'))
        relational_model.select()

        # Create headers (optional)
        headers = ("Order ID", "Date Created", "Customer", "Product", "Price", "Qty", "Order Value")
        for columnIndex, header in enumerate(headers):
            relational_model.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)

        # Create a simple table view widget
        table_view = QTableView(self)
        table_view.setAlternatingRowColors(True)
        table_view.setModel(relational_model)
        table_view.setItemDelegate(QSqlRelationalDelegate(table_view))
        table_view.show()

        self.setCentralWidget(table_view)

        w_width = 20
        for col in range(relational_model.columnCount()):
            w_width += table_view.columnWidth(col)
        self.resize(w_width, self.height())


def createConnection() -> bool:
    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName('rdb.db')

    ''' 
    CREATE TABLE "orders" (
 "id" INTEGER NOT NULL UNIQUE,
 "created" TEXT NOT NULL,
 "customer" INTEGER NOT NULL,
 "product" INTEGER NOT NULL,
 "price" NUMERIC NOT NULL,
 "qty" NUMERIC NOT NULL,
 "total" NUMERIC,
 PRIMARY KEY("id")
)
CREATE TABLE "customers" (
 "id" INTEGER NOT NULL,
 "name" TEXT NOT NULL,
 PRIMARY KEY("id")
)
CREATE TABLE "products" (
 "id" INTEGER NOT NULL,
 "name" TEXT NOT NULL,
 PRIMARY KEY("id")
)
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('geek.db')

    # cursor object
    cursor_obj = connection_obj.cursor()

    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

    # Creating table
    table = """ CREATE TABLE GEEK (
                Email VARCHAR(255) NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25),
                Score INT
            ); """

    cursor_obj.execute(table)

    print("Table is Ready")

    # Close the connection
    connection_obj.close()
'''
    if not con.open():
        QMessageBox.critical(
            None,
            'QTableView Example - Error!',
            'Database Error: %s' % con.lastError().databaseText(),
        )
        return False
    return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())