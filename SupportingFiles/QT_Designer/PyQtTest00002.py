import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QApplication, QWidget, QTableWidget, QTableWidgetItem, QFileDialog, QDialog, QPushButton, QDialogButtonBox, QLineEdit
from qgis.core import QgsProject, Qgis
from qgis.utils import iface

filename, _filter = QFileDialog.getOpenFileName(
    iface.mainWindow(), "Select input file ","",
    ("Comma separated values (*.csv);;GeoPackages (*.gpkg);;Shapefiles (*.shp)")
)

model = QStandardItemModel()
tableView = QTableView()

tableView.setModel(model)
tableView.horizontalHeader().setStretchLastSection(True)

with open(filename, "r") as fileInput:
    for i, row in enumerate(csv.reader(fileInput)):
        if i == 0:
            model.setHorizontalHeaderLabels([r.strip().strip('"') for r in row])
        else:
            items = [
                QStandardItem(field.strip())
                for field in row
            ]
            model.appendRow(items)

tableView.show()