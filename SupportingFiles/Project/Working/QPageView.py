# https://pypi.org/project/qpageview/
import qpageview

from PyQt5.Qt import *
a = QApplication([])

v = qpageview.View()
v.show()
v.loadPdf("E:\GSReddy\PythonProjects\ResourceManagementSystem\table.pdf")
v.show()