# https://stackoverflow.com/questions/58460653/how-can-i-convert-a-panda-dataframe-or-qtablewidget-to-a-pdf

# Other Useful Article Links
# https://stackoverflow.com/questions/51973991/saving-pandas-dataframe-into-pdf-file-format-without-pdfkit
# https://stackoverflow.com/questions/33155776/export-pandas-dataframe-into-a-pdf-file-using-python
# https://forum.qt.io/topic/78143/export-a-qtablewidget-in-pdf
# https://codeloop.org/how-to-export-file-as-pdf-in-pyqt5/
# https://codeloop.org/how-to-create-pyqt5-qtablewidget-in-qt-designer/
# https://codeloop.org/convert-python-py-file-to-exe-file-with-pyinstaller/
# https://codeloop.org/pyqt5/

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QTextDocument
import sys
import pandas as pd

df = pd.DataFrame({'test1':[1],'test2':[2]}) #the dataframe
html = df.to_html()

app = QApplication(sys.argv)
out = QTextDocument()
out.setHtml(html)
printer = QPrinter()
printer.setOutputFileName("test.pdf")
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setPageSize(QPrinter.A4)
printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)
out.print_(printer)