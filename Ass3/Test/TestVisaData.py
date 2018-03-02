# PySide works almost identically, just by changing the module name:
# from PySide.QtCore import *
# from PySide.QtGui import *
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

qt_app = QApplication(sys.argv)

data = ["one", "two", "three", "four", "five"]

model = QStringListModel(data)

combobox = QComboBox()
combobox.setModel(model)
combobox.show()

listView = QListView()
listView.setModel(model)
listView.show()

qt_app.exec_()