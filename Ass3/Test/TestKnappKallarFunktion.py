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


def some_func():
    print("some function has been called!")


def some_other_func():
    print("some other function has been called!")


qt_app = QApplication.instance()
button = QPushButton("Call some function")

button.clicked.connect(some_func)
#         ^               ^
#       signal           slot

button.clicked.connect(some_other_func)  # We can connect multiple slots to a signal.

button.show()
qt_app.exec_()